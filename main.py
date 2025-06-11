import asyncio
import sys

from app.agent.manus import Manus
from app.logger import logger


async def main():
    """Main entry point for the OpenManus application."""
    logger.info("🚀 Starting OpenManus application...")
    logger.debug(f"Python version: {sys.version}")
    logger.debug(f"Event loop policy: {asyncio.get_event_loop_policy().__class__.__name__}")

    # Create and initialize Manus agent
    logger.info("Initializing Manus agent...")
    try:
        agent = await Manus.create()
        logger.success("✅ Manus agent created successfully")
    except Exception as e:
        logger.error(f"❌ Failed to create Manus agent: {e}")
        logger.exception("Exception details:")
        return

    try:
        logger.info("📝 Waiting for user input...")
        prompt = input("Enter your prompt: ")

        if not prompt.strip():
            logger.warning("⚠️  Empty prompt provided - exiting")
            return

        logger.info(f"📥 Received prompt: '{prompt[:100]}{'...' if len(prompt) > 100 else ''}'")
        logger.info("🔄 Processing your request...")

        # Process the request
        await agent.run(prompt)

        logger.success("✅ Request processing completed successfully")

    except KeyboardInterrupt:
        logger.warning("⚠️  Operation interrupted by user (Ctrl+C)")
    except Exception as e:
        logger.error(f"❌ An error occurred during processing: {e}")
        logger.exception("Exception details:")
    finally:
        # Ensure agent resources are cleaned up before exiting
        logger.info("🧹 Cleaning up agent resources...")
        try:
            await agent.cleanup()
            logger.success("✅ Agent cleanup completed")
        except Exception as e:
            logger.error(f"❌ Error during cleanup: {e}")
            logger.exception("Cleanup exception details:")

        logger.info("👋 OpenManus application shutdown complete")


if __name__ == "__main__":
    logger.info("=" * 50)
    logger.info("🎯 OpenManus - Starting main execution")
    logger.info("=" * 50)

    try:
        asyncio.run(main())
    except Exception as e:
        logger.critical(f"💥 Critical error in main execution: {e}")
        logger.exception("Critical exception details:")
        sys.exit(1)

    logger.info("🏁 Main execution finished")
