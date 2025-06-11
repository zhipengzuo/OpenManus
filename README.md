<p align="center">
  <img src="assets/logo.jpg" width="200"/>
</p>

English | [中文](README_zh.md) | [한국어](README_ko.md) | [日本語](README_ja.md)

[![GitHub stars](https://img.shields.io/github/stars/FoundationAgents/OpenManus?style=social)](https://github.com/FoundationAgents/OpenManus/stargazers)
&ensp;
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) &ensp;
[![Discord Follow](https://dcbadge.vercel.app/api/server/DYn29wFk9z?style=flat)](https://discord.gg/DYn29wFk9z)
[![Demo](https://img.shields.io/badge/Demo-Hugging%20Face-yellow)](https://huggingface.co/spaces/lyh-917/OpenManusDemo)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15186407.svg)](https://doi.org/10.5281/zenodo.15186407)

# 👋 OpenManus

Manus is incredible, but OpenManus can achieve any idea without an *Invite Code* 🛫!

Our team members [@Xinbin Liang](https://github.com/mannaandpoem) and [@Jinyu Xiang](https://github.com/XiangJinyu) (core authors), along with [@Zhaoyang Yu](https://github.com/MoshiQAQ), [@Jiayi Zhang](https://github.com/didiforgithub), and [@Sirui Hong](https://github.com/stellaHSR), we are from [@MetaGPT](https://github.com/geekan/MetaGPT). The prototype is launched within 3 hours and we are keeping building!

It's a simple implementation, so we welcome any suggestions, contributions, and feedback!

Enjoy your own agent with OpenManus!

We're also excited to introduce [OpenManus-RL](https://github.com/OpenManus/OpenManus-RL), an open-source project dedicated to reinforcement learning (RL)- based (such as GRPO) tuning methods for LLM agents, developed collaboratively by researchers from UIUC and OpenManus.

## Project Demo

<video src="https://private-user-images.githubusercontent.com/61239030/420168772-6dcfd0d2-9142-45d9-b74e-d10aa75073c6.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDEzMTgwNTksIm5iZiI6MTc0MTMxNzc1OSwicGF0aCI6Ii82MTIzOTAzMC80MjAxNjg3NzItNmRjZmQwZDItOTE0Mi00NWQ5LWI3NGUtZDEwYWE3NTA3M2M2Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA3VDAzMjIzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdiZjFkNjlmYWNjMmEzOTliM2Y3M2VlYjgyNDRlZDJmOWE3NWZhZjE1MzhiZWY4YmQ3NjdkNTYwYTU5ZDA2MzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.UuHQCgWYkh0OQq9qsUWqGsUbhG3i9jcZDAMeHjLt5T4" data-canonical-src="https://private-user-images.githubusercontent.com/61239030/420168772-6dcfd0d2-9142-45d9-b74e-d10aa75073c6.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDEzMTgwNTksIm5iZiI6MTc0MTMxNzc1OSwicGF0aCI6Ii82MTIzOTAzMC80MjAxNjg3NzItNmRjZmQwZDItOTE0Mi00NWQ5LWI3NGUtZDEwYWE3NTA3M2M2Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA3VDAzMjIzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdiZjFkNjlmYWNjMmEzOTliM2Y3M2VlYjgyNDRlZDJmOWE3NWZhZjE1MzhiZWY4YmQ3NjdkNTYwYTU5ZDA2MzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.UuHQCgWYkh0OQq9qsUWqGsUbhG3i9jcZDAMeHjLt5T4" controls="controls" muted="muted" class="d-block rounded-bottom-2 border-top width-fit" style="max-height:640px; min-height: 200px"></video>

## Installation

We provide two installation methods. Method 2 (using uv) is recommended for faster installation and better dependency management.

### Method 1: Using conda

1. Create a new conda environment:

```bash
conda create -n open_manus python=3.12
conda activate open_manus
```

2. Clone the repository:

```bash
git clone https://github.com/FoundationAgents/OpenManus.git
cd OpenManus
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Method 2: Using uv (Recommended)

1. Install uv (A fast Python package installer and resolver):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone the repository:

```bash
git clone https://github.com/FoundationAgents/OpenManus.git
cd OpenManus
```

3. Create a new virtual environment and activate it:

```bash
uv venv --python 3.12
source .venv/bin/activate  # On Unix/macOS
# Or on Windows:
# .venv\Scripts\activate
```

4. Install dependencies:

```bash
uv pip install -r requirements.txt
```

### Browser Automation Tool (Optional)
```bash
playwright install
```

## Configuration

OpenManus requires configuration for the LLM APIs it uses. Follow these steps to set up your configuration:

1. Create a `config.toml` file in the `config` directory (you can copy from the example):

```bash
cp config/config.example.toml config/config.toml
```

2. Edit `config/config.toml` to add your API keys and customize settings:

```toml
# Global LLM configuration
[llm]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."  # Replace with your actual API key
max_tokens = 4096
temperature = 0.0

# Optional configuration for specific LLM models
[llm.vision]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."  # Replace with your actual API key
```

## Quick Start

One line for run OpenManus:

```bash
python main.py
```

Then input your idea via terminal!

For MCP tool version, you can run:
```bash
python run_mcp.py
```

For unstable multi-agent version, you also can run:

```bash
python run_flow.py
```

## How to contribute

We welcome any friendly suggestions and helpful contributions! Just create issues or submit pull requests.

Or contact @mannaandpoem via 📧email: mannaandpoem@gmail.com

**Note**: Before submitting a pull request, please use the pre-commit tool to check your changes. Run `pre-commit run --all-files` to execute the checks.

## 🛠️ Tools Overview

OpenManus provides a comprehensive set of tools that enable AI agents to perform various tasks. Here's a detailed overview of all available tools:

### Core Tools

#### 1. **Bash Tool** (`bash`)
Execute bash commands in the terminal with full session support.
- **Purpose**: Run shell commands, manage processes, and interact with the operating system
- **Features**:
  - Long-running command support with background execution
  - Interactive command handling
  - Session persistence across calls
  - Timeout management and process control
- **Use Cases**: System administration, file operations, package installation, process management

#### 2. **Browser Automation Tool** (`browser_use`)
A powerful browser automation tool for web interaction and content extraction.
- **Purpose**: Automate web browsing tasks and extract information from websites
- **Features**:
  - Navigation: Go to URLs, back navigation, page refresh
  - Element interaction: Click elements, input text, select dropdowns
  - Content extraction: Extract specific information based on goals
  - Scrolling: Scroll by pixels or to specific text
  - Tab management: Switch, open, and close tabs
  - Web search integration
- **Use Cases**: Web scraping, form filling, automated testing, content research

#### 3. **File Editor Tool** (`str_replace_editor`)
Advanced file and directory manipulation tool with sandbox support.
- **Purpose**: View, create, and edit files with precise string replacement capabilities
- **Features**:
  - File operations: Create, view, edit files and directories
  - String replacement: Exact pattern matching and replacement
  - Undo functionality: Revert recent edits
  - Range viewing: View specific line ranges
  - Sandbox support: Safe execution in isolated environments
- **Use Cases**: Code editing, configuration management, text processing

#### 4. **Web Search Tool** (`web_search`)
Comprehensive web search tool with multiple search engine support.
- **Purpose**: Search the web for real-time information across multiple platforms
- **Features**:
  - Multi-engine support: Google, Bing, Baidu, DuckDuckGo
  - Automatic fallback: Switch engines if primary fails
  - Content fetching: Optional full content extraction from results
  - Structured results: Organized search results with metadata
  - Configurable parameters: Language, country, result count
- **Use Cases**: Research, fact-checking, current information gathering

#### 5. **Python Execution Tool** (`python_execute`)
Safe Python code execution with timeout and safety restrictions.
- **Purpose**: Execute Python code for data processing and analysis
- **Features**:
  - Secure execution: Sandboxed environment with timeout protection
  - Output capture: Capture print statements and execution results
  - Error handling: Comprehensive exception catching and reporting
  - Multiprocessing: Isolated execution processes
- **Use Cases**: Data analysis, calculations, algorithm testing, automation scripts

#### 6. **Planning Tool** (`planning`)
Comprehensive project planning and task management tool.
- **Purpose**: Create, manage, and track complex project plans and tasks
- **Features**:
  - Plan creation: Define projects with structured steps
  - Progress tracking: Mark steps as completed, in-progress, or blocked
  - Active plan management: Set and switch between multiple plans
  - Step annotations: Add notes and status updates to individual steps
  - Progress visualization: Display completion statistics and status
- **Use Cases**: Project management, task organization, workflow planning

#### 7. **Chat Completion Tool** (`create_chat_completion`)
Structured completion tool with customizable output formatting.
- **Purpose**: Generate structured responses with specific type formatting
- **Features**:
  - Type-aware responses: Support for strings, lists, dictionaries, custom objects
  - Schema validation: Automatic parameter schema generation
  - Flexible output: Adaptable to various response formats
  - Pydantic integration: Support for complex data models
- **Use Cases**: Structured data generation, API responses, formatted outputs

#### 8. **Termination Tool** (`terminate`)
Clean interaction termination with status reporting.
- **Purpose**: Properly end interactions with success or failure status
- **Features**:
  - Status reporting: Clear success/failure indication
  - Clean shutdown: Proper resource cleanup
  - Completion signals: Clear interaction boundaries
- **Use Cases**: Workflow completion, error handling, session management

#### 9. **Human Interaction Tool** (`ask_human`)
Direct human input tool for clarification and assistance.
- **Purpose**: Request human input when automated solutions are insufficient
- **Features**:
  - Interactive prompts: Real-time human input collection
  - Question formatting: Clear inquiry presentation
  - Response capture: Structured human response handling
- **Use Cases**: Clarification requests, decision making, manual intervention

### Search Engine Tools

The web search functionality is powered by multiple specialized search engines:

#### **Google Search Engine**
- High-quality search results with comprehensive coverage
- Advanced search capabilities and rich snippets

#### **Bing Search Engine**
- Microsoft's search platform with integrated features
- Good performance for technical and academic queries

#### **Baidu Search Engine**
- Optimized for Chinese language content and regional results
- Excellent coverage of Chinese websites and information

#### **DuckDuckGo Search Engine**
- Privacy-focused search without tracking
- Clean results without personalization bias

### Chart Visualization Tools

Advanced data visualization capabilities powered by VChart and VMind:

#### **Data Visualization Tool** (`data_visualization`)
- **Purpose**: Generate interactive charts and visualizations from data
- **Features**:
  - Multiple output formats: PNG images and interactive HTML
  - Chart types: Support for various chart types (line, bar, pie, scatter, etc.)
  - Theme support: Multiple visual themes and customization options
  - Language support: Chinese and English localization
  - Data processing: Automatic data preparation and formatting

#### **Python Data Processing**
- **Purpose**: Prepare and process data for visualization
- **Features**:
  - Data cleaning and transformation
  - Statistical analysis and summary generation
  - CSV file processing and manipulation
  - Report generation capabilities

#### **Chart Preparation Tool**
- **Purpose**: Configure and prepare chart specifications
- **Features**:
  - JSON configuration generation
  - Data-to-chart mapping
  - Insight annotation support
  - Visualization parameter setup

### File Operation Tools

Comprehensive file system interaction capabilities:

#### **Local File Operator**
- Direct filesystem access for local environments
- Full read/write capabilities with proper error handling
- Command execution with timeout management

#### **Sandbox File Operator**
- Isolated file operations for secure execution
- Remote sandbox environment integration
- Safe file manipulation with restricted access

### Tool Collection and Management

#### **Tool Collection** (`tool_collection`)
- Centralized tool registry and management
- Dynamic tool loading and configuration
- Tool metadata and parameter validation

#### **MCP Integration** (`mcp`)
- Model Context Protocol support for tool communication
- Standardized tool interface and messaging
- Remote tool execution capabilities

## Tool Usage Examples

### Basic File Operations
```python
# Create a new file
await str_replace_editor.execute(
    command="create",
    path="/path/to/file.txt",
    file_text="Hello, World!"
)

# Edit file content
await str_replace_editor.execute(
    command="str_replace",
    path="/path/to/file.txt",
    old_str="Hello",
    new_str="Hi"
)
```

### Web Search and Browser Automation
```python
# Search for information
results = await web_search.execute(
    query="OpenAI GPT-4",
    num_results=5,
    fetch_content=True
)

# Navigate to a website
await browser_use.execute(
    action="go_to_url",
    url="https://example.com"
)
```

### Data Analysis and Visualization
```python
# Execute Python code
result = await python_execute.execute(
    code="import pandas as pd\ndf = pd.read_csv('data.csv')\nprint(df.head())"
)

# Create visualization
await data_visualization.execute(
    json_path="/path/to/config.json",
    tool_type="visualization",
    output_type="html"
)
```

All tools are designed to work together seamlessly, enabling complex workflows and automation tasks. They provide comprehensive error handling, logging, and configuration options to ensure reliable operation in various environments.

## Community Group
Join our networking group on Feishu and share your experience with other developers!

<div align="center" style="display: flex; gap: 20px;">
    <img src="assets/community_group.jpg" alt="OpenManus 交流群" width="300" />
</div>

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=FoundationAgents/OpenManus&type=Date)](https://star-history.com/#FoundationAgents/OpenManus&Date)

## Sponsors
Thanks to [PPIO](https://ppinfra.com/user/register?invited_by=OCPKCN&utm_source=github_openmanus&utm_medium=github_readme&utm_campaign=link) for computing source support.
> PPIO: The most affordable and easily-integrated MaaS and GPU cloud solution.


## Acknowledgement

Thanks to [anthropic-computer-use](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)
and [browser-use](https://github.com/browser-use/browser-use) for providing basic support for this project!

Additionally, we are grateful to [AAAJ](https://github.com/metauto-ai/agent-as-a-judge), [MetaGPT](https://github.com/geekan/MetaGPT), [OpenHands](https://github.com/All-Hands-AI/OpenHands) and [SWE-agent](https://github.com/SWE-agent/SWE-agent).

We also thank stepfun(阶跃星辰) for supporting our Hugging Face demo space.

OpenManus is built by contributors from MetaGPT. Huge thanks to this agent community!

## Cite
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
