import asyncio
import time
from typing import List, Any, Dict, TypeVar
from agents.base_agent import BaseAgent
from agents.openai_agent import OpenAIAgent
from agents.emergence_agent import CoordinatorAgent

T = TypeVar('T', bound=BaseAgent)


class MindEvolution:
    def __init__(self):
        self.agents: List[T] = [
            OpenAIAgent("Solution Generator"),    # Solution Generator
            OpenAIAgent("Critic"),               # Critic
            OpenAIAgent("Refiner"),              # Refiner
            OpenAIAgent("Optimizer"),            # Optimizer
            OpenAIAgent("Creative Integrator"),   # Creative Integrator
            CoordinatorAgent()                   # Coordinator
        ]
    
    def animate_progress(self, stage: str) -> None:
        animation = "|/-\\"
        for i in range(20):
            print(
                f"\r{stage} {animation[i % len(animation)]}", 
                end="", 
                flush=True
            )
            time.sleep(0.1)
        print()
        
    def solve_task(self, task: str, constraints: List[str]) -> Dict[str, Any]:
        context = {
            "problem": task,
            "constraints": constraints,
            "current_solutions": [],
            "feedback": [],
            "iterations": 0
        }
        
        print("\nInitiating agent team...\n")
        
        # Stage 1: Generate initial solutions
        self.animate_progress("Generating initial solutions...")
        generator_result = self.agents[0].act(context)
        context["current_solutions"] = generator_result["solutions"]
        
        # Stage 2: Critic evaluation
        self.animate_progress("Evaluating solutions...")
        critic_result = self.agents[1].act(context)
        context["feedback"] = critic_result["feedback"]
        
        # Stage 3: Refinement
        self.animate_progress("Refining solutions...")
        refiner_result = self.agents[2].act(context)
        context["refined_solutions"] = refiner_result["refined_solutions"]
        
        # Stage 4: Optimization
        self.animate_progress("Optimizing solutions...")
        optimizer_result = self.agents[3].act(context)
        context["optimized_solutions"] = optimizer_result["optimized_solutions"]
        
        # Stage 5: Creative Integration
        self.animate_progress("Integrating creative elements...")
        creative_result = self.agents[4].act(context)
        context["creative_solutions"] = creative_result["creative_solutions"]
        
        # Stage 6: Final Synthesis
        self.animate_progress("Synthesizing final solution...")
        final_result = self.agents[5].act(context)
        
        print("\nEvolution complete!\n")
        synthesis = final_result.get("final_synthesis", "No synthesis available")
        return {
            "final_solution": synthesis,
            "evolution_history": {
                "generation": generator_result,
                "critique": critic_result,
                "refinement": refiner_result,
                "optimization": optimizer_result,
                "creative_integration": creative_result,
                "final_synthesis": final_result
            }
        }


async def main() -> None:
    evolution = MindEvolution()
    task = "TravelPlanner: Plan a 7-day trip to Europe visiting 3 cities"
    constraints = [
        "Budget: $3000",
        "Must include cultural and historical sites",
        "Maximum 2 hours between cities"
    ]
    
    result = evolution.solve_task(task, constraints)
    print("Evolution complete:", result)


if __name__ == "__main__":
    asyncio.run(main())
