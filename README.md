# NursePath Planner

## Overview
NursePath Planner is a Python command-line application designed to help prospective nursing students organize and track their applications to Bachelor of Science in Nursing (BScN) programs.

The system allows users to:
- add and store nursing programs
- record prerequisite courses and grades
- view application readiness
- add and view important deadlines

The project also demonstrates:
- cloud database integration using Neon PostgreSQL
- external web API usage using the Resend email API

---

## Intended Users
The main users of NursePath Planner are prospective nursing students who need a simple way to manage program requirements, track grades, and remember important application deadlines.

---

## Main Features
- Add a nursing program
- View saved nursing programs
- Add prerequisite course information
- View application readiness
- Add deadlines
- View saved deadlines
- Demonstrate external email API usage with `email_api_test.py`

---

## Technologies Used
- Python
- PostgreSQL (Neon cloud database)
- `psycopg2-binary`
- `python-dotenv`
- `requests`
- Resend Email API

---

## Design Patterns Used
This project uses several software design patterns:

### 1. MVC (Model-View-Controller)
The application separates domain data, user interaction, and control flow.
- `models/` stores domain objects
- `views/` handles the command-line interface
- `controllers/` manages the application flow

### 2. Strategy Pattern
The Strategy Pattern is used for application readiness evaluation.
- `ReadinessStrategy` defines the common interface
- `BasicReadinessStrategy` implements the current readiness checking logic

### 3. Factory Pattern
The Factory Pattern is used to create the appropriate readiness strategy object.
- `ReadinessStrategyFactory` handles object creation

### 4. Repository Pattern
The Repository Pattern is used to separate database access logic from the rest of the application.
- `ProgramRepository`
- `CourseRepository`
- `DeadlineRepository`

---

## Project Structure
```text
nursepath_planner/
├── controllers/
├── models/
├── repositories/
├── services/
├── strategies/
├── views/
├── .env
├── .env.example
├── API_DEMO_README.md
├── email_api_test.py
├── main.py
├── README.md
├── requirements.txt
└── RUN_INSTRUCTIONS.md