#!/bin/bash

# OpenManus 调试模式启动脚本
# OpenManus Debug Mode Startup Script

echo "🚀 启动 OpenManus 调试模式 (Starting OpenManus in Debug Mode)"
echo "📝 详细日志将显示所有调试信息 (Verbose logging will show all debug information)"
echo "📁 日志文件也会保存到 logs/ 目录下 (Log files will also be saved to logs/ directory)"
echo ""

# 确保 logs 目录存在
mkdir -p logs

# 启动应用程序并启用调试日志
python main.py --debug "$@"
