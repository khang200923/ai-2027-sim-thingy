from sim.const.utils import get
from sim.const.statements import STATEMENTS, DEFINITIONS
from sim.const.trackers import TRACKERS
from pathlib import Path

ground_template = get(Path(__file__).parent / "prompts" / "ground.md")

def get_ground(end_date: str) -> str:
    return ground_template.format(
        statements=STATEMENTS,
        trackers=TRACKERS,
        end_date=end_date,
        definitions=DEFINITIONS,
    )
