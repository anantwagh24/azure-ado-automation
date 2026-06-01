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

        steps_text = "<steps id='0' last='{}'>".format(
            len(test_case["steps"])
        )

        for index, step in enumerate(
                test_case["steps"],
                start=1
        ):
            steps_text += f"""

        <step id="{index}" type="ActionStep">

            <parameterizedString isformatted="true">
                <![CDATA[{step}]]>
            </parameterizedString>

            <parameterizedString isformatted="true">
                <![CDATA[
                {test_case.get("expected_result", "")}
                ]]>
            </parameterizedString>

        </step>

        """

        steps_text += "</steps>"

        payload = [

            {
                "op": "add",

                "path":
                    "/fields/System.Title",

                "value":
                    test_case["title"]
            },

            {
                "op": "add",

                "path":
                    "/fields/Microsoft.VSTS.Common.Priority",

                "value":
                    1
            },

            {
                "op": "add",

                "path":
                    "/fields/System.Description",

                "value": f"""

        <b>Test Case ID:</b>

        {test_case.get("test_case_id", "")}

        <br><br>

        <b>Preconditions:</b>

        <br><br>

        {test_case.get("preconditions", "")}

        <br><br>

        <b>Expected Result:</b>

        <br><br>

        {test_case.get("expected_result", "")}

        <br><br>

        <b>Priority:</b>

        {test_case.get("priority", "")}

        <br><br>

        <b>Test Type:</b>

        {test_case.get("test_type", "")}

        """
            },

            {
                "op": "add",

                "path":
                    "/fields/Microsoft.VSTS.TCM.Steps",

                "value":
                    steps_text
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

                "id":
                    created["id"],

                "test_case_id":
                    test_case.get(
                        "test_case_id",
                        ""
                    ),

                "title":
                    test_case.get(
                        "title",
                        ""
                    ),

                "preconditions":
                    test_case.get(
                        "preconditions",
                        ""
                    ),

                "steps":
                    test_case.get(
                        "steps",
                        []
                    ),

                "expected_result":
                    test_case.get(
                        "expected_result",
                        ""
                    ),

                "priority":
                    test_case.get(
                        "priority",
                        ""
                    ),

                "test_type":
                    test_case.get(
                        "test_type",
                        ""
                    )

            })

        return created_test_cases