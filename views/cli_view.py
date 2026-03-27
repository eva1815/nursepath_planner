def show_menu():
    print("\n=== NursePath Planner ===")
    print("1. Add nursing program")
    print("2. View nursing programs")
    print("3. Add prerequisite course")
    print("4. View application readiness")
    print("5. Add deadline")
    print("6. View deadlines")
    print("7. Exit")


def get_menu_choice() -> str:
    return input("Enter your choice: ").strip()


def prompt_program_data():
    name = input("Program name: ").strip()
    school_name = input("School name: ").strip()
    required_average = float(input("Required average: ").strip())
    return name, school_name, required_average


def prompt_course_data():
    program_id = int(input("Program ID: ").strip())
    course_name = input("Course name: ").strip()
    grade = float(input("Your grade: ").strip())
    minimum_required_grade = float(input("Minimum required grade: ").strip())
    return program_id, course_name, grade, minimum_required_grade


def prompt_deadline_data():
    program_id = int(input("Program ID: ").strip())
    title = input("Deadline title: ").strip()
    due_date = input("Due date (YYYY-MM-DD): ").strip()
    return program_id, title, due_date


def prompt_program_id() -> int:
    return int(input("Program ID: ").strip())


def show_message(message: str):
    print(message)
