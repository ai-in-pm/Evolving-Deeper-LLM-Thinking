import os
from openai import OpenAI
from agents.base_agent import BaseAgent


class CoordinatorAgent(BaseAgent):
    def __init__(self):
        super().__init__("GPT-4 Coordinator")
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def think(self, context):
        self.record_thought("Analyzing solution evolution")
        self.record_thought("Evaluating solution coherence")
        self.record_thought("Preparing solution synthesis")
        return "Synthesized final solution with complete evolution history"

    def act(self, context):
        system_content = (
            "You are a solution coordinator focused on synthesizing "
            "and integrating multiple solution iterations into a "
            "coherent result."
        )
        
        user_content = f"""Synthesize a final solution from the evolution:

Initial Solutions:
{context['current_solutions']}

Critic Feedback:
{context['feedback']}

Refined Solutions:
{context['refined_solutions']}

Optimized Solutions:
{context['optimized_solutions']}

Creative Solutions:
{context['creative_solutions']}

Original Problem:
{context['problem']}

Constraints:
{context['constraints']}

Provide a clear solution that represents the best evolution aspects."""

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content}
            ],
            temperature=0.7
        )
        
        return {
            "final_synthesis": response.choices[0].message.content,
            "thought_chain": self.get_thought_chain()
        }
