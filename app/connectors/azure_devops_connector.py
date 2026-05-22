import requests
from requests.auth import HTTPBasicAuth

from app.core.config import (
    AZURE_DEVOPS_PAT,
    AZURE_ORG_URL,
    AZURE_PROJECT
)


class AzureDevOpsConnector:

    def __init__(self):
        self.base_url = AZURE_ORG_URL
        self.project = AZURE_PROJECT
        self.auth = HTTPBasicAuth('', AZURE_DEVOPS_PAT)

    def get_work_item(self, work_item_id):

        url = f"{self.base_url}/_apis/wit/workitems/{work_item_id}?$expand=relations&api-version=7.1"

        response = requests.get(url, auth=self.auth)

        response.raise_for_status()

        return response.json()

    def extract_child_work_item_ids(self, work_item_data):

        child_ids = []

        relations = work_item_data.get("relations", [])

        for relation in relations:

            relation_type = relation.get("rel")

            if relation_type == "System.LinkTypes.Hierarchy-Forward":
                url = relation.get("url")

                child_id = url.split("/")[-1]

                child_ids.append(int(child_id))

        return child_ids

    def fetch_complete_hierarchy(self, work_item_id):

        work_item = self.get_work_item(work_item_id)

        print(f"Processing Work Item: {work_item_id}")
        print(f"Relations: {work_item.get('relations', [])}")

        children = []

        child_ids = self.extract_child_work_item_ids(work_item)

        for child_id in child_ids:
            child_data = self.fetch_complete_hierarchy(child_id)

            children.append(child_data)

        return {
            "id": work_item.get("id"),
            "title": work_item["fields"].get("System.Title"),
            "type": work_item["fields"].get("System.WorkItemType"),
            "description": work_item["fields"].get("System.Description"),
            "children": children
        }