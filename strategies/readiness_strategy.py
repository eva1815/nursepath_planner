class ReadinessStrategy:
    """
    Strategy interface for readiness evaluation.
    """

    def evaluate(self, program, courses):
        raise NotImplementedError("Subclasses must implement evaluate().")