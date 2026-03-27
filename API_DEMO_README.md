# NursePath Planner - Web API Demo

This file demonstrates basic usage of the external email web API chosen for Milestone 3.

## Files
- `email_api_test.py` - sends one test email using the Resend Email API
- `.env.example` - shows which environment variables are required
- `requirements_api_demo.txt` - dependencies for the API demo

## Required .env values
Add these to your `.env` file:

```env
RESEND_API_KEY=your_resend_api_key_here
RESEND_FROM_EMAIL=Your Name <onboarding@resend.dev>
RESEND_TO_EMAIL=delivered@resend.dev
```

## Install dependencies
```bash
pip install -r requirements_api_demo.txt
```

## Run the demo
```bash
python email_api_test.py
```

## What this demonstrates
- the program can authenticate to an external web API
- the program can send a POST request with JSON data
- the program can receive and print the API response

