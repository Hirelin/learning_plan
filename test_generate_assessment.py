import json
from services import assessment_generator

topic = "Introduction to Python"
num_questions = 5  # you can change

try:
    questions = assessment_generator.generate_assessment(topic, num_questions)

    # Pretty print to console
    print(json.dumps(questions, indent=2))

    # Save to file
    with open("mock_assessment.json", "w") as f:
        json.dump(questions, f, indent=2)

    print("✅ Saved to mock_assessment.json")

except Exception as e:
    print("❌ Failed to generate assessment:", e)
