import asyncio
import os
from typing import Optional

from app.exceptions import ToolError
from app.tool.base import BaseTool, CLIResult
from app.logger import logger


_BASH_DESCRIPTION = """Execute a bash command in the terminal.
* Long running commands: For commands that may run indefinitely, it should be run in the background and the output should be redirected to a file, e.g. command = `python3 app.py > server.log 2>&1 &`.
* Interactive: If a bash command returns exit code `-1`, this means the process is not yet finished. The assistant must then send a second call to terminal with an empty `command` (which will retrieve any additional logs), or it can send additional text (set `command` to the text) to STDIN of the running process, or it can send command=`ctrl+c` to interrupt the process.
* Timeout: If a command execution result says "Command timed out. Sending SIGINT to the process", the assistant should retry running the command in the background.
"""


class _BashSession:
    """A session of a bash shell."""

    _started: bool
    _process: asyncio.subprocess.Process

    command: str = "/bin/bash"
    _output_delay: float = 0.2  # seconds
    _timeout: float = 120.0  # seconds
    _sentinel: str = "<<exit>>"

    def __init__(self):
        self._started = False
        self._timed_out = False
        logger.debug("🐚 Bash session initialized")

    async def start(self):
        if self._started:
            logger.debug("🔄 Bash session already started")
            return

        logger.debug("🚀 Starting new bash session")
        self._process = await asyncio.create_subprocess_shell(
            self.command,
            preexec_fn=os.setsid,
            shell=True,
            bufsize=0,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        self._started = True
        logger.info("✅ Bash session started successfully")

    def stop(self):
        """Terminate the bash shell."""
        if not self._started:
            logger.error("❌ Cannot stop bash session: not started")
            raise ToolError("Session has not started.")
        if self._process.returncode is not None:
            logger.debug("🔄 Bash process already terminated")
            return
        logger.info("🛑 Terminating bash session")
        self._process.terminate()

    async def run(self, command: str):
        """Execute a command in the bash shell."""
        logger.info(f"🐚 Executing bash command: {command}")

        if not self._started:
            logger.error("❌ Bash session not started")
            raise ToolError("Session has not started.")
        if self._process.returncode is not None:
            logger.warning(f"⚠️ Bash process exited with code {self._process.returncode}")
            return CLIResult(
                system="tool must be restarted",
                error=f"bash has exited with returncode {self._process.returncode}",
            )
        if self._timed_out:
            logger.error(f"⏰ Bash session timed out after {self._timeout} seconds")
            raise ToolError(
                f"timed out: bash has not returned in {self._timeout} seconds and must be restarted",
            )

        # we know these are not None because we created the process with PIPEs
        assert self._process.stdin
        assert self._process.stdout
        assert self._process.stderr

        # send command to the process
        logger.debug(f"📤 Sending command to bash: {command}")
        self._process.stdin.write(
            command.encode() + f"; echo '{self._sentinel}'\n".encode()
        )
        await self._process.stdin.drain()

        # read output from the process, until the sentinel is found
        try:
            async with asyncio.timeout(self._timeout):
                logger.debug(f"⏳ Waiting for command output (timeout: {self._timeout}s)")
                while True:
                    await asyncio.sleep(self._output_delay)
                    # if we read directly from stdout/stderr, it will wait forever for
                    # EOF. use the StreamReader buffer directly instead.
                    output = (
                        self._process.stdout._buffer.decode()
                    )  # pyright: ignore[reportAttributeAccessIssue]
                    if self._sentinel in output:
                        # strip the sentinel and break
                        output = output[: output.index(self._sentinel)]
                        logger.debug("✅ Command output received, sentinel found")
                        break
        except asyncio.TimeoutError:
            self._timed_out = True
            logger.error(f"⏰ Bash command timed out after {self._timeout} seconds")
            raise ToolError(
                f"timed out: bash has not returned in {self._timeout} seconds and must be restarted",
            ) from None

        if output.endswith("\n"):
            output = output[:-1]

        error = (
            self._process.stderr._buffer.decode()
        )  # pyright: ignore[reportAttributeAccessIssue]
        if error.endswith("\n"):
            error = error[:-1]

        # clear the buffers so that the next output can be read correctly
        self._process.stdout._buffer.clear()  # pyright: ignore[reportAttributeAccessIssue]
        self._process.stderr._buffer.clear()  # pyright: ignore[reportAttributeAccessIssue]

        result = CLIResult(output=output, error=error)
        if error:
            logger.warning(f"⚠️ Bash command completed with stderr: {error}")
        else:
            logger.info("✅ Bash command completed successfully")

        return result


class Bash(BaseTool):
    """A tool for executing bash commands"""

    name: str = "bash"
    description: str = _BASH_DESCRIPTION
    parameters: dict = {
        "type": "object",
        "properties": {
            "command": {
                "type": "string",
                "description": "The bash command to execute. Can be empty to view additional logs when previous exit code is `-1`. Can be `ctrl+c` to interrupt the currently running process.",
            },
        },
        "required": ["command"],
    }

    _session: Optional[_BashSession] = None

    async def execute(
        self, command: str | None = None, restart: bool = False, **kwargs
    ) -> CLIResult:
        logger.debug(f"🐚 Bash tool execute called - restart: {restart}, command: {command}")

        if restart:
            logger.info("🔄 Restarting bash session")
            if self._session:
                self._session.stop()
            self._session = _BashSession()
            await self._session.start()

            return CLIResult(system="tool has been restarted.")

        if self._session is None:
            logger.info("🚀 Creating new bash session")
            self._session = _BashSession()
            await self._session.start()

        if command is not None:
            try:
                result = await self._session.run(command)
                logger.debug(f"📄 Bash command result: output_len={len(result.output or '')}, error_len={len(result.error or '')}")
                return result
            except Exception as e:
                logger.error(f"❌ Error executing bash command: {e}")
                raise

        logger.error("❌ No command provided to bash tool")
        raise ToolError("no command provided.")


if __name__ == "__main__":
    bash = Bash()
    rst = asyncio.run(bash.execute("ls -l"))
    print(rst)
