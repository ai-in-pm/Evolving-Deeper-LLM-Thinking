from anthropic import Anthropic
from .base_agent import BaseAgent
import os

class AnthropicAgent(BaseAgent):
    def __init__(self):
        super().__init__("Anthropic Critic")
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    async def think(self, context):
        self.record_thought("Evaluating solution candidates against constraints")
        self.record_thought("Identifying optimization opportunities")
        self.record_thought("Generating constructive feedback")
        return "Completed solution evaluation with detailed feedback"

    async def act(self, context):
        response = await self.client.messages.create(
            model="claude-3-opus-20240229",
            messages=[{
                "role": "user",
                "content": f"Evaluate these solutions and provide detailed feedback: {context['solutions']}"
            }]
        )
        
        feedback = response.content
        return {
            "feedback": feedback,
            "thought_chain": self.get_thought_chain()
        }
