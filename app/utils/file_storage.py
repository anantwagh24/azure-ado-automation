import json
import os


class FileStorage:

    OUTPUT_DIR = "generated_test_cases"

    @classmethod
    def save_test_cases(cls, epic_id, test_cases):

        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)

        file_path = f"{cls.OUTPUT_DIR}/epic_{epic_id}_test_cases.json"

        with open(file_path, "w") as file:

            json.dump(test_cases, file, indent=4)

        return file_path