from typing import List
from ..core.engine import Engine
from ..core.types import Task, Environment


class Executor:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def execute(self, tasks: List[Task]) -> None:
        for task in tasks:
            self.engine.execute(task.agent, task.environment, task.strategy)

    def run(self) -> None:
        tasks = self.engine.distribute_tasks()
        self.execute(tasks)