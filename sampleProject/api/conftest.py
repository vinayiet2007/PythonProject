import pytest

from common.api.api_client.api_client import APIClient
from common.ui.base_classes.driver import Driver
from sampleProject.ui.pages.login_page import LoginPage


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        formatted_docstring = docstring.format(**item.funcargs)
        report.nodeid = formatted_docstring
    else:
        report.nodeid = f"Running test with arguments: {item.funcargs}"

@pytest.fixture
def set_api_client():
    api_client=APIClient("https://api.agify.io")
    yield api_client

