from dotenv import load_dotenv
import os

load_dotenv()

AZURE_DEVOPS_PAT = os.getenv("AZURE_DEVOPS_PAT")

AZURE_ORG_URL = os.getenv("AZURE_ORG_URL")

AZURE_PROJECT = os.getenv("AZURE_PROJECT")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

TEST_CASE_LINKING_MODE = "FEATURE" #EPIC, FEATURE, STORY, NONE
# Link To Feature, Link To Story, Standalone