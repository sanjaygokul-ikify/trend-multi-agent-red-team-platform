from packages.core.engine import Engine
from packages.core.types import VMEnvironment
from services.orchestrator import Orchestrator
import unittest

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        engine = Engine(agents=[], strategies=[], environments=[VMEnvironment('test_env', 'test_vm')])
        orchestrator = Orchestrator(engine)
        orchestrator.run()