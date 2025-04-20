from dataclasses import dataclass
from enum import Enum

class Capability(Enum):
    EXISTS = "exists"
    EMERGING = "emerging"
    FICTION = "fiction"

@dataclass
class SimState:
    capabilities: dict[str, Capability]
    situations: dict[str, str]
