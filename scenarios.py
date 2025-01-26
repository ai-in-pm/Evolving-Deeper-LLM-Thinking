SCENARIOS = {
    'travel': {
        'task': 'Plan a 7-day trip to Europe visiting 3 cities',
        'constraints': [
            'Budget: $3000 (transport, lodging, food)',
            'Must include pre-booked cultural and historical sites',
            'Maximum 2 hours between cities by train or bus',
            'Consider seasonal weather and peak tourist times',
            'Account for language barriers and local customs',
            'Plan around attraction opening hours and weekly closures',
            'Include backup plans for transportation strikes or delays',
            'Consider visa requirements and processing times',
            'Factor in time zones and jet lag recovery',
            'Include travel insurance and medical considerations',
            'Account for luggage restrictions and storage',
            'Plan for local currency and payment methods',
            'Consider mobile connectivity and Wi-Fi access',
            'Include emergency contact information and embassy locations'
        ],
        'name': 'TravelPlanner'
    },
    'meeting': {
        'task': 'Schedule 5 team meetings across time zones',
        'constraints': [
            'Must accommodate team members in PST, EST, and GMT',
            'Each meeting must be 1 hour long',
            'No meetings outside of working hours in any timezone'
        ],
        'name': 'Meeting Planner'
    },
    'stegpoet': {
        'task': 'Create a poem encoding a hidden message about AI',
        'constraints': [
            'Must follow traditional sonnet structure',
            'First letter of each line reveals hidden message',
            'Maintain natural poetic flow and meaning'
        ],
        'name': 'StegPoet Generator'
    }
}
