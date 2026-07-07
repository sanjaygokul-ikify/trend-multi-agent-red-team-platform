from typing import Dict
from logging import getLogger

logger = getLogger(__name__)

class MetricException(Exception):
    pass

class Metrics:
    def __init__(self):
        self.metrics: Dict[str, float] = {}

    def add_metric(self, name: str, value: float) -> None:
        try:
            self.metrics[name] = value
            logger.info(f"Added metric: {name} = {value}")
        except Exception as e:
            logger.error(f"Failed to add metric: {name} = {value}. Error: {e}")
            raise MetricException(f"Failed to add metric: {name} = {value}. Error: {e}")

    def get_metric(self, name: str) -> float:
        try:
            return self.metrics[name]
        except KeyError as e:
            logger.error(f"Metric not found: {name}. Error: {e}")
            raise MetricException(f"Metric not found: {name}. Error: {e}")

    def remove_metric(self, name: str) -> None:
        try:
            del self.metrics[name]
            logger.info(f"Removed metric: {name}")
        except KeyError as e:
            logger.error(f"Metric not found: {name}. Error: {e}")
            raise MetricException(f"Metric not found: {name}. Error: {e}")