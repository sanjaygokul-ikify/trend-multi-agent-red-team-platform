from typing import Protocol
from dataclasses import dataclass


class Agent(Protocol):
    def execute(self, environment: 'Environment', strategy: 'Strategy') -> None:
        ...


class Strategy(Protocol):
    agent: 'Agent'
    def __init__(self, agent: 'Agent') -> None:
        self.agent = agent


class Environment(Protocol):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


class VMEnvironment(Environment):
    def __init__(self, name: str, vm_id: str) -> None:
        super().__init__(name)
        self.vm_id = vm_id


class SIEMInterface(Protocol):
    def capture_events(self, environment: Environment) -> None:
        ...


class Blockchain(Protocol):
    def store_audits(self, environment: Environment) -> None:
        ...

@dataclass
class Task:
    agent: Agent
    strategy: Strategy
    environment: Environment