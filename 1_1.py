from smolagents import ToolCallingAgent, LiteLLMModel
import os

from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

model = LiteLLMModel(model_id="gemini/gemini-2.0-flash-exp",
                     api_key=GEMINI_API_KEY)

agent = ToolCallingAgent(model=model, tools=[])

#answer = agent.run("Kas geriau Žalgeris ar Lietuvos Rytas?")
answer = agent.run("Koks oras ir temperatūra Vilniuje?")
print(answer)