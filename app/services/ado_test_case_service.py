import json
import requests

from requests.auth import HTTPBasicAuth
from app.core.config import (
    TEST_CASE_LINKING_MODE
)

from app.core.config import (
    AZURE_DEVOPS_PAT,
    AZURE_ORG_URL,
    AZURE_PROJECT
)


class ADOTestCaseService:

    def __init__(self):

        self.base_url = (
            f"{AZURE_ORG_URL}/"
            f"{AZURE_PROJECT}"
        )

        self.auth = HTTPBasicAuth(
            "",
            AZURE_DEVOPS_PAT
        )

    def create_test_case(
            self,
            test_case,
            parent_id=None
    ):

        url = (
            f"{self.base_url}/"
            "_apis/wit/workitems/"
            "$Test%20Case"
            "?api-version=7.1"
        )

        steps_text = ""

        for index, step in enumerate(
                test_case["steps"],
                start=1
        ):
            steps_text += (
                f"{index}. {step}\n"
            )

        payload = [
            {
                "op": "add",
                "path": "/fields/System.Title",
                "value": test_case["title"]
            },
            {
                "op": "add",
                "path":
                    "/fields/Microsoft.VSTS.TCM.Steps",
                "value": steps_text
            }
        ]

        # Dynamic Parent Linking
        if parent_id:
            payload.append({

                "op": "add",

                "path": "/relations/-",

                "value": {

                    "rel":
                        "System.LinkTypes.Hierarchy-Reverse",

                    "url":
                        f"{self.base_url}/"
                        f"_apis/wit/workItems/"
                        f"{parent_id}"

                }

            })

        response = requests.post(

            url,

            headers={
                "Content-Type":
                    "application/json-patch+json"
            },

            auth=self.auth,

            data=json.dumps(payload)

        )

        response.raise_for_status()

        return response.json()

    def push_test_cases(
            self,
            test_cases,
            hierarchy_data,
            target
    ):

        created_test_cases = []

        parent_id = None

        target = target.upper()

        if target == "EPIC":

            parent_id = hierarchy_data["id"]

        elif target == "FEATURE":

            if hierarchy_data["children"]:
                parent_id = (
                    hierarchy_data["children"][0]["id"]
                )

        elif target == "STORY":

            if (
                    hierarchy_data["children"]
                    and
                    hierarchy_data["children"][0]["children"]
            ):
                parent_id = (

                    hierarchy_data
                    ["children"][0]
                    ["children"][0]
                    ["id"]

                )

        elif target == "NONE":

            parent_id = None

        for test_case in test_cases:
            created = (
                self.create_test_case(
                    test_case,
                    parent_id
                )
            )

            created_test_cases.append({

                "id": created["id"],

                "title":
                    created["fields"]["System.Title"]

            })

        return created_test_cases