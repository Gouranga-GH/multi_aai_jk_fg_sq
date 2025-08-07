from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

from app.config.settings import settings

def get_response_from_ai_agents(llm_id, query, system_prompt):
    """
    Smart Agentic AI that automatically decides which single tool to use based on the user prompt.
    Uses either Tavily search OR Wikipedia OR no tools for focused information gathering.
    Returns both the response and tool usage information.
    """
    llm = ChatGroq(model=llm_id)

    # Initialize tools
    tavily_tool = TavilySearchResults(max_results=3)
    wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

    # Create a comprehensive system prompt that enforces single tool usage
    enhanced_system_prompt = f"""
    {system_prompt}
    
    CRITICAL INSTRUCTION: You can ONLY use ONE tool maximum per response. You must choose between:
    1. Tavily Search: For current events, recent information, and real-time data
    2. Wikipedia: For historical facts, detailed explanations, and comprehensive overviews
    3. NO tools: For conversational, opinion-based, or direct answers
    
    Tool Selection Rules (STRICTLY FOLLOW):
    - Use Tavily Search ONLY for: current events, recent news, real-time data, live information, trending topics, breaking news
    - Use Wikipedia ONLY for: historical facts, detailed explanations, comprehensive overviews, academic topics, established knowledge, concepts, definitions
    - Use NO tools when: the query is conversational, opinion-based, doesn't require factual information, or can be answered directly
    
    CRITICAL: You are FORBIDDEN to use multiple tools. Choose exactly ONE tool or use no tools at all.
    If you need both current and historical information, choose the most relevant single tool based on the primary intent of the query.
    
    Always provide comprehensive, accurate, and helpful responses using only the chosen single tool.
    """

    # Create agent with both tools
    agent = create_react_agent(
        model=llm,
        tools=[tavily_tool, wikipedia_tool],
        state_modifier=enhanced_system_prompt
    )

    state = {"messages": query}

    response = agent.invoke(state)

    messages = response.get("messages")
    
    # Extract tool usage information with single-tool enforcement
    tool_usage = []
    used_tools = set()
    
    for message in messages:
        if hasattr(message, 'tool_calls') and message.tool_calls:
            # Only take the first tool call to enforce single-tool usage
            tool_call = message.tool_calls[0]  # Take only the first tool call
            tool_name = tool_call.get('name', 'unknown')
            used_tools.add(tool_name)
            tool_usage.append({
                'tool': tool_name,
                'args': tool_call.get('args', {}),
                'call_id': tool_call.get('id', '')
            })
            # Break after first tool call to enforce single-tool usage
            break
    
    # Get the final AI response
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    final_response = ai_messages[-1] if ai_messages else "No response generated."
    
    # Determine if tools were used or if it was default LLM
    if used_tools:
        tool_summary = f"Tool used: {', '.join(used_tools)}"
    else:
        tool_summary = "Default LLM response (no tools used)"
    
    return {
        "response": final_response,
        "tool_usage": tool_usage,
        "tools_used": list(used_tools),
        "tool_summary": tool_summary
    } 