from sim.const.prompts import get_ground
from sim.llm import parse, systemp

schema = {
    "type": "json_object"
}


def simulate(end_time: str) -> str:
    x = parse(
        messages=[systemp(get_ground(end_time))],
        temperature=0.2,
        max_tokens=10000,
        model="gpt-4o-mini-2024-07-18",
        response_format=schema,
    )
    x = x.choices[0].message.content
    return x
