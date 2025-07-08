# OpenManus 详细日志使用示例 / Usage Examples for Detailed Logging

## 快速开始 / Quick Start

### 1. 启用调试日志 / Enable Debug Logging

```bash
# 方法一：使用调试脚本（推荐）
./debug_mode.sh

# 方法二：使用命令行参数
python main.py --debug

# 方法三：使用 verbose 参数（与 debug 相同）
python main.py --verbose
```

### 2. 指定日志级别 / Specify Log Level

```bash
# 最详细的调试信息
python main.py --log-level DEBUG

# 标准信息（默认）
python main.py --log-level INFO

# 仅警告和错误
python main.py --log-level WARNING

# 仅错误信息
python main.py --log-level ERROR
```

### 3. 非交互模式运行 / Non-interactive Mode

```bash
# 启用调试并直接提供提示词
python main.py --debug --prompt "请帮我创建一个Python脚本"

# 简写形式
python main.py -d -p "分析这个文件的内容"

# 使用调试脚本（非交互）
./debug_mode.sh --prompt "你的提示词"
```

## 输出对比 / Output Comparison

### 普通模式输出 / Normal Mode Output
```
2024-01-01 12:00:00 | INFO | OpenManus 启动中... (日志级别: INFO)
2024-01-01 12:00:01 | INFO | 正在处理您的请求...
2024-01-01 12:00:05 | INFO | 请求处理完成
```

### 调试模式输出 / Debug Mode Output
```
2024-01-01 12:00:00 | INFO | OpenManus 启动中... (日志级别: DEBUG)
2024-01-01 12:00:01 | DEBUG | 初始化 MCP 服务器连接...
2024-01-01 12:00:01 | DEBUG | 加载工具集合...
2024-01-01 12:00:01 | INFO | 正在处理您的请求...
2024-01-01 12:00:02 | DEBUG | 🧰 Tools being prepared: ['python_execute']
2024-01-01 12:00:02 | DEBUG | 🔧 Tool arguments: {"code": "print('Hello World')"}
2024-01-01 12:00:03 | INFO | 🔧 Activating tool: 'python_execute'...
2024-01-01 12:00:03 | DEBUG | Token usage: Input=150, Completion=45, Total=195
2024-01-01 12:00:05 | INFO | 请求处理完成
```

## 常见使用场景 / Common Use Cases

### 调试工具问题 / Debug Tool Issues
```bash
# 当某个工具不工作时，查看详细执行过程
python main.py --debug --prompt "使用浏览器工具搜索信息"
```

### 监控性能 / Monitor Performance
```bash
# 监控 Token 使用和 API 调用
python main.py --verbose --prompt "复杂的数据分析任务"
```

### 开发新功能 / Develop New Features
```bash
# 开发时查看详细的内部状态
python main.py --log-level DEBUG --prompt "测试新功能"
```

### 生产环境监控 / Production Monitoring
```bash
# 生产环境只显示警告和错误
python main.py --log-level WARNING
```

## 日志文件管理 / Log File Management

### 查看最新日志文件 / View Latest Log File
```bash
# 查看最新的日志文件
ls -la logs/ | tail -1
cat logs/$(ls -t logs/ | head -1)
```

### 监控实时日志 / Monitor Real-time Logs
```bash
# 实时监控最新日志文件
tail -f logs/$(ls -t logs/ | head -1)
```

### 清理旧日志 / Clean Old Logs
```bash
# 删除 7 天前的日志文件
find logs/ -name "*.log" -mtime +7 -delete

# 只保留最近 10 个日志文件
ls -t logs/*.log | tail -n +11 | xargs rm -f
```

## 故障排除 / Troubleshooting Examples

### 问题：工具调用失败 / Issue: Tool Call Failure
```bash
# 启用详细日志查看工具调用详情
python main.py --debug --prompt "执行失败的任务"
```

### 问题：性能问题 / Issue: Performance Problems
```bash
# 监控 Token 使用和响应时间
python main.py --verbose --prompt "性能测试任务"
```

### 问题：连接问题 / Issue: Connection Problems
```bash
# 查看 MCP 服务器连接详情
python main.py --debug --prompt "需要外部服务的任务"
```

## 自定义日志配置 / Custom Log Configuration

如果您需要更复杂的日志配置，可以直接修改代码：

```python
from app.logger import define_log_level

# 自定义日志配置
logger = define_log_level(
    print_level="DEBUG",      # 控制台输出级别
    logfile_level="DEBUG",    # 文件输出级别
    name="custom_session"     # 自定义日志文件前缀
)
```

## 提示与技巧 / Tips and Tricks

1. **文件大小控制**: 调试模式会产生大量日志，定期清理 `logs/` 目录
2. **性能考虑**: 生产环境建议使用 INFO 或 WARNING 级别
3. **安全考虑**: DEBUG 日志可能包含敏感信息，注意文件权限
4. **存储管理**: 确保有足够的磁盘空间存储日志文件

---

通过这些示例，您可以根据具体需求选择合适的日志级别和使用方式。
