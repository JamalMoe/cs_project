from ip_reputation import check_ip_reputation

def test_check_ip_reputation(mocker):
    fake_response = mocker.Mock()
    fake_response.json.return_value = {
        "data": {
            "ipAddress": "8.8.8.8",
            "abuseConfidenceScore": 0,
            "countryCode": "US",
            "totalReports": 0,
        }
    }
    fake_response.raise_for_status.return_value = None
    mocker.patch("ip_reputation.requests.get", return_value=fake_response)
    result = check_ip_reputation("8.8.8.8")
    assert result["abuse_score"] == 0
    assert result["country"] == "US"