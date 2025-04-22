from const.utils import get
from const.statements import STATEMENTS, DEFINITIONS
from const.trackers import TRACKERS
from pathlib import Path

ground_template = get(Path(__file__).parent / "prompts" / "ground.md")

ground = ground_template.format(
    statements=STATEMENTS,
    trackers=TRACKERS,
    end_date="06/2025",
    definitions=DEFINITIONS,
)
