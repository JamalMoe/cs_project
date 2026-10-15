"""Look up an IP address's abuse history using the AbuseIPDB API."""
import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.environ.get("ABUSEIPDB_KEY")
API_URL = "https://api.abuseipdb.com/api/v2/check"

def check_ip_reputation(ip_address: str) -> dict:
    """Return a short reputation summary for one IP address."""

    if not API_KEY:
        raise RuntimeError("ABUSEIPDB_KEY is not set, check your .env file")
    headers = {"Key": API_KEY, "Accept": "application/json"}
    params = {"ipAddress": ip_address, "maxAgeInDays": 90}
    
    try:
        response = requests.get(
            API_URL, headers=headers, params=params, timeout=5
        )
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise RuntimeError(f"Request to AbuseIPDB timed out for {ip_address}")
        
    except requests.exceptions.HTTPError as exc:
        raise RuntimeError(f"AbuseIPDB returned an error: {exc}")
    
    data = response.json()["data"]
    return {
        "ip": data["ipAddress"],
        "abuse_score": data["abuseConfidenceScore"],
        "country": data.get("countryCode"),
        "total_reports": data["totalReports"],
    }
# comment from master

if __name__ == "__main__":
    result = check_ip_reputation("149.56.150.161")
    print(result)