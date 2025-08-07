import streamlit as st
import requests

from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

st.set_page_config(page_title="Agentic AI" , layout="centered")
st.title("Smart Agentic AI with Intelligent Tool Selection")

st.markdown("""
This Agentic AI automatically chooses the best single tool for your query:
- **Tavily Search**: For current events, recent news, and real-time information
- **Wikipedia**: For historical facts, detailed explanations, and comprehensive knowledge
- **Smart Selection**: The AI chooses EXACTLY ONE tool or uses no tools at all
""")

system_prompt = st.text_area("Define your AI Agent: " , height=70)

user_query = st.text_area("Enter your query : " , height=150)

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask Agent") and user_query.strip():

    payload = {
        "model_name": settings.DEFAULT_MODEL,
        "system_prompt": system_prompt,
        "messages": [user_query]
    }

    try:
        logger.info("Sending request to backend")

        response = requests.post(API_URL , json=payload)

        if response.status_code==200:
            response_data = response.json()
            agent_response = response_data.get("response", "")
            tool_summary = response_data.get("tool_summary", "")
            tool_usage = response_data.get("tool_usage", [])
            
            logger.info("Sucesfully recived response from backend")

            # Display tool usage information
            st.subheader("🔧 Tool Usage")
            if tool_summary:
                if "Default LLM" in tool_summary:
                    st.info("🤖 " + tool_summary)
                else:
                    st.success("🛠️ " + tool_summary)
            
            # Add single-tool enforcement notice
            if tool_usage and len(tool_usage) > 1:
                st.warning("⚠️ Multiple tools detected - only the first tool was used")
            
            # Display detailed tool usage if available
            if tool_usage:
                with st.expander("📋 Detailed Tool Usage"):
                    st.write("**Single Tool Used:**")
                    for tool_call in tool_usage:
                        st.write(f"**Tool:** {tool_call.get('tool', 'Unknown')}")
                        st.write(f"**Arguments:** {tool_call.get('args', {})}")
                        st.write("---")

            # Display the main response
            st.subheader("💬 Agentic AI Response")
            st.markdown(agent_response.replace("\n","<br>"), unsafe_allow_html=True)

        else:
            logger.error("Backend error")
            st.error("Error with backend")
    
    except Exception as e:
        logger.error("Error occured while sending request to backend")
        st.error(str(CustomException("Failed to communicate to backend")))

        

