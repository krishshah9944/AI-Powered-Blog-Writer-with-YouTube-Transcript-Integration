from crewai import Agent,LLM
from tools import yt_tool
from langchain_groq import ChatGroq


llm=ChatGroq(
    model="groq/llama3-8b-8192",
    temperature=0.7,
    # base_url="https://api.groq.com/openai/v1",
    api_key="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"
)




## Create a senior blog content researcher

blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verbose=True,
    memory=True,
    backstory=(
       "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" 
    ),
    tools=[yt_tool],
    allow_delegation=True,
    llm=llm
)

## creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False,
    llm=llm
)
