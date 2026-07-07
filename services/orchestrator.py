from packages.core.engine import Engine
from packages.utils.logging import setup_logging

class Orchestrator:
    def __init__(self, engine: Engine):
        self.engine = engine
        setup_logging()

    def run(self):
        self.engine.run()