from abc import ABC, abstractmethod
from typing import List, Dict, Any
import os
from dotenv import load_dotenv

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.thoughts = []
        load_dotenv()

    @abstractmethod
    async def think(self, context: Dict[str, Any]) -> str:
        """Chain of Thought reasoning step"""
        pass

    @abstractmethod
    async def act(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Take action based on thoughts"""
        pass

    def record_thought(self, thought: str):
        """Record a step in the Chain of Thought reasoning"""
        self.thoughts.append(thought)
        
    def get_thought_chain(self) -> List[str]:
        """Return the complete chain of thoughts"""
        return self.thoughts
