import asyncio
from ddgs import DDGS
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

from dotenv import load_dotenv
load_dotenv()

def search_weather_news(city:str) -> str:
    """The weather news searches the latest information about the weather from the internet"""
    return str(DDGS().news(query=f"{city} weather today", max_results=5))

city=input("Which city?")
model_client=OpenAIChatCompletionClient(model="gpt-4o-mini")

agent = AssistantAgent(
    name="weather_news",
    model_client=model_client,
    tools=[search_weather_news],
    system_message="Filter the current weather for the day",
    reflect_on_tool_use=True
)

async def main():
    await Console(agent.run_stream(task =f"find out the current weather from the {city} today. Provide accurate informaation related to rainfall, snow etc."))
    await model_client.close()

asyncio. run(main())