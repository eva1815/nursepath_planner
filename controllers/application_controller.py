# MVC Pattern:
# This controller handles user requests from the CLI view
# and coordinates actions between the view, services, and repositories.

from repositories.deadline_repository import DeadlineRepository
from repositories.program_repository import ProgramRepository
from repositories.course_repository import CourseRepository
from services.readiness_service import ReadinessService
from views import cli_view


class ApplicationController:
    def __init__(self):
        self.program_repository = ProgramRepository()
        self.course_repository = CourseRepository()
        self.deadline_repository = DeadlineRepository()
        self.readiness_service = ReadinessService()

    def run(self):
        while True:
            try:
                cli_view.show_menu()
                choice = cli_view.get_menu_choice()

                if choice == "1":
                    self.add_program()
                elif choice == "2":
                    self.view_programs()
                elif choice == "3":
                    self.add_course()
                elif choice == "4":
                    self.view_readiness()
                elif choice == "5":
                    self.add_deadline()
                elif choice == "6":
                    self.view_deadlines()
                elif choice == "7":
                    cli_view.show_message("Goodbye.")
                    break
                else:
                    cli_view.show_message("Invalid choice. Please try again.")
            except Exception as exc:
                cli_view.show_message(f"Error: {exc}")

    def add_program(self):
        name, school_name, required_average = cli_view.prompt_program_data()
        self.program_repository.add_program(name, school_name, required_average)
        cli_view.show_message("Program added successfully.")

    def view_programs(self):
        programs = self.program_repository.get_all_programs()
        if not programs:
            cli_view.show_message("No nursing programs found.")
            return

        print("\nSaved Nursing Programs")
        for program in programs:
            print(
                f"ID: {program[0]} | Program: {program[1]} | School: {program[2]} | Required Average: {float(program[3]):.2f}"
            )

    def add_course(self):
        program_id, course_name, grade, minimum_required_grade = cli_view.prompt_course_data()
        program = self.program_repository.get_program_by_id(program_id)
        if not program:
            cli_view.show_message("Program ID not found.")
            return

        self.course_repository.add_course(program_id, course_name, grade, minimum_required_grade)
        cli_view.show_message("Prerequisite course added successfully.")

# The controller delegates readiness checking to the service layer.
# The service uses the Factory and Strategy patterns internally.
    def view_readiness(self):
        program_id = cli_view.prompt_program_id()
        result = self.readiness_service.check_readiness(program_id)

        print("\n=== Readiness Result ===")
        print(f"Status: {'Ready' if result.get('ready') else 'Not Ready'}")
        print(f"Message: {result.get('message')}")
        if 'required_average' in result:
            print(f"Required Average: {float(result['required_average']):.2f}")
        print(f"Current Average: {float(result.get('average_grade', 0.0)):.2f}")

        failed_courses = result.get("failed_courses", [])
        if failed_courses:
            print("Courses below minimum requirement:")
            for course in failed_courses:
                print(
                    f"- {course['course_name']}: {course['grade']:.2f} / minimum {course['minimum_required_grade']:.2f}"
                )

    def add_deadline(self):
        program_id, title, due_date = cli_view.prompt_deadline_data()
        program = self.program_repository.get_program_by_id(program_id)
        if not program:
            cli_view.show_message("Program ID not found.")
            return

        self.deadline_repository.add_deadline(program_id, title, due_date)
        cli_view.show_message("Deadline added successfully.")

    def view_deadlines(self):
        program_id = cli_view.prompt_program_id()
        deadlines = self.deadline_repository.get_deadlines_by_program(program_id)
        if not deadlines:
            cli_view.show_message("No deadlines found for this program.")
            return

        print("\nSaved Deadlines")
        for deadline in deadlines:
            print(f"ID: {deadline[0]} | Title: {deadline[2]} | Due Date: {deadline[3]}")
