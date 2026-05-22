from openai import OpenAI

from app.core.config import OPENAI_API_KEY


class SelfHealingService:

    def __init__(self):

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    def repair_locator(
            self,
            failed_locator,
            page_html,
            action
    ):

        prompt = f"""

You are an expert Playwright automation engineer.

A locator failed.

Failed locator:
{failed_locator}

Action:
{action}

HTML DOM:
{page_html[:15000]}

Return ONLY the best alternative CSS selector.

        """

        response = self.client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return (
            response
            .choices[0]
            .message
            .content
            .strip()
        )