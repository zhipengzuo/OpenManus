import asyncio

from app.agent.manus import Manus
from app.logger import logger


async def main():
    logger.info("🚀 Starting OpenManus application")

    # Create and initialize Manus agent
    logger.info("🤖 Initializing Manus agent...")
    try:
        agent = await Manus.create()
        logger.info("✅ Manus agent initialized successfully")
    except Exception as e:
        logger.error(f"❌ Failed to initialize Manus agent: {e}")
        return

    try:
        prompt = input("Enter your prompt: ")
        if not prompt.strip():
            logger.warning("⚠️ Empty prompt provided")
            return

        logger.info(f"📝 User prompt received: '{prompt[:100]}{'...' if len(prompt) > 100 else ''}'")
        logger.info("🔄 Processing your request...")

        result = await agent.run(prompt)

        logger.info("✅ Request processing completed successfully")
        logger.debug(f"📄 Final result: {result}")

    except KeyboardInterrupt:
        logger.warning("⚠️ Operation interrupted by user")
    except Exception as e:
        logger.error(f"❌ Error during execution: {e}", exc_info=True)
    finally:
        # Ensure agent resources are cleaned up before exiting
        logger.info("🧹 Cleaning up resources...")
        try:
            await agent.cleanup()
            logger.info("✅ Cleanup completed successfully")
        except Exception as e:
            logger.error(f"❌ Error during cleanup: {e}")

        logger.info("👋 OpenManus application terminated")


if __name__ == "__main__":
    asyncio.run(main())
