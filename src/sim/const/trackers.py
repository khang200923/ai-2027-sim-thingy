from sim.const.utils import number_type_with_anchors
from dataclasses import dataclass

@dataclass
class Tracker:
    target: str
    format: str | None = None
    conditions: str | None = None

TRACKERS = [
    Tracker("Relationship between US government and China government"),
    Tracker("US stance on AI safety"),
    Tracker("Sentiment of the public towards AI"),
    Tracker("AI level of OpenBrain's frontier AI"),
    Tracker("AI level of DeepCent's frontier AI"),
    Tracker("Risk of AI misalignment in the current leading lab",
        format=number_type_with_anchors(10, {0: "no risk", 10: "catastrophic risk"})),
    Tracker("Impact of AI on global job markets",
        format=number_type_with_anchors(
            10,
            {
                0: "economy would stay the same without AI",
                5: "one would likely lose in most markets without AI",
                8: "AI replaces most jobs",
                10: "AI replaces every job, including AI capabilities"
            }
        )),
]
