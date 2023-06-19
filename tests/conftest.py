import allure
import pytest
from allure_commons.types import AttachmentType

TIME_OUT = 10

def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", required=True, help="REQUIRED: Base URL")

@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")

