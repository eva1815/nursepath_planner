from repositories.program_repository import ProgramRepository
from repositories.course_repository import CourseRepository
from strategies.readiness_strategy_factory import ReadinessStrategyFactory


class ReadinessService:
    """
    Service layer for evaluating whether a user is ready
    to apply to a selected nursing program.
    """

    def __init__(self):
        self.program_repository = ProgramRepository()
        self.course_repository = CourseRepository()

    def check_readiness(self, program_id: int):
        """
        Check readiness for a program by ID.
        This method fetches the program and related courses,
        then delegates evaluation to a strategy object created
        by the factory.
        """
        program = self.program_repository.get_program_by_id(program_id)
        if not program:
            return {
                "ready": False,
                "message": "Program ID not found.",
                "average_grade": 0.0,
                "failed_courses": []
            }

        courses = self.course_repository.get_courses_by_program(program_id)

        strategy = ReadinessStrategyFactory.create_strategy(program[1])
        return strategy.evaluate(program, courses)