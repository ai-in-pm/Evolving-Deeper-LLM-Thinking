from groq import Groq
from .base_agent import BaseAgent
import os

class GroqAgent(BaseAgent):
    def __init__(self):
        super().__init__("Groq Refiner")
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    async def think(self, context):
        self.record_thought("Analyzing critic feedback for improvement areas")
        self.record_thought("Identifying patterns in successful solution components")
        self.record_thought("Applying iterative refinement strategies")
        return "Generated refined solutions based on feedback"

    async def act(self, context):
        response = await self.client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {"role": "system", "content": "You are a solution refiner focused on iterative improvements."},
                {"role": "user", "content": f"""
                Original solutions: {context['current_solutions']}
                Critic feedback: {context['feedback']}
                Refine these solutions while maintaining their strengths and addressing the feedback.
                """}
            ]
        )
        
        refined_solutions = response.choices[0].message.content
        return {
            "refined_solutions": refined_solutions,
            "thought_chain": self.get_thought_chain()
        }
