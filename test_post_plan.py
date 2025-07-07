import requests
import json

url = "http://127.0.0.1:5000/api/init"
payload = {
    "skill": "Python",
    "deadline": "2025-12-31"
}

try:
    response = requests.post(url, json=payload)
    response.raise_for_status()  # raises exception for HTTP 4xx/5xx
    data = response.json()

    # Pretty print to console
    print(json.dumps(data, indent=2))

    # Save plan only, or whole response (with user_id)
    with open("generated_plan.json", "w") as f:
        json.dump(data, f, indent=2)

    print("✅ Saved to generated_plan.json")

except requests.exceptions.RequestException as e:
    print("❌ HTTP request failed:", e)
except Exception as e:
    print("❌ Something else went wrong:", e)
