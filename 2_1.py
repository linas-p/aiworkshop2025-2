from smolagents import ToolCallingAgent, LiteLLMModel, load_tool, tool
import os

from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

model = LiteLLMModel(model_id="gemini/gemini-2.0-flash-exp",
                     api_key=GEMINI_API_KEY)

@tool
def get_weather(location: str) -> str:
    """
    Gauti orų informaciją duotam miestui.
    Args:
        location: miestas
    """
    return f"Oro temperatūra {location} yra -7°C :) ."

@tool
def get_opinion() -> str:
    """
    Atsakyti Žalgirio ir Lietuvos Ryto palyginimo klausimais
    """
    return f"Žalgiris yra geresnė komanda."

agent = ToolCallingAgent(model=model, tools=[get_weather, get_opinion])

answer = agent.run("Kas geriau Žalgeris ar Lietuvos Rytas?")
#answer = agent.run("Koks oras ir temperatūra Vilniuje?")
print(answer)