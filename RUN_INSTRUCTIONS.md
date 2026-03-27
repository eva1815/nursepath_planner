# Run Instructions

## 1. Install dependencies
```bash
pip install -r requirements.txt
```

## 2. Create a `.env` file
Add your Neon connection string:

```env
DATABASE_URL=your_neon_postgresql_connection_string_here
```

## 3. Run the program
```bash
python main.py
```

## 4. First run behavior
The application will automatically create the required database tables if they do not already exist.

## 5. Menu options
- Add nursing program
- Add prerequisite course
- View readiness
- Add deadline
- View saved data
- Exit

## Optional Web API Demo
To test the external email API integration, run:

python email_api_test.py

This demonstrates basic access to the selected web API used for reminder functionality.