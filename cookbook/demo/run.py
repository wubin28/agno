"""Minimal demo of the AgentOS."""

import getpass
import os
from pathlib import Path
from textwrap import dedent

from agno.os import AgentOS

# ============================================================================
# Check and prompt for API keys
# ============================================================================
def check_api_keys():
    """Check for required API keys and prompt if missing."""
    print("=" * 60)
    print("AgentOS API Key Configuration")
    print("=" * 60)
    
    # Check DeepSeek API Key
    if not os.getenv("DEEPSEEK_API_KEY"):
        print("\n⚠️  DEEPSEEK_API_KEY not found in environment")
        print("Please enter your DeepSeek API key:")
        print("(Get one at: https://platform.deepseek.com/)")
        try:
            api_key = getpass.getpass("DeepSeek API Key (hidden): ")
            if api_key.strip():
                os.environ["DEEPSEEK_API_KEY"] = api_key.strip()
                print("✓ DeepSeek API key set for this session")
            else:
                print("❌ Error: API key cannot be empty")
                exit(1)
        except KeyboardInterrupt:
            print("\n\n❌ Setup cancelled by user")
            exit(1)
    else:
        print("\n✓ DEEPSEEK_API_KEY found")
    
    # Check OpenAI API Key (optional, used for embeddings)
    if not os.getenv("OPENAI_API_KEY"):
        print("\n⚠️  OPENAI_API_KEY not found (optional)")
        print("The knowledge base uses OpenAI embeddings.")
        response = input("Would you like to enter it now? (y/n): ").lower()
        if response == 'y':
            try:
                openai_key = getpass.getpass("OpenAI API Key (hidden): ")
                if openai_key.strip():
                    os.environ["OPENAI_API_KEY"] = openai_key.strip()
                    print("✓ OpenAI API key set for this session")
            except KeyboardInterrupt:
                print("\nSkipping OpenAI API key...")
        else:
            print("ℹ️  Skipping OpenAI API key (some features may not work)")
    else:
        print("✓ OPENAI_API_KEY found")
    
    print("\n" + "=" * 60)
    print("Starting AgentOS...")
    print("=" * 60 + "\n")

# Run the check before importing agents (which may use the API keys)
check_api_keys()
from agno_knowledge_agent import agno_knowledge_agent
from agno_mcp_agent import agno_mcp_agent
from competitive_brief import competitive_brief
from finance_agent import finance_agent
from finance_team import finance_team
from memory_agent import memory_manager
from research_agent import research_agent
from youtube_agent import youtube_agent

# ============================================================================
# AgentOS Config
# ============================================================================
config_path = str(Path(__file__).parent.joinpath("config.yaml"))

# ============================================================================
# Create AgentOS
# ============================================================================
agent_os = AgentOS(
    description=dedent("""\
        Demo AgentOS — a lightweight runtime wiring together demo agents and teams.
        Includes knowledge lookup (Agno docs), MCP-powered assistance, YouTube QA,
        market analysis, memory management, and web research — all in one process.
        """),
    agents=[
        agno_knowledge_agent,
        agno_mcp_agent,
        youtube_agent,
        finance_agent,
        memory_manager,
        research_agent,
    ],
    teams=[
        finance_team,
    ],
    workflows=[
        competitive_brief,
    ],
    config=config_path,
)
app = agent_os.get_app()

# ============================================================================
# Run AgentOS
# ============================================================================
if __name__ == "__main__":
    # Serves a FastAPI app exposed by AgentOS. Use reload=True for local dev.
    agent_os.serve(app="run:app", reload=True)
