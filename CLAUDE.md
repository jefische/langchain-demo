# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LangChain learning and experimentation repository focused on building LLM-powered applications using the Anthropic Claude API. The project contains both Python scripts and Jupyter notebooks for exploring LangChain capabilities.

## Environment Setup

### Virtual Environment
- Virtual environment: `langChainEnv`
- Activate: `langChainEnv\Scripts\activate` (Windows)

### Dependencies
Install all dependencies:
```bash
pip install -r requirements.txt
```

Key dependencies:
- `langchain` - Core LangChain framework
- `langchain-anthropic` - Anthropic/Claude integration
- `langchain-community` - Community integrations (e.g., YoutubeLoader)
- `anthropic` - Direct Anthropic API client
- `python-dotenv` - Environment variable management
- `jupyter` - Notebook environment

### API Keys
API keys are loaded from `.env` file using `python-dotenv`:
- `ANTHROPIC_API_KEY` - Required for all Claude API calls

**Important**: All code that uses the Anthropic API must load environment variables:
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
```

## Running Code

### Jupyter Notebooks
```bash
jupyter notebook
# or
jupyter lab
```

The main learning notebook is [tutorial.ipynb](tutorial.ipynb).

### Python Scripts
```bash
python tutorial.py
```

## Important LangChain Import Changes

**Critical**: LangChain has reorganized its module structure. Use the correct imports:

**Correct**:
```python
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel
from langchain_anthropic import ChatAnthropic
from langchain_community.document_loaders import YoutubeLoader
```

**Incorrect** (deprecated):
```python
from langchain import PromptTemplate  # Will fail
from langchain.prompts import PromptTemplate  # Will fail
```

## Code Architecture

### LLM Clients
Two approaches are used in this codebase:

1. **Direct Anthropic SDK** ([tutorial.py](tutorial.py)):
   - Uses `anthropic.Anthropic()` client
   - Direct API calls with `client.messages.create()`
   - Simpler for basic use cases

2. **LangChain Integration** ([tutorial.ipynb](tutorial.ipynb)):
   - Uses `ChatAnthropic` from `langchain_anthropic`
   - Supports chain composition with LCEL (LangChain Expression Language)
   - Better for complex workflows

### Chain Patterns

The notebook demonstrates several LangChain runnable patterns:

- **RunnableSequence**: Sequential chains using `|` operator (e.g., `prompt | llm | parser`)
- **RunnableLambda**: Custom Python functions in chains
- **RunnablePassthrough**: Pass data through unchanged or add keys
- **RunnableParallel**: Execute multiple runnables concurrently

### Message Extraction

When a chain ends with an LLM, it returns an `AIMessage` object:
```python
result = chain.invoke({...})  # Returns AIMessage
text = result.content  # Extract the text content
```

Or chain directly:
```python
text = chain.invoke({...}).content  # Get content immediately
```

## Windows-Specific Considerations

### Long Path Support
This project path may trigger Windows 260-character path limit errors when installing packages like Jupyter. Solutions:

1. Enable Windows Long Path support in Registry (`LongPathsEnabled`)
2. Move project to shorter path (e.g., `C:\dev\langchain-demo`)

### Git Configuration
If long paths are enabled:
```bash
git config --system core.longpaths true
```

## Common Patterns

### Claude Model Names
```python
llm_opus = ChatAnthropic(model='claude-opus-4-5')
llm_sonnet = ChatAnthropic(model='claude-sonnet-4-5')
llm_haiku = ChatAnthropic(model='claude-haiku-4-5')
```

### Basic Chain Construction
```python
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic}"
)
llm = ChatAnthropic(model='claude-sonnet-4-5')
chain = prompt | llm

response = chain.invoke({"topic": "LangChain"}).content
```

### System + User Messages
```python
from langchain_core.messages import SystemMessage, HumanMessage

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="What is LangChain?")
]
response = llm.invoke(messages)
```
