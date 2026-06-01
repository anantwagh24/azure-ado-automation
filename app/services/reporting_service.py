import json
import os


class ReportingService:

    def generate_report(
            self,
            test_results
    ):

        os.makedirs(
            "reports",
            exist_ok=True
        )

        report_path = (
            "reports/execution_report.html"
        )

        html_content = f"""

        <html>

        <head>

            <title>
                AI Automation Report
            </title>

        </head>

        <body>

            <h1>
                Execution Summary
            </h1>

            <pre>
                {json.dumps(test_results, indent=4)}
            </pre>

        </body>

        </html>

        """

        with open(
                report_path,
                "w"
        ) as file:

            file.write(html_content)

        return report_path