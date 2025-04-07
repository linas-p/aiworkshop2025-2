from praisonaiagents import Agent, MCP
import os

from dotenv import load_dotenv
load_dotenv()

search_agent = Agent(
    instructions="""You help book apartments on Airbnb.""",
    llm="gemini/gemini-2.0-flash-exp",
    tools=MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")
)

search_agent.start("Atostogų pasiūlymas AirBnB. 04/08 - 04/10 dviem žmonėms Gran Kanarijoje")