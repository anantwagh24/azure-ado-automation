import random


class TestDataGeneratorService:

    def generate_test_data(
            self,
            field_name
    ):

        field_name = field_name.lower()

        if "email" in field_name:

            return (
                f"test"
                f"{random.randint(100,999)}"
                f"@gmail.com"
            )

        elif "password" in field_name:

            return "Secure@123"

        elif "username" in field_name:

            return (
                f"testuser"
                f"{random.randint(100,999)}"
            )

        elif "phone" in field_name:

            return "9876543210"

        elif "amount" in field_name:

            return "1000"

        return "test_data"