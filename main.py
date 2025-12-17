import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.tools import tool
from langchain.agents import create_agent
from tavily import TavilyClient
from langchain_tavily import TavilySearch
load_dotenv()

#tavily= TavilyClient()

# @tool
# def get_current_weather(city:str) -> str:
#     """Tool that gets the current weather for a given city
#     
#     Args:
#         city: The city to get the weather for
#     Returns:
#         The current weather for the city
#     """
#     print(f"Getting the weather for {city}")
#     return tavily.search(query=f"weather in {city}")



tools= [TavilySearch()]
model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.0)
#model = ChatOllama(model="gemma3:1b", temperature=0.0)
agent=create_agent(model, tools)

def main():
    print("Hello from langchain-tivoli!")
    
    result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo?")})
    print(result)
    
  
    
      
if __name__ == "__main__":
    main()
