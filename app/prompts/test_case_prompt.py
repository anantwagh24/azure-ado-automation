def build_test_case_prompt(requirement_data):

    return f"""
You are a Senior QA Automation Architect.

Generate comprehensive manual test cases.

Requirement Data:
{requirement_data}

STRICT RULES:
1. Return ONLY valid JSON.
2. Do NOT wrap response in markdown.
3. Do NOT use ```json.
4. Output must be parseable directly.
5. Return an array of test cases.

JSON Structure:
[
  {{
    "test_case_id": "",
    "title": "",
    "preconditions": "",
    "steps": [],
    "expected_result": "",
    "priority": "",
    "test_type": ""
  }}
]
"""