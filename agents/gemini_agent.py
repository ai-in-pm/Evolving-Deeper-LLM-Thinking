import google.generativeai as genai
from .base_agent import BaseAgent
import os

class GeminiAgent(BaseAgent):
    def __init__(self):
        super().__init__("Gemini Optimizer")
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel('gemini-pro')

    async def think(self, context):
        self.record_thought("Analyzing solution complexity and resource requirements")
        self.record_thought("Identifying optimization opportunities")
        self.record_thought("Applying computational efficiency improvements")
        return "Optimized solutions for scalability and efficiency"

    async def act(self, context):
        response = await self.model.generate_content(
            f"""
            Refined solutions: {context['refined_solutions']}
            Task: Optimize these solutions for computational efficiency while maintaining quality.
            Consider:
            1. Resource utilization
            2. Scalability
            3. Performance bottlenecks
            Provide optimized versions with efficiency improvements.
            """
        )
        
        optimized_solutions = response.text
        return {
            "optimized_solutions": optimized_solutions,
            "thought_chain": self.get_thought_chain()
        }
