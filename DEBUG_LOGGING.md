# OpenManus 详细日志指南 / Detailed Logging Guide

OpenManus 支持多种方式启用详细日志，帮助您调试和监控应用程序的运行状态。

## 启用详细日志的方法 / Methods to Enable Detailed Logging

### 1. 使用命令行参数 / Using Command Line Arguments

#### 启用调试模式 / Enable Debug Mode
```bash
# 使用 --debug 或 -d 参数
python main.py --debug

# 或者使用 --verbose 或 -v 参数（效果相同）
python main.py --verbose
```

#### 设置特定日志级别 / Set Specific Log Level
```bash
# 设置为 DEBUG 级别
python main.py --log-level DEBUG

# 设置为 INFO 级别（默认）
python main.py --log-level INFO

# 设置为 WARNING 级别
python main.py --log-level WARNING
```

#### 直接提供提示词 / Provide Prompt Directly
```bash
# 启用调试并直接运行提示词
python main.py --debug --prompt "你的提示词"

# 或者简写形式
python main.py -d -p "你的提示词"
```

### 2. 使用便捷脚本 / Using Convenience Script

我们提供了一个便捷的调试脚本：

```bash
# 启动调试模式
./debug_mode.sh

# 启动调试模式并提供提示词
./debug_mode.sh --prompt "你的提示词"
```

### 3. 日志文件位置 / Log File Location

详细日志会同时显示在控制台和保存到文件：

- **控制台输出**: 显示设定级别的日志（默认 INFO，调试模式为 DEBUG）
- **文件输出**: 始终保存 DEBUG 级别的完整日志到 `logs/` 目录

日志文件命名格式：`YYYYMMDDHHMMSS.log`

### 4. 日志级别说明 / Log Level Explanation

| 级别 / Level | 说明 / Description |
|-------------|-------------------|
| **DEBUG**   | 最详细的日志，包含所有调试信息、工具调用细节、API 请求响应等 |
| **INFO**    | 正常操作信息，包含主要步骤和状态变更 |
| **WARNING** | 警告信息，可能的问题但不影响正常运行 |
| **ERROR**   | 错误信息，需要注意的问题 |
| **CRITICAL** | 严重错误，可能导致程序终止 |

### 5. 调试模式下的输出示例 / Debug Mode Output Example

启用调试模式后，您将看到类似以下的详细输出：

```
2024-01-01 12:00:00.000 | INFO     | app.logger:define_log_level:28 - OpenManus 启动中... (日志级别: DEBUG)
2024-01-01 12:00:01.000 | DEBUG    | app.agent.manus:initialize_mcp_servers:75 - 初始化 MCP 服务器连接...
2024-01-01 12:00:02.000 | DEBUG    | app.tool.browser_use_tool:_ensure_browser_initialized:142 - 初始化浏览器实例...
2024-01-01 12:00:03.000 | INFO     | app.agent.toolcall:execute_tool:177 - 🔧 Activating tool: 'python_execute'...
2024-01-01 12:00:04.000 | DEBUG    | app.llm:ask:255 - Token usage: Input=150, Completion=45, Total=195
```

### 6. 程序化控制日志级别 / Programmatic Log Level Control

如果您需要在代码中动态调整日志级别：

```python
from app.logger import define_log_level

# 设置为调试级别
logger = define_log_level(print_level="DEBUG", logfile_level="DEBUG")

# 设置为信息级别
logger = define_log_level(print_level="INFO", logfile_level="DEBUG")
```

### 7. 常见使用场景 / Common Use Cases

#### 调试工具调用问题 / Debug Tool Call Issues
```bash
python main.py --debug --prompt "帮我分析这个错误"
```

#### 监控 API 调用和 Token 使用 / Monitor API Calls and Token Usage
```bash
python main.py --verbose
```

#### 生产环境警告级别日志 / Production Warning Level Logs
```bash
python main.py --log-level WARNING
```

## 注意事项 / Notes

1. **性能影响**: DEBUG 级别日志会产生大量输出，可能影响性能
2. **日志文件大小**: 详细日志会快速增长，定期清理 `logs/` 目录
3. **敏感信息**: 调试日志可能包含敏感信息，请注意安全性
4. **存储空间**: 确保有足够的磁盘空间存储日志文件

## 故障排除 / Troubleshooting

如果日志未按预期显示：

1. 检查 `logs/` 目录权限
2. 确认命令行参数正确
3. 检查是否有其他程序占用日志文件
4. 验证 Python 路径和模块导入

---

通过这些方法，您可以根据需要灵活控制 OpenManus 的日志详细程度，更好地理解和调试应用程序的行为。
