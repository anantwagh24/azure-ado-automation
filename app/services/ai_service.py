import json

from openai import OpenAI

from app.prompts.test_case_prompt import build_test_case_prompt

from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


class AIService:

    def generate_test_cases(self, requirement_data):

        prompt = build_test_case_prompt(requirement_data)

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a Senior QA Architect."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        content = response.choices[0].message.content

        return json.loads(content)