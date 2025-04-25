from dataclasses import dataclass
from enum import Enum
import json
import re
from sim.const.prompts import ground
from sim.llm import parse, create, systemp
from pydantic import BaseModel, Field

class ResponseType(BaseModel):
    date: str = Field(..., pattern=r"^(0[1-9]|1[0-2])/20\d{2}$", description="Date in mm/YYYY format")
    situation: str = Field(..., description="Detailed information about the world in AI")
    tracker_fills: dict[str, str | None] = Field(..., description="Tracker name mapped to info or null if no significant change")

def simulate(end_time: str) -> str:
    x = parse(
        messages=[systemp(ground)],
        temperature=0.5,
        max_tokens=10000,
        model="gpt-4o-mini-2024-07-18",
        stop=[end_time]
    )
    x = x.choices[0].message.content
    print(x)
    x = re.sub(r',\s*\{\s*"date":\s*"$', "]", x, flags=re.MULTILINE)
    x = json.loads(x)
    return x
