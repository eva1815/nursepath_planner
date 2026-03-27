# Repository Pattern:
# This repository handles all database operations related to nursing programs.
# It keeps SQL logic separate from the rest of the application.

from strategies.basic_readiness_strategy import BasicReadinessStrategy


class ReadinessStrategyFactory:
    """
    Factory class responsible for creating readiness strategy objects.

    This adds a clear creational design pattern to the project.
    Right now the system always returns BasicReadinessStrategy,
    but this can be extended later for program-specific strategies.
    """

    @staticmethod
    def create_strategy(program_name: str = None):
        return BasicReadinessStrategy()