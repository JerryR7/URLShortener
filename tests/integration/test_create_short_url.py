from pytest_bdd import scenarios, given, when, then
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

scenarios('features/create_short_url.feature')

@given('I have an original URL "<url>"')
def original_url(url):
    return url

@when('I create a short URL')
def create_short_url(original_url):
    response = client.post("/api/routes/shorten", json={"original_url": original_url})
    return response

@then('I should receive a short URL and an expiration date')
def check_short_url_response(create_short_url):
    data = create_short_url.json()
    assert create_short_url.status_code == 200
    assert "short_url" in data
    assert "expiration_date" in data
    assert data["success"] is True
