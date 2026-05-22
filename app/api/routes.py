from fastapi import APIRouter

from app.services.requirement_service import RequirementService

router = APIRouter()

service = RequirementService()


@router.get("/requirement/{work_item_id}")
def get_requirement(work_item_id: int):

    return service.fetch_requirement(work_item_id)

@router.get("/generate-test-cases/{work_item_id}")
def generate_test_cases(work_item_id: int):

    return service.generate_test_cases(work_item_id)

@router.get("/generate-bdd/{work_item_id}")
def generate_bdd(work_item_id: int):

    return service.generate_bdd_feature_file(
        work_item_id
    )

@router.get(
    "/generate-step-definitions/{work_item_id}"
)
def generate_step_definitions(
        work_item_id: int
):

    return (
        service.generate_step_definitions(
            work_item_id
        )
    )

@router.get(
    "/generate-business-flows/{work_item_id}"
)
def generate_business_flows(
        work_item_id: int
):

    return (
        service.generate_business_flows(
            work_item_id
        )
    )

@router.get(
    "/generate-page-objects/{work_item_id}"
)
def generate_page_objects(
        work_item_id: int
):

    return (
        service.generate_page_objects(
            work_item_id
        )
    )

@router.get(
    "/generate-playwright-framework"
)
def generate_playwright_framework():

    return (
        service
        .generate_playwright_framework()
    )

@router.get(
    "/generate-test-runner/{work_item_id}"
)
def generate_test_runner(
        work_item_id: int
):

    return (
        service.generate_test_runner(
            work_item_id
        )
    )

@router.get(
    "/push-test-cases-to-ado/{work_item_id}"
)
def push_test_cases_to_ado(
        work_item_id: int,
        target: str = "FEATURE"
):

    return (
        service.push_test_cases_to_ado(
            work_item_id,
            target
        )
    )

@router.get(
    "/generate-playwright-tests/{work_item_id}"
)
def generate_playwright_tests(
        work_item_id: int
):

    return (
        service.generate_playwright_tests(
            work_item_id
        )
    )