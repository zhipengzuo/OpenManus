import asyncio
import time

from app.agent.manus import Manus
from app.flow.flow_factory import FlowFactory, FlowType
from app.logger import logger


async def run_flow():
    logger.info("🚀 Starting OpenManus Flow execution")

    agents = {
        "manus": Manus(),
    }
    logger.info("🤖 Agents initialized for flow execution")

    try:
        prompt = input("Enter your prompt: ")

        if prompt.strip().isspace() or not prompt:
            logger.warning("⚠️ Empty prompt provided")
            return

        logger.info(f"📝 User prompt received: '{prompt[:100]}{'...' if len(prompt) > 100 else ''}'")

        logger.info("🏗️ Creating planning flow...")
        flow = FlowFactory.create_flow(
            flow_type=FlowType.PLANNING,
            agents=agents,
        )
        logger.info("✅ Planning flow created successfully")
        logger.info("🔄 Processing your request...")

        try:
            start_time = time.time()
            logger.debug(f"⏱️ Flow execution started at {time.strftime('%Y-%m-%d %H:%M:%S')}")

            result = await asyncio.wait_for(
                flow.execute(prompt),
                timeout=3600,  # 60 minute timeout for the entire execution
            )

            elapsed_time = time.time() - start_time
            logger.info(f"✅ Request processed successfully in {elapsed_time:.2f} seconds")
            logger.info(f"📄 Flow execution result: {result}")

        except asyncio.TimeoutError:
            logger.error("⏰ Request processing timed out after 1 hour")
            logger.warning("Operation terminated due to timeout. Please try a simpler request.")

    except KeyboardInterrupt:
        logger.warning("⚠️ Operation cancelled by user")
    except Exception as e:
        logger.error(f"❌ Unexpected error during flow execution: {str(e)}", exc_info=True)
    finally:
        logger.info("🧹 Cleaning up flow resources...")
        # Note: Add any specific cleanup if needed
        logger.info("👋 Flow execution completed")


if __name__ == "__main__":
    asyncio.run(run_flow())
