#!/usr/bin/env python
import argparse
import asyncio
import sys

from app.agent.mcp import MCPAgent
from app.config import config
from app.logger import logger


class MCPRunner:
    """Runner class for MCP Agent with proper path handling and configuration."""

    def __init__(self):
        logger.debug("🏗️ Initializing MCPRunner")
        self.root_path = config.root_path
        self.server_reference = config.mcp_config.server_reference
        self.agent = MCPAgent()
        logger.debug(f"📁 Root path: {self.root_path}")
        logger.debug(f"🔗 Server reference: {self.server_reference}")

    async def initialize(
        self,
        connection_type: str,
        server_url: str | None = None,
    ) -> None:
        """Initialize the MCP agent with the appropriate connection."""
        logger.info(f"🔧 Initializing MCPAgent with {connection_type} connection...")

        try:
            if connection_type == "stdio":
                logger.debug(f"📡 Setting up STDIO connection with command: {sys.executable}")
                await self.agent.initialize(
                    connection_type="stdio",
                    command=sys.executable,
                    args=["-m", self.server_reference],
                )
            else:  # sse
                logger.debug(f"🌐 Setting up SSE connection to: {server_url}")
                await self.agent.initialize(connection_type="sse", server_url=server_url)

            logger.info(f"✅ Connected to MCP server via {connection_type}")
        except Exception as e:
            logger.error(f"❌ Failed to initialize MCP connection: {e}", exc_info=True)
            raise

    async def run_interactive(self) -> None:
        """Run the agent in interactive mode."""
        logger.info("🎮 Starting interactive mode")
        print("\nMCP Agent Interactive Mode (type 'exit' to quit)\n")

        while True:
            try:
                user_input = input("\nEnter your request: ")
                if user_input.lower() in ["exit", "quit", "q"]:
                    logger.info("👋 User requested exit from interactive mode")
                    break

                if not user_input.strip():
                    logger.warning("⚠️ Empty input received, skipping")
                    continue

                logger.info(f"📝 Processing user input: '{user_input[:50]}{'...' if len(user_input) > 50 else ''}'")
                response = await self.agent.run(user_input)
                print(f"\nAgent: {response}")
                logger.debug("✅ Request processed successfully")

            except KeyboardInterrupt:
                logger.warning("⚠️ Interactive mode interrupted by user")
                break
            except Exception as e:
                logger.error(f"❌ Error in interactive mode: {e}")
                print(f"Error: {e}")

    async def run_single_prompt(self, prompt: str) -> None:
        """Run the agent with a single prompt."""
        logger.info(f"🎯 Running single prompt: '{prompt[:50]}{'...' if len(prompt) > 50 else ''}'")
        try:
            await self.agent.run(prompt)
            logger.info("✅ Single prompt execution completed")
        except Exception as e:
            logger.error(f"❌ Error executing single prompt: {e}", exc_info=True)
            raise

    async def run_default(self) -> None:
        """Run the agent in default mode."""
        logger.info("🏠 Starting default mode")
        prompt = input("Enter your prompt: ")
        if not prompt.strip():
            logger.warning("⚠️ Empty prompt provided")
            return

        logger.info(f"📝 User prompt received: '{prompt[:100]}{'...' if len(prompt) > 100 else ''}'")
        logger.info("🔄 Processing your request...")

        try:
            await self.agent.run(prompt)
            logger.info("✅ Request processing completed")
        except Exception as e:
            logger.error(f"❌ Error during request processing: {e}", exc_info=True)
            raise

    async def cleanup(self) -> None:
        """Clean up agent resources."""
        logger.info("🧹 Starting cleanup process...")
        try:
            await self.agent.cleanup()
            logger.info("✅ Agent cleanup completed successfully")
        except Exception as e:
            logger.error(f"❌ Error during cleanup: {e}")
        logger.info("👋 Session ended")


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run the MCP Agent")
    parser.add_argument(
        "--connection",
        "-c",
        choices=["stdio", "sse"],
        default="stdio",
        help="Connection type: stdio or sse",
    )
    parser.add_argument(
        "--server-url",
        default="http://127.0.0.1:8000/sse",
        help="URL for SSE connection",
    )
    parser.add_argument(
        "--interactive", "-i", action="store_true", help="Run in interactive mode"
    )
    parser.add_argument("--prompt", "-p", help="Single prompt to execute and exit")
    return parser.parse_args()


async def run_mcp() -> None:
    """Main entry point for the MCP runner."""
    logger.info("🚀 Starting MCP Agent application")

    args = parse_args()
    logger.debug(f"📋 Arguments parsed - Connection: {args.connection}, Interactive: {args.interactive}")

    runner = MCPRunner()

    try:
        await runner.initialize(args.connection, args.server_url)

        if args.prompt:
            logger.info("🎯 Single prompt mode selected")
            await runner.run_single_prompt(args.prompt)
        elif args.interactive:
            logger.info("🎮 Interactive mode selected")
            await runner.run_interactive()
        else:
            logger.info("🏠 Default mode selected")
            await runner.run_default()

    except KeyboardInterrupt:
        logger.warning("⚠️ Program interrupted by user")
    except Exception as e:
        logger.error(f"❌ Critical error running MCPAgent: {str(e)}", exc_info=True)
        sys.exit(1)
    finally:
        await runner.cleanup()
        logger.info("👋 MCP Agent application terminated")


if __name__ == "__main__":
    asyncio.run(run_mcp())
