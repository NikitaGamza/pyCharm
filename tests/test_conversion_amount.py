from src.external_api import conversion_amount
from unittest.mock import patch, Mock


def test_conversion_amount_success():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 10}

    with patch("requests.get", return_value=mock_response):
        result = conversion_amount("USD")
        assert result == 10