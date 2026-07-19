from typing import Protocol
from dataclasses import dataclass


class Agent(Protocol):
    def execute(self, environment: 'Environment', strategy: 'Strategy') -> None:
        ...


class Strategy(Protocol):
    agent: 'Agent'
    def __init__(self, agent: 'Agent') -> None:
        self.agent = agent

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Strategy) and self.agent == other.agent


class Environment(Protocol):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Environment) and self.name == other.name


class VMEnvironment(Environment):
    def __init__(self, name: str, vm_id: str) -> None:
        super().__init__(name)
        self.vm_id = vm_id

    def __eq__(self, other: object) -> bool:
        return isinstance(other, VMEnvironment) and self.name == other.name and self.vm_id == other.vm_id


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

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Task) and self.agent == other.agent and self.strategy == other.strategy and self.environment == other.environment