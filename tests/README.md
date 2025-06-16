# 谷歌搜索工具单元测试

本目录包含了为谷歌搜索工具创建的完整单元测试套件。

## 测试覆盖范围

### 1. GoogleSearchEngine 测试 (`tests/tool/test_google_search.py`)

测试 `app/tool/search/google_search.py` 中的 `GoogleSearchEngine` 类：

- ✅ **基本搜索功能**: 测试正常搜索流程
- ✅ **结果格式处理**: 测试高级结果对象和简单URL字符串的处理
- ✅ **混合结果处理**: 测试同时包含对象和字符串的搜索结果
- ✅ **空结果处理**: 测试无搜索结果的情况
- ✅ **参数验证**: 测试默认和自定义参数
- ✅ **异常处理**: 测试搜索API错误和格式错误对象
- ✅ **继承验证**: 测试类继承关系
- ✅ **方法签名**: 测试方法签名正确性
- ✅ **集成测试**: 可选的真实网络搜索测试（默认跳过）

**测试统计**: 2 个测试类，12 个测试方法

### 2. WebSearch 测试 (`tests/tool/test_web_search.py`)

测试 `app/tool/web_search.py` 中的 `WebSearch` 类和相关组件：

#### WebSearch 类测试
- ✅ **成功搜索执行**: 测试完整搜索流程
- ✅ **内容获取**: 测试启用内容获取的搜索
- ✅ **失败重试机制**: 测试搜索失败时的重试逻辑
- ✅ **自定义语言和国家**: 测试国际化参数
- ✅ **谷歌搜索优先**: 测试谷歌搜索引擎优先使用
- ✅ **搜索引擎切换**: 测试谷歌失败时的备用引擎
- ✅ **引擎顺序配置**: 测试搜索引擎优先级配置

#### WebContentFetcher 类测试
- ✅ **成功内容获取**: 测试HTML内容解析和清理
- ✅ **HTTP错误处理**: 测试404等HTTP错误
- ✅ **请求异常处理**: 测试网络连接错误
- ✅ **超时参数**: 测试自定义超时设置
- ✅ **内容大小限制**: 测试10KB内容大小限制

#### SearchResponse 模型测试
- ✅ **输出格式化**: 测试搜索结果的格式化输出
- ✅ **错误输出**: 测试错误情况的输出格式

**测试统计**: 3 个测试类，17 个测试方法

## 运行测试

### 环境准备

1. 安装依赖项：
```bash
pip install -r requirements.txt
```

2. 确保项目根目录在Python路径中：
```bash
export PYTHONPATH=/workspace:$PYTHONPATH
```

### 运行所有谷歌搜索相关测试

```bash
# 使用pytest直接运行
python -m pytest tests/tool/test_google_search.py tests/tool/test_web_search.py -v

# 使用提供的测试脚本
python run_tests.py --google

# 运行带覆盖率报告的测试
python run_tests.py --google --coverage
```

### 运行单个测试文件

```bash
# 只运行GoogleSearchEngine测试
python -m pytest tests/tool/test_google_search.py -v

# 只运行WebSearch测试
python -m pytest tests/tool/test_web_search.py -v
```

### 运行特定测试方法

```bash
# 运行特定测试方法
python -m pytest tests/tool/test_google_search.py::TestGoogleSearchEngine::test_perform_search_with_advanced_results -v

# 运行特定测试类
python -m pytest tests/tool/test_web_search.py::TestWebSearch -v
```

### 跳过集成测试

默认情况下，需要网络访问的集成测试会被跳过。如需运行集成测试：

```bash
python -m pytest tests/tool/test_google_search.py -m integration -v
```

## 测试特性

### Mock 和 Patch
- 使用 `unittest.mock` 模拟外部依赖
- Mock `googlesearch` 库避免实际网络请求
- Mock `requests` 库测试网页内容获取
- Mock `asyncio.sleep` 测试重试机制

### 异步测试
- 使用 `pytest-asyncio` 测试异步方法
- 支持 `@pytest.mark.asyncio` 装饰器
- 测试并发操作和异步内容获取

### 参数化测试
- 使用 `@pytest.fixture` 提供测试数据
- 模拟不同类型的搜索结果格式
- 测试多种异常情况

### 标记系统
- `@pytest.mark.integration`: 集成测试标记
- `@pytest.mark.unit`: 单元测试标记
- `@pytest.mark.slow`: 慢速测试标记

## 代码覆盖率

目标代码覆盖率：**90%+**

主要覆盖区域：
- GoogleSearchEngine 类的所有公共方法
- WebSearch 类的核心搜索逻辑
- WebContentFetcher 的内容获取功能
- SearchResponse 的数据模型验证
- 异常处理和边界情况

## 维护和扩展

### 添加新测试
1. 在相应的测试类中添加新的测试方法
2. 使用描述性的测试方法名：`test_功能_场景`
3. 添加适当的文档字符串说明测试目的
4. 使用合适的断言检查结果

### 更新测试
当搜索工具代码发生变化时：
1. 检查是否需要更新相关的Mock对象
2. 验证测试断言仍然有效
3. 添加针对新功能的测试用例
4. 运行完整测试套件确保兼容性

### 最佳实践
- 保持测试独立性，避免测试间相互依赖
- 使用有意义的测试数据
- 优先测试边界条件和异常情况
- 定期审查和重构测试代码
- 保持测试代码的可读性和可维护性
