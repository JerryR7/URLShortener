import pytest

@pytest.fixture
def mock_repository(mocker):
    """ Fixture for mocking repository across all unit tests. """
    repository_mock = mocker.patch('app.infrastructure.repositories.short_url_repository_impl.ShortUrlRepositoryImpl')
    return repository_mock
