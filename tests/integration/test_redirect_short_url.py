from pytest_bdd import scenarios, given, when, then
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

scenarios('features/redirect_short_url.feature')

@given('I have created a short URL for "<url>"')
def create_short_url(url):
    response = client.post("/api/routes/shorten", json={"original_url": url})
    assert response.status_code == 200
    return response.json()["short_url"]

@when('I visit the short URL')
def visit_short_url(create_short_url):
    response = client.get(f"/{create_short_url}", allow_redirects=False)
    return response

@then('I should be redirected to "<url>"')
def check_redirect_response(visit_short_url, url):
    assert visit_short_url.status_code == 307
    assert visit_short_url.headers["location"] == url
