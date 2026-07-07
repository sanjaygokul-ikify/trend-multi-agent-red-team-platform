from packages.core.engine import Engine, Agent, Strategy, Environment
import unittest
from unittest.mock import Mock

class TestEngine(unittest.TestCase):
    def test_distribute_tasks(self):
        agent = Mock(spec=Agent)
        strategy = Mock(spec=Strategy)
        environment = Mock(spec=Environment)
        engine = Engine(agents=[agent], strategies=[strategy], environments=[environment])
        tasks = engine.distribute_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertIn(agent, tasks)
        self.assertEqual(len(tasks[agent]), 1)
        self.assertIn(strategy, tasks[agent])