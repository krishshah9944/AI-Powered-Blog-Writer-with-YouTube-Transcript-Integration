# AI-Powered Blog Writer with YouTube Transcript Integration

## 📝 Overview
This project is an AI-powered blog writer that extracts transcripts from YouTube videos and generates well-structured blog content. It utilizes Crew AI to orchestrate agents for research and content generation, powered by Groq's Llama 3 model.

## 🚀 Features
- **YouTube Transcript Extraction**: Fetches video transcripts automatically.
- **AI-Powered Blog Generation**: Uses Crew AI agents to generate high-quality blog posts.
- **Content Summarization**: Condenses long transcripts into concise blog summaries.
- **Crew AI Integration**: Uses agents for efficient research and writing tasks.
- **Groq Llama 3 Model**: Utilizes `llama3-8b-8192` for advanced text generation.
- **Simple Execution**: Just specify the YouTube channel name in tools and the topic in Crew AI, then run the script.

## 🛠️ Tech Stack
- **Orchestration**: Crew AI
- **LLM Provider**: Groq (Llama 3 - 8B)
- **Backend**: Python 


## 📌 Setup Instructions
### Prerequisites
- Python 3.8+
- Pip
- Groq API Key (Get yours at [Groq Console](https://console.groq.com/keys))

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/krishshah9944/AI-Powered-Blog-Writer-with-YouTube-Transcript-Integration.git
   cd AI-Powered-Blog-Writer-with-YouTube-Transcript-Integration
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   ```bash
   export GROQ_API_KEY=your_api_key_here
   ```
5. Specify the YouTube channel name in tools and the topic in Crew AI.
6. Run the application:
   ```bash
   python crew.py
   ```

## 📂 Project Structure
```
ai-blog-writer/
│-- crew.py                 # Main execution script
│-- agents.py               # Crew AI agents setup
│-- tasks.py                # Crew AI tasks setup
│-- tools.py                # YouTube channel tools setup
│-- requirements.txt        # Dependencies
│-- .env                    # API Key (not included in repo)
│-- README.md               # Documentation
```

## 🎯 Usage Guide
1. **Specify YouTube Channel**: Set the desired channel in `tools.py`.
2. **Define Topic**: Input the topic in Crew AI.
3. **Run the Script**: Execute `python crew.py` to generate the blog post.

## 🛠️ Issues & Support
For any issues, feel free to reach out via:
- **LinkedIn**: [Krish Shah](https://www.linkedin.com/in/krishshah9944/)
- **Email**: krishshah9944@gmail.com

