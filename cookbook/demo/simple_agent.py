from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.anthropic import Claude
from agno.os import AgentOS

# ************* Create Agent *************
simple_agent = Agent(
    name="Simple Agent",
    model=Claude(id="claude-sonnet-4-5"),
    db=SqliteDb(db_file="tmp/simple_agent.db"),
    add_history_to_context=True,
    add_datetime_to_context=True,
    enable_agentic_memory=True,
    num_history_runs=3,
    markdown=True,
)

# ************* Create AgentOS *************
agent_os = AgentOS(agents=[simple_agent], telemetry=False)
app = agent_os.get_app()

# ************* Run AgentOS *************
if __name__ == "__main__":
    agent_os.serve(app="simple_agent:app", reload=True)
