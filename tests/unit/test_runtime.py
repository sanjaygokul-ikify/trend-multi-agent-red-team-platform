from packages.core.engine import Engine
import unittest

class TestRuntime(unittest.TestCase):
    def test_engine_run(self):
        engine = Engine(agents=[], strategies=[], environments=[])
        engine.run()