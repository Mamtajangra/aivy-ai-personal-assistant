from langchain.agents import initialize_agent, Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

'''
pycache:
Tumne ek recipe likhi: “Make tea” 🫖 → ye tumhara .py file
Pehli baar tumne try kiya → tumhe tea banana pada step by step → slow
Tumne ek shortcut note bana diya: “Boil water + add tea leaves” → ye .pyc file
Agli baar, tum direct shortcut se tea bana loge → fast
pycache folder = ye shortcut notes store karta hai.'''
## call functions here
from tools.weather_tool import get_weather
from tools.news_tool import get_latest_news


# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini LLM with a valid available model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.7,google_api_key=API_KEY)

# Define tools
tools = [
    Tool("WeatherTool", get_weather, "Get current weather for a city"),
    Tool("NewsTool", get_latest_news, "Get latest news headlines")]

# Initialize agent
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description", verbose=True)

# Chat loop using invoke() 
while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break
    response = agent.invoke({"input": query})
    print("AI:", response["output"])
