from google.adk.agents.llm_agent import Agent
from google.adk.tools.google_search_tool import google_search
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that can search the web.',
    instruction=('Answer user questions accurately.'
    'Use google search when you need current information.'
    'or need to verify facts'
    ),
    tools=[google_search]
)
