from google.adk.agents.llm_agent import Agent
from google.adk.tools.langchain_tool import LangchainTool
from langchain_tavily import TavilySearch

#Langchain tavily tool
tavily_search = TavilySearch(
    max_results=5,
    topics='general',
)

#Wrap it so adk can use it
tavily_tool = LangchainTool(tool=tavily_search)

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that can search the web.',
    instruction=('Answer user questions accurately.' 
    'Use tavily search tool when you need current information.' 
    'or need to verify facts.'
    ),
    tools=[tavily_tool],
)
