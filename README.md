# Agentic AI Project

A comprehensive Agentic AI System that integrates the powerful llama3-70b-8192 model (Groq) with smart single-tool selection (Tavily search OR Wikipedia) to create an intelligent conversational agent. The AI automatically decides which single tool to use or uses no tools at all based on the user's query. The project demonstrates a complete CI/CD pipeline from development to production deployment on AWS.

## 🏗️ Project Structure

```
multi_aai_jk_fg_sq/
├── app.py                # Primary application entry point
├── app/
│   ├── backend/          # FastAPI backend + AI agent logic
│   │   ├── api.py        # RESTful API endpoints
│   │   └── ai_agent.py   # Agentic AI processing engine (llama3-70b-8192)
│   ├── frontend/         # Streamlit frontend
│   │   └── ui.py         # Web-based user interface
│   ├── config/           # Settings & configuration
│   │   └── settings.py   # Environment variables & app config
│   ├── common/           # Shared utilities
│   │   ├── logger.py     # Logging configuration
│   │   └── custom_exception.py # Custom exception handling
│   └── main.py           # Internal application logic
├── custom_jenkins/       # Jenkins Docker setup
├── Dockerfile            # Application container
├── Jenkinsfile           # CI/CD pipeline
└── requirements.txt      # Python dependencies
```

## 🚀 Features

- **Agentic AI Model**: Uses the powerful llama3-70b-8192 model by default
- **Smart Tool Selection**: Automatically chooses ONE tool (Tavily search OR Wikipedia) or uses no tools based on user queries
- **Tool Usage Tracking**: Shows which tools were used in each response
- **Custom System Prompts**: Define AI agent behavior
- **Error Handling**: Comprehensive logging and exception handling
- **Scalable Architecture**: Microservices with containerization
- **Automated Deployment**: Full CI/CD pipeline to AWS

## 🛠️ Technology Stack

### AI/ML
- **LangChain**: Framework for LLM applications
- **LangGraph**: Multi-agent orchestration
- **Groq**: High-performance LLM inference
- **Tavily**: Web search API
- **Wikipedia**: Comprehensive knowledge base

### Web Framework
- **FastAPI**: High-performance API framework
- **Streamlit**: Data science web app framework
- **Pydantic**: Data validation

### DevOps
- **Jenkins**: CI/CD automation
- **SonarQube**: Code quality analysis
- **Docker**: Containerization
- **AWS ECS**: Container orchestration

## 📦 Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -e .`
5. Set up environment variables in `.env` file:
   ```
   GROQ_API_KEY=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```
   See `sample_env.txt` for a template of required environment variables.
6. Run the application: `python app.py`

## 🎯 Use Cases

- **Agentic AI Assistant**: Conversational AI with web search
- **Research Tool**: AI-powered information gathering
- **Learning Platform**: Interactive AI tutoring
- **Content Generation**: AI-assisted content creation

## 📚 Documentation

For detailed setup and deployment instructions, see [FULL_DOCUMENTATION.md](FULL_DOCUMENTATION.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.