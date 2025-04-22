from dataclasses import dataclass
from enum import Enum
from const.prompts import ground
from llm import parse, create, systemp

def simulate() -> str:
    return create(
        messages=[systemp(ground)],
        temperature=0.5,
        max_tokens=10000,
        model="gpt-4o-mini-2024-07-18"
    )
