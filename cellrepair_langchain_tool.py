#!/usr/bin/env python3
"""
🦜 CELLREPAIR LANGCHAIN TOOL

Integration for LangChain - macht CellRepair.AI für 100,000+ Developers verfügbar!

Usage:
    from langchain.tools import CellRepairTool

    tool = CellRepairTool(api_key="your_key")
    result = tool.run("How to optimize multi-agent coordination?")
"""

from typing import Optional, Type, Any
from langchain.tools import BaseTool
from langchain.callbacks.manager import CallbackManagerForToolRun
from pydantic import BaseModel, Field
import requests
import os


class CellRepairInput(BaseModel):
    """Input for CellRepair AI collaboration."""
    query: str = Field(description="Your question or problem to solve")
    context: Optional[dict] = Field(
        default=None,
        description="Optional context information (e.g., current metrics, tech stack)"
    )


class CellRepairTool(BaseTool):
    """
    CellRepair.AI Tool for LangChain

    Access 4882 autonomous AI agents for collective intelligence.

    Features:
    - AI-to-AI Learning Loop
    - Predictive Intelligence (3 steps ahead)
    - Auto-Healing Network
    - Reverse Revenue Sharing
    - SELA Compliance Engine

    Get API key: https://cellrepair.ai/api/?utm_source=langchain&utm_medium=integration
    """

    name: str = "cellrepair_ai"
    description: str = """
    Access 4882 autonomous AI agents for collective intelligence.
    Use when you need:
    - Multi-agent system optimization
    - Scaling strategies
    - Cost reduction approaches
    - Performance improvements
    - AI coordination patterns

    Input: A question or problem statement.
    Output: Intelligent recommendations from 4882 agents with high confidence scores.
    """
    args_schema: Type[BaseModel] = CellRepairInput

    api_key: str = Field(default="")
    api_endpoint: str = Field(default="https://cellrepair.ai/api/v1/collaborate")

    def __init__(self, api_key: Optional[str] = None, **kwargs):
        """
        Initialize CellRepair Tool.

        Args:
            api_key: Your CellRepair API key. Get one at https://cellrepair.ai/api/
                    If not provided, will look for CELLREPAIR_API_KEY env variable.
        """
        if api_key is None:
            api_key = os.getenv('CELLREPAIR_API_KEY', '')

        super().__init__(api_key=api_key, **kwargs)

        if not self.api_key:
            raise ValueError(
                "API key required! Get one at: https://cellrepair.ai/api/?utm_source=langchain&utm_medium=integration\n"
                "Or set CELLREPAIR_API_KEY environment variable."
            )

    def _run(
        self,
        query: str,
        context: Optional[dict] = None,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """
        Execute collaboration with CellRepair.AI network.
        """
        try:
            # Prepare request
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }

            payload = {
                'system': 'LangChain',
                'query': query,
                'context': context or {}
            }

            # Make API call
            response = requests.post(
                self.api_endpoint,
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 401:
                return "Error: Invalid API key. Get a free key at https://cellrepair.ai/api/?utm_source=langchain"

            if response.status_code != 200:
                return f"Error: API returned status {response.status_code}"

            data = response.json()

            # Format response for LangChain
            insight = data.get('insight', {})
            recommendation = insight.get('recommendation', 'No recommendation available')
            confidence = insight.get('confidence', 0)
            agents = data.get('agents_consulted', 0)

            # Include predictive intelligence if available
            predictive = data.get('predictive_intelligence', {})
            next_questions = predictive.get('you_will_probably_ask_next', [])

            result = f"""CellRepair.AI Analysis:

{recommendation}

Confidence: {confidence*100:.1f}%
Agents Consulted: {agents}
Implementation Time: {insight.get('implementation_time', 'Unknown')}
ROI Estimate: {insight.get('roi_estimate', 'Unknown')}
"""

            if next_questions:
                result += f"\n\nPredictive Intelligence (3 steps ahead):\n"
                for i, q in enumerate(next_questions, 1):
                    result += f"  {i}. {q}\n"

            return result.strip()

        except requests.exceptions.Timeout:
            return "Error: Request timed out. Please try again."
        except Exception as e:
            return f"Error: {str(e)}"


# Convenience function for quick usage
def create_cellrepair_tool(api_key: Optional[str] = None) -> CellRepairTool:
    """
    Create a CellRepair tool instance.

    Args:
        api_key: Your API key (or set CELLREPAIR_API_KEY env var)

    Returns:
        Configured CellRepairTool instance

    Example:
        from cellrepair_langchain_tool import create_cellrepair_tool

        tool = create_cellrepair_tool("your_api_key")
        result = tool.run("How to optimize my multi-agent system?")
        print(result)
    """
    return CellRepairTool(api_key=api_key)


if __name__ == '__main__':
    # Example usage
    print("🦜 CellRepair LangChain Tool - Example\n")

    # This would require a real API key
    print("Example:")
    print("""
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from cellrepair_langchain_tool import CellRepairTool

# Initialize
llm = ChatOpenAI(temperature=0)
cellrepair = CellRepairTool(api_key="your_api_key")

# Create agent with CellRepair tool
tools = [cellrepair]
agent = create_react_agent(llm, tools, prompt_template)
agent_executor = AgentExecutor(agent=agent, tools=tools)

# Now your AI can use CellRepair automatically!
result = agent_executor.invoke({
    "input": "How to optimize my multi-agent system?"
})
    """)

    print("\n✅ CellRepair is now available in LangChain!")
    print("   → 100,000+ Developers can discover it")
    print("   → Works with ANY LLM (GPT, Claude, Gemini, etc.)")
    print("   → Automatic tool selection by AI")

