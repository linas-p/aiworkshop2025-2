from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel
import os

from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

model = LiteLLMModel(model_id="gemini/gemini-2.0-flash-exp",
                     api_key=GEMINI_API_KEY)


web_agent = CodeAgent(
    model=model,          
    tools=[DuckDuckGoSearchTool()],
    name="web_agent",            
    description="Agent that searches the web for information",
    max_steps=3,                 
    verbosity_level=2            
)

manager_agent = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[web_agent],
    name="manager_agent",
    description="Agent that delegates tasks to the web agent and processes results",
    max_steps=5,
    verbosity_level=2
)


query = """
1) Find the top DuckDuckGo web search results for 'Lithuanian films'.
2) Summarize them in a short paragraph.
3) Count how many words are in that paragraph.
"""

final_answer = manager_agent.run(query)
print("Final Answer:\n", final_answer)