# Concrete Strategy:
# This class implements the default readiness evaluation logic
# by checking average grade and minimum course requirements.

class ReadinessStrategy:
    """
    Strategy interface for readiness evaluation.
    """

    def evaluate(self, program, courses):
        raise NotImplementedError("Subclasses must implement evaluate().")