import os
from openai import OpenAI
from agents.base_agent import BaseAgent


class OpenAIAgent(BaseAgent):
    def __init__(self, role="Solution Generator"):
        super().__init__(f"OpenAI {role}")
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.role = role

    def think(self, context):
        thoughts = {
            "Solution Generator": [
                "Analyzing problem space and constraints",
                "Generating diverse initial solutions",
                "Applying exploration principles"
            ],
            "Critic": [
                "Evaluating solution feasibility",
                "Identifying improvements",
                "Assessing constraints"
            ],
            "Refiner": [
                "Analyzing feedback",
                "Finding refinement paths",
                "Planning improvements"
            ],
            "Optimizer": [
                "Analyzing solutions",
                "Finding optimizations",
                "Improving efficiency"
            ],
            "Creative Integrator": [
                "Analyzing solutions",
                "Finding synergies",
                "Creating combinations"
            ]
        }
        
        for thought in thoughts.get(self.role, []):
            self.record_thought(thought)
        
        return f"Completed {self.role.lower()} analysis"

    def act(self, context):
        system_prompts = {
            "Solution Generator": (
                "Generate 3 detailed and diverse solutions for the given task."
            ),
            "Critic": (
                "Evaluate solutions for feasibility and provide improvement feedback."
            ),
            "Refiner": (
                "Improve solutions based on feedback while maintaining strengths."
            ),
            "Optimizer": (
                "Enhance solution efficiency while maintaining quality."
            ),
            "Creative Integrator": (
                "Create innovative hybrid solutions from the best elements."
            )
        }
        
        # Safe access to context with defaults
        current_solutions = context.get('current_solutions', [])
        feedback = context.get('feedback', [])
        refined_solutions = context.get('refined_solutions', [])
        optimized_solutions = context.get('optimized_solutions', [])
        constraints = context.get('constraints', [])
        problem = context.get('problem', '')
        
        user_prompts = {
            "Solution Generator": f"""Generate 3 diverse solutions for this travel planning problem:

Problem: {problem}

Constraints:
{chr(10).join(f'- {c}' for c in constraints)}

For each solution, provide:
1. Cities to visit with travel time between them
2. Duration in each city
3. Key attractions and activities
4. Estimated costs
5. Travel logistics

Format each solution clearly and number them 1-3.""",

            "Critic": f"""Evaluate these solutions considering our constraints:

Solutions:
{current_solutions}

Constraints:
{chr(10).join(f'- {c}' for c in constraints)}

For each solution provide:
1. Feasibility analysis
2. Constraint satisfaction
3. Specific improvements needed
4. Strengths to maintain""",

            "Refiner": f"""Refine these solutions based on the feedback:

Original Solutions:
{current_solutions}

Feedback Received:
{feedback}

Constraints:
{chr(10).join(f'- {c}' for c in constraints)}

Provide 3 refined solutions that address the feedback while maintaining the original strengths.""",

            "Optimizer": f"""Optimize these solutions for efficiency:

Solutions to Optimize:
{refined_solutions}

Constraints:
{chr(10).join(f'- {c}' for c in constraints)}

For each solution, optimize:
1. Time management
2. Cost efficiency
3. Travel logistics
4. Activity scheduling""",

            "Creative Integrator": f"""Create innovative combinations of these optimized solutions:

Optimized Solutions:
{optimized_solutions}

Constraints:
{chr(10).join(f'- {c}' for c in constraints)}

Create 2-3 hybrid solutions that:
1. Combine the best elements
2. Add creative enhancements
3. Maximize value and experience"""
        }

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompts[self.role]},
                {"role": "user", "content": user_prompts[self.role]}
            ],
            temperature=0.7
        )
        
        content = response.choices[0].message.content
        return {
            "solutions": content if self.role == "Solution Generator" else None,
            "feedback": content if self.role == "Critic" else None,
            "refined_solutions": content if self.role == "Refiner" else None,
            "optimized_solutions": content if self.role == "Optimizer" else None,
            "creative_solutions": content if self.role == "Creative Integrator" else None,
            "thought_chain": self.get_thought_chain()
        }
