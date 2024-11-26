from crewai import Crew,Process,LLM
from agents import blog_researcher,blog_writer
from tasks import research_task,writer_task
from langchain_groq import ChatGroq
import os 

os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] = 'llama3-8b-8192'
os.environ["OPENAI_API_KEY"] = os.environ.get("GROQ_API_KEY")


# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research_task, writer_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True,
   
)

## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':"AI VS ML VS DL vs Data Science"})
print(result)