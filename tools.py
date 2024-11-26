from crewai_tools import YoutubeChannelSearchTool

# Initialize the tool with a specific Youtube channel handle to target your search
# yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='')

# yt_tool = YoutubeChannelSearchTool( youtube_channel_handle='' ,
#     config=dict(
#         llm=dict(
#             provider="groq",  # Use "custom" or any identifier for GROQ
#             config=dict(
#                 model="llama3-70b-8192",
#                 base_url="https://api.groq.com/openai/v1",  # GROQ API URL
#                 api_key="",
#                 temperature=0.7,  # Add other parameters as needed
#             ),
#         ),
#         embedder=dict(
#             provider="google",  # Update embedder to use GROQ
#             config=dict(
#                 model="models/text-embedding-004",  # Replace with a GROQ-supported embedding model if needed
#                 task_type="retrieval_document",
#                 # base_url="https://generativelanguage.googleapis.com",  # GROQ API URL
#                 # api_key="",
#             ),
#         ),
#     ) 
 
# )


import google.generativeai as genai

genai.configure(api_key="")

# Initialize the tool with corrected arguments
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle="@IBMTechnology",  # This must be a string
    config=dict(
        llm=dict(
            provider="groq",  # Use "groq" as the LLM provider
            config=dict(
                model="llama3-70b-8192",  # GROQ-supported model
                base_url="https://api.groq.com/openai/v1",  # GROQ API base URL
                api_key="",
                temperature=0.7,  # Adjust as necessary
            ),
        ),
        embedder=dict(
            provider="google",  # Using Google as the embedder
            config=dict(
                model="models/text-embedding-004",  # Google-supported embedding model
                task_type="retrieval_document",  # Task-specific configuration
            ),
        ),
    ),
)

# Call the tool
result = yt_tool.run(search_query="AI VS ML VS DL vs Data Science")
print(result)
