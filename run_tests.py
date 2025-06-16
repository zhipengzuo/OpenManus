#!/usr/bin/env python3
"""
测试运行脚本
使用示例:
    python run_tests.py                    # 运行所有测试
    python run_tests.py --google           # 只运行谷歌搜索相关测试
    python run_tests.py --unit             # 只运行单元测试
    python run_tests.py --integration      # 只运行集成测试
"""

import argparse
import subprocess
import sys


def run_command(cmd):
    """运行命令并返回结果"""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    return result.returncode


def main():
    parser = argparse.ArgumentParser(description="Run tests for OpenManus project")
    parser.add_argument("--google", action="store_true", help="Run only Google search tests")
    parser.add_argument("--unit", action="store_true", help="Run only unit tests")
    parser.add_argument("--integration", action="store_true", help="Run only integration tests")
    parser.add_argument("--coverage", action="store_true", help="Run tests with coverage report")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    args = parser.parse_args()

    cmd = ["python", "-m", "pytest"]

    if args.verbose:
        cmd.append("-v")

    if args.google:
        cmd.extend(["tests/tool/test_google_search.py", "tests/tool/test_web_search.py"])
    elif args.unit:
        cmd.extend(["-m", "unit"])
    elif args.integration:
        cmd.extend(["-m", "integration"])
    else:
        cmd.append("tests/")

    if args.coverage:
        cmd = ["python", "-m", "pytest", "--cov=app", "--cov-report=html", "--cov-report=term"] + cmd[3:]

    return run_command(cmd)


if __name__ == "__main__":
    sys.exit(main())
