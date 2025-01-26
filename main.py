import argparse
from scenarios import SCENARIOS
from mind_evolution import MindEvolution

def main():
    parser = argparse.ArgumentParser(description='Run Mind Evolution Demo')
    parser.add_argument('scenario', choices=['travel', 'meeting', 'stegpoet'], help='Scenario to run')
    parser.add_argument('--verbose', action='store_true', help='Show detailed evolution steps')
    
    args = parser.parse_args()
    scenario = SCENARIOS[args.scenario]
    
    print("\nRunning Mind Evolution Demo")
    print(f"Scenario: {scenario['name']}: {scenario['task']}")
    print("Constraints:")
    for constraint in scenario['constraints']:
        print(f"- {constraint}")
    
    print("\nInitiating agent team...")
    evolution = MindEvolution()
    result = evolution.solve_task(scenario['task'], scenario['constraints'])
    
    if args.verbose:
        print("\nEvolution History:")
        for stage, data in result['evolution_history'].items():
            print(f"\n{stage.replace('_', ' ').title()}:")
            if 'thought_chain' in data:
                print("Thoughts:")
                for thought in data['thought_chain']:
                    print(f"- {thought}")
            print("\nOutput:")
            for key, value in data.items():
                if key != 'thought_chain':
                    print(f"{key}: {value}")
    
    print("\nFinal Solution:")
    print(result['final_solution'])

if __name__ == "__main__":
    main()
