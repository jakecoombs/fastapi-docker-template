import pytest


@pytest.fixture
def names():
    return ["Sample Name"]


@pytest.fixture
def emails():
    return ["example@example.com"]


@pytest.fixture
def names_and_emails(names, emails):
    return zip(names, emails, strict=True)


@pytest.fixture
def users(names_and_emails):
    return [{"name": name, "email": email} for name, email in names_and_emails]
