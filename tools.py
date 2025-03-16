from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for the provided information",
)

wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=3)
wiki_query_run = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)
wiki_tool = Tool(
    name="wikipedia",
    func=wiki_query_run.run,
    description="Search Wikipedia for information on a specific topic"
)