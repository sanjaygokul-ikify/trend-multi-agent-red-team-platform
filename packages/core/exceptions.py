class InvalidAgentError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class InvalidStrategyError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)