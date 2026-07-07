from packages.core.engine import Engine
from services.orchestrator import Orchestrator
import argparse

parser = argparse.ArgumentParser(description='Multi-Agent Red Team Platform')
parser.add_argument('--agents', type=int, default=1, help='number of agents')
parser.add_argument('--strategies', type=int, default=1, help='number of strategies')
parser.add_argument('--environments', type=int, default=1, help='number of environments')
args = parser.parse_args()

engine = Engine(agents=[], strategies=[], environments=[])
orchestrator = Orchestrator(engine)
orchestrator.run()