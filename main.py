import asyncio
import argparse

from app.agent.manus import Manus
from app.logger import logger, define_log_level


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="OpenManus - 多功能AI代理")
    parser.add_argument(
        "--debug", "-d",
        action="store_true",
        help="启用调试级别日志 (Enable debug level logging)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="启用详细日志 (Enable verbose logging - same as debug)"
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="设置日志级别 (Set logging level)"
    )
    parser.add_argument(
        "--prompt", "-p",
        help="直接提供提示词，不进入交互模式 (Provide prompt directly, skip interactive mode)"
    )
    return parser.parse_args()


async def main():
    args = parse_args()

    # Configure logging based on arguments
    log_level = "DEBUG" if (args.debug or args.verbose) else args.log_level
    global logger
    logger = define_log_level(print_level=log_level, logfile_level="DEBUG")

    logger.info(f"OpenManus 启动中... (日志级别: {log_level})")

    # Create and initialize Manus agent
    agent = await Manus.create()
    try:
        if args.prompt:
            prompt = args.prompt
            logger.info(f"使用提供的提示词: {prompt}")
        else:
            prompt = input("请输入您的提示词 (Enter your prompt): ")

        if not prompt.strip():
            logger.warning("提供的提示词为空 (Empty prompt provided).")
            return

        logger.warning("正在处理您的请求... (Processing your request...)")
        await agent.run(prompt)
        logger.info("请求处理完成 (Request processing completed).")
    except KeyboardInterrupt:
        logger.warning("操作被中断 (Operation interrupted).")
    finally:
        # Ensure agent resources are cleaned up before exiting
        await agent.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
