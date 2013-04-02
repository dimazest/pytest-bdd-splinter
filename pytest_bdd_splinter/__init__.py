import pytest
from splinter import Browser


@pytest.fixture
def browser():
    return Browser()
