# NursePath Planner

NursePath Planner is a command-line Python application for prospective nursing students to track nursing programs, prerequisite courses, readiness status, and deadlines.

## Features
- Add a nursing program
- Add prerequisite courses and grades
- View readiness for a program
- Save important deadlines
- Use a cloud PostgreSQL database through Neon

## Project Structure
- `main.py` - application entry point
- `controllers/` - controller logic
- `views/` - command-line interface
- `services/` - business logic
- `strategies/` - readiness evaluation strategy
- `repositories/` - database access
- `models/` - domain models

## Database Tables
- `nursing_programs`
- `prerequisite_courses`
- `deadlines`

## Web API Demonstration
The file `email_api_test.py` demonstrates basic usage of the external email reminder API selected for the project. It sends a test request to the Resend API and prints the response to confirm successful web API access.

## Notes
This implementation is a Milestone 3 starter version. 

The file email_api_test.py demonstrates basic usage of the selected external web API for NursePath Planner. The script sends a test request to the Resend email API using an API key stored in the .env file. A successful response with HTTP status code 200 and a returned message ID confirms that the system can access and use the chosen web API.