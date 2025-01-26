import cohere
from .base_agent import BaseAgent
import os

class CohereAgent(BaseAgent):
    def __init__(self):
        super().__init__("Cohere Creative Integrator")
        self.client = cohere.Client(os.getenv("COHERE_API_KEY"))

    async def think(self, context):
        self.record_thought("Analyzing solution structure for creative opportunities")
        self.record_thought("Identifying areas for style enhancement")
        self.record_thought("Integrating creative elements while maintaining functionality")
        return "Enhanced solutions with creative elements"

    async def act(self, context):
        response = await self.client.generate(
            model='command',
            prompt=f"""
            Optimized solutions: {context['optimized_solutions']}
            Task: Enhance these solutions with creative elements while maintaining their core functionality.
            Focus on:
            1. Style and presentation
            2. User engagement
            3. Innovative approaches
            Provide creatively enhanced versions of the solutions.
            """,
            max_tokens=1000,
            temperature=0.8
        )
        
        creative_solutions = response.generations[0].text
        return {
            "creative_solutions": creative_solutions,
            "thought_chain": self.get_thought_chain()
        }
