import logging
from typing import List, Dict
from .types import Agent, Strategy, Environment
from .exceptions import InvalidAgentError, InvalidStrategyError


class Engine:
    def __init__(self, agents: List[Agent], strategies: List[Strategy], environments: List[Environment]):
        self.agents = agents
        self.strategies = strategies
        self.environments = environments
        self.logger = logging.getLogger(__name__)

    def distribute_tasks(self) -> Dict[Agent, List[Strategy]]:
        tasks = {}
        for agent in self.agents:
            tasks[agent] = []
            for strategy in self.strategies:
                if strategy.agent == agent:
                    tasks[agent].append(strategy)
        return tasks

    def update_strategies(self, agent: Agent, new_strategies: List[Strategy]) -> None:
        for strategy in new_strategies:
            if strategy.agent != agent:
                raise InvalidStrategyError(f"Strategy {strategy} does not match agent {agent}")
        self.strategies = new_strategies

    def execute(self, agent: Agent, environment: Environment, strategy: Strategy) -> None:
        try:
            agent.execute(environment, strategy)
        except Exception as e:
            self.logger.error(f"Error executing agent {agent} in environment {environment} with strategy {strategy}: {e}")
            raise

    def run(self) -> None:
        tasks = self.distribute_tasks()
        for agent, strategies in tasks.items():
            for strategy in strategies:
                for environment in self.environments:
                    try:
                        self.execute(agent, environment, strategy)
                    except Exception as e:
                        self.logger.error(f"Error executing agent {agent} in environment {environment} with strategy {strategy}: {e}")

    def add_agent(self, agent: Agent) -> None:
        if not isinstance(agent, Agent):
            raise InvalidAgentError(f"Invalid agent {agent}")
        self.agents.append(agent)

    def add_strategy(self, strategy: Strategy) -> None:
        if not isinstance(strategy, Strategy):
            raise InvalidStrategyError(f"Invalid strategy {strategy}")
        self.strategies.append(strategy)

    def add_environment(self, environment: Environment) -> None:
        if not isinstance(environment, Environment):
            raise ValueError(f"Invalid environment {environment}")
        self.environments.append(environment)