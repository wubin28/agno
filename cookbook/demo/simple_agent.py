from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.deepseek import DeepSeek
from agno.os import AgentOS
from agno.tools.duckduckgo import DuckDuckGoTools

# ************* Create Agent *************
simple_agent = Agent(
    name="DeepSeek Agent",
    model=DeepSeek(id="deepseek-chat"),  # Use DeepSeek class instead of OpenAIChat
    db=SqliteDb(db_file="tmp/simple_agent.db"),
    tools=[DuckDuckGoTools()],  # Add search functionality
    add_history_to_context=True,
    num_history_runs=3,
    markdown=True,
    instructions="You are a helpful AI assistant with web search access. Use search when you need current information.",
)

# ************* Create AgentOS *************
agent_os = AgentOS(agents=[simple_agent])
app = agent_os.get_app()

# ************* Run AgentOS *************
if __name__ == "__main__":
    agent_os.serve(app="simple_agent:app", reload=True)
