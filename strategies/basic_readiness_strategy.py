from strategies.readiness_strategy import ReadinessStrategy


class BasicReadinessStrategy(ReadinessStrategy):
    """
    Basic readiness evaluation strategy.

    This strategy checks:
    1. Whether the user's average grade meets the program's required average
    2. Whether any prerequisite course grade is below its minimum required grade
    """

    def evaluate(self, program, courses):
        # program tuple format:
        # (id, name, school_name, required_average)

        if not courses:
            return {
                "ready": False,
                "message": "No prerequisite courses found for this program.",
                "required_average": float(program[3]),
                "average_grade": 0.0,
                "failed_courses": []
            }

        total_grade = 0.0
        failed_courses = []

        for course in courses:
            # course tuple format:
            # (id, program_id, course_name, grade, minimum_required_grade)
            course_name = course[2]
            grade = float(course[3])
            minimum_required_grade = float(course[4])

            total_grade += grade

            if grade < minimum_required_grade:
                failed_courses.append({
                    "course_name": course_name,
                    "grade": grade,
                    "minimum_required_grade": minimum_required_grade
                })

        average_grade = total_grade / len(courses)
        required_average = float(program[3])

        if failed_courses:
            return {
                "ready": False,
                "message": "Some prerequisite courses are below the minimum required grade.",
                "required_average": required_average,
                "average_grade": average_grade,
                "failed_courses": failed_courses
            }

        if average_grade < required_average:
            return {
                "ready": False,
                "message": "Average grade is below the required program average.",
                "required_average": required_average,
                "average_grade": average_grade,
                "failed_courses": []
            }

        return {
            "ready": True,
            "message": "Application appears ready based on current grades.",
            "required_average": required_average,
            "average_grade": average_grade,
            "failed_courses": []
        }