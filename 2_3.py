from smolagents import CodeAgent, LiteLLMModel, PythonInterpreterTool
import os

from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

model = LiteLLMModel(model_id="gemini/gemini-2.0-flash-exp",
                     api_key=GEMINI_API_KEY)

python_tool = PythonInterpreterTool()
agent = CodeAgent(model=model, tools=[python_tool])


answer = agent.run("Kiek bus 5 procentai nuo 15*24")
print(answer)