import multiprocessing
import sys
from io import StringIO
from typing import Dict

from app.tool.base import BaseTool
from app.logger import logger


class PythonExecute(BaseTool):
    """A tool for executing Python code with timeout and safety restrictions."""

    name: str = "python_execute"
    description: str = "Executes Python code string. Note: Only print outputs are visible, function return values are not captured. Use print statements to see results."
    parameters: dict = {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": "The Python code to execute.",
            },
        },
        "required": ["code"],
    }

    def _run_code(self, code: str, result_dict: dict, safe_globals: dict) -> None:
        logger.debug("🐍 Starting Python code execution in subprocess")
        original_stdout = sys.stdout
        try:
            output_buffer = StringIO()
            sys.stdout = output_buffer
            logger.debug(f"📝 Executing code: {code[:100]}{'...' if len(code) > 100 else ''}")
            exec(code, safe_globals, safe_globals)
            output = output_buffer.getvalue()
            result_dict["observation"] = output
            result_dict["success"] = True
            logger.debug(f"✅ Code execution successful, output length: {len(output)} characters")
        except Exception as e:
            logger.warning(f"⚠️ Code execution failed: {e}")
            result_dict["observation"] = str(e)
            result_dict["success"] = False
        finally:
            sys.stdout = original_stdout

    async def execute(
        self,
        code: str,
        timeout: int = 5,
    ) -> Dict:
        """
        Executes the provided Python code with a timeout.

        Args:
            code (str): The Python code to execute.
            timeout (int): Execution timeout in seconds.

        Returns:
            Dict: Contains 'output' with execution output or error message and 'success' status.
        """
        logger.info(f"🐍 Executing Python code (timeout: {timeout}s)")
        logger.debug(f"📋 Code to execute: {code}")

        with multiprocessing.Manager() as manager:
            result = manager.dict({"observation": "", "success": False})
            if isinstance(__builtins__, dict):
                safe_globals = {"__builtins__": __builtins__}
            else:
                safe_globals = {"__builtins__": __builtins__.__dict__.copy()}

            logger.debug("🚀 Starting subprocess for code execution")
            proc = multiprocessing.Process(
                target=self._run_code, args=(code, result, safe_globals)
            )
            proc.start()
            proc.join(timeout)

            # timeout process
            if proc.is_alive():
                logger.warning(f"⏰ Code execution timed out after {timeout} seconds, terminating process")
                proc.terminate()
                proc.join(1)
                return {
                    "observation": f"Execution timeout after {timeout} seconds",
                    "success": False,
                }

            final_result = dict(result)
            if final_result["success"]:
                logger.info("✅ Python code execution completed successfully")
            else:
                logger.warning(f"⚠️ Python code execution failed: {final_result['observation']}")

            return final_result
