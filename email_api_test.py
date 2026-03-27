import os
import json
from typing import Any, Dict

import requests
from dotenv import load_dotenv


load_dotenv()

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
RESEND_FROM_EMAIL = os.getenv("RESEND_FROM_EMAIL")
RESEND_TO_EMAIL = os.getenv("RESEND_TO_EMAIL")


def validate_env() -> None:
    missing = []
    if not RESEND_API_KEY:
        missing.append("RESEND_API_KEY")
    if not RESEND_FROM_EMAIL:
        missing.append("RESEND_FROM_EMAIL")
    if not RESEND_TO_EMAIL:
        missing.append("RESEND_TO_EMAIL")

    if missing:
        raise EnvironmentError(
            "Missing environment variables: " + ", ".join(missing) + "\n"
            "Add them to your .env file before running this script."
        )


def build_payload() -> Dict[str, Any]:
    return {
        "from": RESEND_FROM_EMAIL,
        "to": [RESEND_TO_EMAIL],
        "subject": "NursePath Planner API Demo",
        "html": (
            "<strong>NursePath Planner Milestone 3</strong><br>"
            "This email proves the project can call an external web API."
        ),
    }


def send_test_email() -> None:
    validate_env()

    url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = build_payload()

    response = requests.post(url, headers=headers, json=payload, timeout=30)

    print("Status code:", response.status_code)
    try:
        data = response.json()
    except ValueError:
        print("Raw response:")
        print(response.text)
        response.raise_for_status()
        return

    print("Response JSON:")
    print(json.dumps(data, indent=2))
    response.raise_for_status()
    print("\nEmail API call completed successfully.")


if __name__ == "__main__":
    try:
        send_test_email()
    except Exception as exc:
        print("Error:", exc)
