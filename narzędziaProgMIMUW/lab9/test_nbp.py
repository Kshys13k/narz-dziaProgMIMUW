import pytest
from nbp_change import get_courses

def test_get_courses(monkeypatch):
    class MockResponse:
        mock_response_json = {
            "rates": [
                {"mid": 1.2345, "effectiveDate": "2023-05-22"},
                {"mid": 1.3456, "effectiveDate": "2023-05-23"}
            ],
            "currency": "Euro"
        }
        def json(self):
            return self.mock_response_json

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    values, currency = get_courses('EUR', 2)

    # Assert that the returned data is correct
    assert values == [1.2345, 1.3456], "The mid values should match the mock response"
    assert currency == "Euro", "The currency name should match the mock response"
