# Evolving Deeper LLM Thinking

A multi-agent system demonstrating the principles of Mind Evolution through collaborative problem-solving using different LLM providers.

The development of this repository was inspired by the "Evolving Deeper LLM Thinking" paper. To read the full article, visit https://arxiv.org/pdf/2501.09891

## Overview

This project implements a team of six AI agents, each powered by a different LLM provider, to showcase the Mind Evolution methodology in solving complex natural language planning tasks. The agents work together to generate, evaluate, refine, and optimize solutions through an iterative process, with real-time progress visualization.

## Agents

1. **OpenAI Agent (Solution Generator)**
   - Generates diverse initial solutions
   - Focuses on exploration and creativity

2. **Anthropic Agent (Critic)**
   - Evaluates solutions against constraints
   - Provides detailed feedback for improvement

3. **Groq Agent (Refiner)**
   - Implements iterative refinement
   - Incorporates feedback into solutions

4. **Gemini Agent (Optimizer)**
   - Focuses on computational efficiency
   - Ensures solution scalability

5. **Cohere Agent (Creative Integrator)**
   - Enhances solutions with creative elements
   - Maintains functionality while adding style

6. **GPT-4 Agent (Coordinator)**
   - Oversees the evolution process
   - Synthesizes final solutions

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
.\venv\Scripts\activate

# Unix/MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables in `.env`:
```env
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
COHERE_API_KEY=your_key_here
```

## Usage

Run the application with one of the following scenarios:

```bash
# Plan a 7-day European trip visiting 3 cities
python main.py travel

# Schedule a series of 5 team meetings across different time zones
python main.py meeting

# Create a poem that encodes a hidden message about AI evolution
python main.py stegpoet
```

Add the --verbose flag to see detailed evolution steps:
```bash
python main.py travel --verbose
```

## Architecture

The system follows a staged evolution process with real-time progress visualization:
1. Initial solution generation
2. Critical evaluation
3. Iterative refinement
4. Optimization
5. Creative integration
6. Final synthesis

Each agent implements Chain of Thought (CoT) reasoning, making their decision-making process transparent and traceable.

## Example Output

Here's an example of the travel planning scenario output:

```
Running Mind Evolution Demo
Scenario: Plan a 7-day trip to Europe visiting 3 cities
Constraints:
- Budget: $3000 (transport, lodging, food)
- Must include pre-booked cultural and historical sites
- Maximum 2 hours between cities by train or bus
- Consider seasonal weather and peak tourist times
- Account for language barriers and local customs
- Plan around attraction opening hours and weekly closures
- Include backup plans for transportation strikes or delays
- Consider visa requirements and processing times
- Factor in time zones and jet lag recovery
- Include travel insurance and medical considerations
- Account for luggage restrictions and storage
- Plan for local currency and payment methods
- Consider mobile connectivity and Wi-Fi access
- Include emergency contact information and embassy locations

[Progress Animation Shows Each Stage]
Generating initial solutions... |/-\|
Evaluating solutions... |/-\|
Refining solutions... |/-\|
Optimizing solutions... |/-\|
Integrating creative elements... |/-\|
Synthesizing final solution... |/-\|

Final Solution: "Cultural and Historical Capitals"
1. Cities & Transport:
   - Amsterdam → Brussels (1.5h train)
   - Brussels → Vienna (1.5h flight)
2. Duration:
   - Amsterdam: 3 days
   - Brussels: 2 days
   - Vienna: 3 days
3. Key Attractions:
   - Amsterdam: Anne Frank House, Van Gogh Museum, canal cruise
   - Brussels: Atomium, Grand Place, local experiences
   - Vienna: Schönbrunn Palace, State Opera, classical concert
4. Budget Breakdown ($2,700):
   - Transport: $700
   - Lodging: $800
   - Food: $450
   - Attractions: $150
   - Insurance: $100
   - Misc: $500
```

## Requirements

- Python 3.8+
- See `requirements.txt` for package dependencies
