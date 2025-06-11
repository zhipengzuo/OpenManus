<p align="center">
  <img src="assets/logo.jpg" width="200"/>
</p>

[English](README.md) | 中文 | [한국어](README_ko.md) | [日本語](README_ja.md)

[![GitHub stars](https://img.shields.io/github/stars/FoundationAgents/OpenManus?style=social)](https://github.com/FoundationAgents/OpenManus/stargazers)
&ensp;
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) &ensp;
[![Discord Follow](https://dcbadge.vercel.app/api/server/DYn29wFk9z?style=flat)](https://discord.gg/DYn29wFk9z)
[![Demo](https://img.shields.io/badge/Demo-Hugging%20Face-yellow)](https://huggingface.co/spaces/lyh-917/OpenManusDemo)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15186407.svg)](https://doi.org/10.5281/zenodo.15186407)

# 👋 OpenManus

Manus 非常棒，但 OpenManus 无需邀请码即可实现任何创意 🛫！

我们的团队成员 [@Xinbin Liang](https://github.com/mannaandpoem) 和 [@Jinyu Xiang](https://github.com/XiangJinyu)（核心作者），以及 [@Zhaoyang Yu](https://github.com/MoshiQAQ)、[@Jiayi Zhang](https://github.com/didiforgithub) 和 [@Sirui Hong](https://github.com/stellaHSR)，来自 [@MetaGPT](https://github.com/geekan/MetaGPT)团队。我们在 3
小时内完成了开发并持续迭代中！

这是一个简洁的实现方案，欢迎任何建议、贡献和反馈！

用 OpenManus 开启你的智能体之旅吧！

我们也非常高兴地向大家介绍 [OpenManus-RL](https://github.com/OpenManus/OpenManus-RL)，这是一个专注于基于强化学习（RL，例如 GRPO）的方法来优化大语言模型（LLM）智能体的开源项目，由来自UIUC 和 OpenManus 的研究人员合作开发。

## 项目演示

<video src="https://private-user-images.githubusercontent.com/61239030/420168772-6dcfd0d2-9142-45d9-b74e-d10aa75073c6.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDEzMTgwNTksIm5iZiI6MTc0MTMxNzc1OSwicGF0aCI6Ii82MTIzOTAzMC80MjAxNjg3NzItNmRjZmQwZDItOTE0Mi00NWQ5LWI3NGUtZDEwYWE3NTA3M2M2Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA3VDAzMjIzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdiZjFkNjlmYWNjMmEzOTliM2Y3M2VlYjgyNDRlZDJmOWE3NWZhZjE1MzhiZWY4YmQ3NjdkNTYwYTU5ZDA2MzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.UuHQCgWYkh0OQq9qsUWqGsUbhG3i9jcZDAMeHjLt5T4" data-canonical-src="https://private-user-images.githubusercontent.com/61239030/420168772-6dcfd0d2-9142-45d9-b74e-d10aa75073c6.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDEzMTgwNTksIm5iZiI6MTc0MTMxNzc1OSwicGF0aCI6Ii82MTIzOTAzMC80MjAxNjg3NzItNmRjZmQwZDItOTE0Mi00NWQ5LWI3NGUtZDEwYWE3NTA3M2M2Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA3VDAzMjIzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdiZjFkNjlmYWNjMmEzOTliM2Y3M2VlYjgyNDRlZDJmOWE3NWZhZjE1MzhiZWY4YmQ3NjdkNTYwYTU5ZDA2MzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.UuHQCgWYkh0OQq9qsUWqGsUbhG3i9jcZDAMeHjLt5T4" controls="controls" muted="muted" class="d-block rounded-bottom-2 border-top width-fit" style="max-height:640px; min-height: 200px"></video>

## 安装指南

我们提供两种安装方式。推荐使用方式二（uv），因为它能提供更快的安装速度和更好的依赖管理。

### 方式一：使用 conda

1. 创建新的 conda 环境：

```bash
conda create -n open_manus python=3.12
conda activate open_manus
```

2. 克隆仓库：

```bash
git clone https://github.com/FoundationAgents/OpenManus.git
cd OpenManus
```

3. 安装依赖：

```bash
pip install -r requirements.txt
```

### 方式二：使用 uv（推荐）

1. 安装 uv（一个快速的 Python 包管理器）：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. 克隆仓库：

```bash
git clone https://github.com/FoundationAgents/OpenManus.git
cd OpenManus
```

3. 创建并激活虚拟环境：

```bash
uv venv --python 3.12
source .venv/bin/activate  # Unix/macOS 系统
# Windows 系统使用：
# .venv\Scripts\activate
```

4. 安装依赖：

```bash
uv pip install -r requirements.txt
```

### 浏览器自动化工具（可选）
```bash
playwright install
```

## 配置说明

OpenManus 需要配置使用的 LLM API，请按以下步骤设置：

1. 在 `config` 目录创建 `config.toml` 文件（可从示例复制）：

```bash
cp config/config.example.toml config/config.toml
```

2. 编辑 `config/config.toml` 添加 API 密钥和自定义设置：

```toml
# 全局 LLM 配置
[llm]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."  # 替换为真实 API 密钥
max_tokens = 4096
temperature = 0.0

# 可选特定 LLM 模型配置
[llm.vision]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."  # 替换为真实 API 密钥
```

## 快速启动

一行命令运行 OpenManus：

```bash
python main.py
```

然后通过终端输入你的创意！

如需使用 MCP 工具版本，可运行：
```bash
python run_mcp.py
```

如需体验不稳定的多智能体版本，可运行：

```bash
python run_flow.py
```

## 贡献指南

我们欢迎任何友好的建议和有价值的贡献！可以直接创建 issue 或提交 pull request。

或通过 📧 邮件联系 @mannaandpoem：mannaandpoem@gmail.com

**注意**: 在提交 pull request 之前，请使用 pre-commit 工具检查您的更改。运行 `pre-commit run --all-files` 来执行检查。

## 🛠️ 工具介绍

OpenManus 提供了一套全面的工具集，使 AI 智能体能够执行各种任务。以下是所有可用工具的详细介绍：

### 核心工具

#### 1. **Bash 工具** (`bash`)
在终端中执行 bash 命令，支持完整的会话管理。
- **用途**: 运行 shell 命令、管理进程、与操作系统交互
- **功能特性**:
  - 支持长时间运行的命令，可后台执行
  - 交互式命令处理
  - 跨调用的会话持久化
  - 超时管理和进程控制
- **应用场景**: 系统管理、文件操作、软件包安装、进程管理

#### 2. **浏览器自动化工具** (`browser_use`)
强大的网页浏览器自动化工具，用于网页交互和内容提取。
- **用途**: 自动化网页浏览任务，从网站提取信息
- **功能特性**:
  - 导航: 访问URL、后退导航、页面刷新
  - 元素交互: 点击元素、输入文本、选择下拉菜单
  - 内容提取: 基于目标提取特定信息
  - 滚动操作: 按像素滚动或滚动到特定文本
  - 标签页管理: 切换、打开和关闭标签页
  - 网络搜索集成
- **应用场景**: 网页抓取、表单填写、自动化测试、内容研究

#### 3. **文件编辑工具** (`str_replace_editor`)
高级文件和目录操作工具，支持沙盒环境。
- **用途**: 查看、创建和编辑文件，具备精确的字符串替换功能
- **功能特性**:
  - 文件操作: 创建、查看、编辑文件和目录
  - 字符串替换: 精确的模式匹配和替换
  - 撤销功能: 回滚最近的编辑
  - 范围查看: 查看特定行范围
  - 沙盒支持: 在隔离环境中安全执行
- **应用场景**: 代码编辑、配置管理、文本处理

#### 4. **网络搜索工具** (`web_search`)
支持多搜索引擎的综合网络搜索工具。
- **用途**: 跨多个平台搜索实时信息
- **功能特性**:
  - 多引擎支持: Google、Bing、百度、DuckDuckGo
  - 自动回退: 主引擎失败时自动切换
  - 内容获取: 可选的完整内容提取
  - 结构化结果: 组织化的搜索结果和元数据
  - 可配置参数: 语言、国家、结果数量
- **应用场景**: 研究、事实核查、当前信息收集

#### 5. **Python 执行工具** (`python_execute`)
具有安全限制的 Python 代码执行工具。
- **用途**: 执行 Python 代码进行数据处理和分析
- **功能特性**:
  - 安全执行: 带有超时保护的沙盒环境
  - 输出捕获: 捕获打印语句和执行结果
  - 错误处理: 全面的异常捕获和报告
  - 多进程: 隔离的执行进程
- **应用场景**: 数据分析、计算、算法测试、自动化脚本

#### 6. **规划工具** (`planning`)
全面的项目规划和任务管理工具。
- **用途**: 创建、管理和跟踪复杂的项目计划和任务
- **功能特性**:
  - 计划创建: 定义具有结构化步骤的项目
  - 进度跟踪: 将步骤标记为已完成、进行中或阻塞
  - 活动计划管理: 设置和切换多个计划
  - 步骤注释: 为个别步骤添加备注和状态更新
  - 进度可视化: 显示完成统计和状态
- **应用场景**: 项目管理、任务组织、工作流规划

#### 7. **聊天完成工具** (`create_chat_completion`)
可自定义输出格式的结构化完成工具。
- **用途**: 生成具有特定类型格式的结构化响应
- **功能特性**:
  - 类型感知响应: 支持字符串、列表、字典、自定义对象
  - 模式验证: 自动参数模式生成
  - 灵活输出: 适应各种响应格式
  - Pydantic 集成: 支持复杂数据模型
- **应用场景**: 结构化数据生成、API 响应、格式化输出

#### 8. **终止工具** (`terminate`)
带有状态报告的清洁交互终止工具。
- **用途**: 以成功或失败状态正确结束交互
- **功能特性**:
  - 状态报告: 清晰的成功/失败指示
  - 清洁关闭: 正确的资源清理
  - 完成信号: 清晰的交互边界
- **应用场景**: 工作流完成、错误处理、会话管理

#### 9. **人机交互工具** (`ask_human`)
直接人类输入工具，用于澄清和协助。
- **用途**: 当自动化解决方案不足时请求人类输入
- **功能特性**:
  - 交互提示: 实时人类输入收集
  - 问题格式化: 清晰的询问展示
  - 响应捕获: 结构化的人类响应处理
- **应用场景**: 澄清请求、决策制定、手动干预

### 搜索引擎工具

网络搜索功能由多个专用搜索引擎提供支持：

#### **Google 搜索引擎**
- 高质量搜索结果，覆盖全面
- 高级搜索功能和丰富摘要

#### **Bing 搜索引擎**
- 微软的搜索平台，集成功能丰富
- 在技术和学术查询方面表现良好

#### **百度搜索引擎**
- 针对中文内容和区域结果优化
- 对中文网站和信息覆盖优秀

#### **DuckDuckGo 搜索引擎**
- 专注隐私的搜索，无追踪
- 无个性化偏差的清洁结果

### 图表可视化工具

由 VChart 和 VMind 提供支持的高级数据可视化功能：

#### **数据可视化工具** (`data_visualization`)
- **用途**: 从数据生成交互式图表和可视化
- **功能特性**:
  - 多种输出格式: PNG 图像和交互式 HTML
  - 图表类型: 支持各种图表类型（折线图、柱状图、饼图、散点图等）
  - 主题支持: 多种视觉主题和自定义选项
  - 语言支持: 中文和英文本地化
  - 数据处理: 自动数据准备和格式化

#### **Python 数据处理**
- **用途**: 为可视化准备和处理数据
- **功能特性**:
  - 数据清理和转换
  - 统计分析和汇总生成
  - CSV 文件处理和操作
  - 报告生成功能

#### **图表准备工具**
- **用途**: 配置和准备图表规格
- **功能特性**:
  - JSON 配置生成
  - 数据到图表的映射
  - 洞察注释支持
  - 可视化参数设置

### 文件操作工具

全面的文件系统交互功能：

#### **本地文件操作器**
- 用于本地环境的直接文件系统访问
- 具有适当错误处理的完整读/写功能
- 具有超时管理的命令执行

#### **沙盒文件操作器**
- 用于安全执行的隔离文件操作
- 远程沙盒环境集成
- 具有受限访问的安全文件操作

### 工具集合和管理

#### **工具集合** (`tool_collection`)
- 集中式工具注册和管理
- 动态工具加载和配置
- 工具元数据和参数验证

#### **MCP 集成** (`mcp`)
- 模型上下文协议支持工具通信
- 标准化工具接口和消息传递
- 远程工具执行功能

## 工具使用示例

### 基本文件操作
```python
# 创建新文件
await str_replace_editor.execute(
    command="create",
    path="/path/to/file.txt",
    file_text="Hello, World!"
)

# 编辑文件内容
await str_replace_editor.execute(
    command="str_replace",
    path="/path/to/file.txt",
    old_str="Hello",
    new_str="Hi"
)
```

### 网络搜索和浏览器自动化
```python
# 搜索信息
results = await web_search.execute(
    query="OpenAI GPT-4",
    num_results=5,
    fetch_content=True
)

# 导航到网站
await browser_use.execute(
    action="go_to_url",
    url="https://example.com"
)
```

### 数据分析和可视化
```python
# 执行 Python 代码
result = await python_execute.execute(
    code="import pandas as pd\ndf = pd.read_csv('data.csv')\nprint(df.head())"
)

# 创建可视化
await data_visualization.execute(
    json_path="/path/to/config.json",
    tool_type="visualization",
    output_type="html"
)
```

所有工具都设计为无缝协作，支持复杂的工作流和自动化任务。它们提供全面的错误处理、日志记录和配置选项，确保在各种环境中可靠运行。

## 交流群

加入我们的飞书交流群，与其他开发者分享经验！

<div align="center" style="display: flex; gap: 20px;">
    <img src="assets/community_group.jpg" alt="OpenManus 交流群" width="300" />
</div>

## Star 数量

[![Star History Chart](https://api.star-history.com/svg?repos=FoundationAgents/OpenManus&type=Date)](https://star-history.com/#FoundationAgents/OpenManus&Date)


## 赞助商
感谢[PPIO](https://ppinfra.com/user/register?invited_by=OCPKCN&utm_source=github_openmanus&utm_medium=github_readme&utm_campaign=link) 提供的算力支持。
> PPIO派欧云：一键调用高性价比的开源模型API和GPU容器

## 致谢

特别感谢 [anthropic-computer-use](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)
和 [browser-use](https://github.com/browser-use/browser-use) 为本项目提供的基础支持！

此外，我们感谢 [AAAJ](https://github.com/metauto-ai/agent-as-a-judge)，[MetaGPT](https://github.com/geekan/MetaGPT)，[OpenHands](https://github.com/All-Hands-AI/OpenHands) 和 [SWE-agent](https://github.com/SWE-agent/SWE-agent).

我们也感谢阶跃星辰 (stepfun) 提供的 Hugging Face 演示空间支持。

OpenManus 由 MetaGPT 社区的贡献者共同构建，感谢这个充满活力的智能体开发者社区！

## 引用
```bibtex
@misc{openmanus2025,
  author = {Xinbin Liang and Jinyu Xiang and Zhaoyang Yu and Jiayi Zhang and Sirui Hong and Sheng Fan and Xiao Tang},
  title = {OpenManus: An open-source framework for building general AI agents},
  year = {2025},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.15186407},
  url = {https://doi.org/10.5281/zenodo.15186407},
}
```
