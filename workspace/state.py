from dataclasses import dataclass, field
from typing import List


@dataclass
class WorkspaceTask:

    name: str

    status: str = "Waiting"

    progress: int = 0


@dataclass
class Workspace:

    mission: str = ""

    tasks: List[WorkspaceTask] = field(default_factory=list)

    overall_progress: int = 0

    running: bool = False


workspace = Workspace()
