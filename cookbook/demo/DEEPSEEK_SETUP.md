# DeepSeek API Setup Guide

## Overview

All agents in this demo have been configured to use DeepSeek models instead of Claude. This allows you to run the demo in regions where Claude API access is restricted.

## Prerequisites

You need a DeepSeek API key to run this demo. Get one at: https://platform.deepseek.com/

## Setup Instructions

### 1. Set the Environment Variable

Add your DeepSeek API key to your environment:

```bash
export DEEPSEEK_API_KEY="your-api-key-here"
```

To make it persistent, add it to your shell configuration file:

**For bash:**
```bash
echo 'export DEEPSEEK_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

**For zsh:**
```bash
echo 'export DEEPSEEK_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### 2. Verify Configuration

Check that the environment variable is set:

```bash
echo $DEEPSEEK_API_KEY
```

### 3. Run the Demo

```bash
python cookbook/demo/run.py
```

## Modified Files

The following agents have been updated to use DeepSeek models:

- ✅ `agno_knowledge_agent.py` - Uses `deepseek-chat`
- ✅ `agno_mcp_agent.py` - Uses `deepseek-chat`
- ✅ `youtube_agent.py` - Uses `deepseek-chat`
- ✅ `memory_agent.py` - Uses `deepseek-chat`
- ✅ `finance_agent.py` - Uses `deepseek-chat`
- ✅ `finance_team.py` - Uses `deepseek-chat`
- ✅ `research_agent.py` - Uses `deepseek-chat`
- ✅ `competitive_brief.py` - Uses `deepseek-chat`
- ✅ `simple_agent.py` - Uses `deepseek-chat`

## Model Information

**Model Used:** `deepseek-chat`

This is DeepSeek's general-purpose chat model that provides:
- Strong reasoning capabilities
- Multilingual support (including Chinese)
- Cost-effective pricing
- Good performance for agent tasks

## Alternative: DeepSeek Reasoner

If you want to use the DeepSeek Reasoner model (`deepseek-reasoner`) for specific agents, you can modify the model initialization:

```python
from agno.models.deepseek import DeepSeek

agent = Agent(
    model=DeepSeek(id="deepseek-reasoner"),  # Use reasoner model
    # ... other parameters
)
```

Note: The reasoner model is optimized for complex reasoning tasks but may have different pricing and performance characteristics.

## Troubleshooting

### Error: "DEEPSEEK_API_KEY not set"

Make sure you've exported the environment variable in the same shell session where you're running the demo.

### Error: "API key invalid"

Verify your API key at https://platform.deepseek.com/

### Other API Errors

Check the DeepSeek API status and documentation at: https://platform.deepseek.com/docs

## Reverting to Claude

If you want to switch back to Claude models, you can:

1. Set your `ANTHROPIC_API_KEY` environment variable
2. Replace imports in the agent files:
   ```python
   from agno.models.deepseek import DeepSeek
   # Change to:
   from agno.models.anthropic import Claude
   ```
3. Update the model initialization:
   ```python
   model=DeepSeek(id="deepseek-chat")
   # Change to:
   model=Claude(id="claude-sonnet-4-5")
   ```

