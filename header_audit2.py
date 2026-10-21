
import requests

REQUIRED_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
]

def check_security_headers(url: str) -> dict:
    try:
        response = requests.get(url, timeout=5)
        missing = [h for h in REQUIRED_HEADERS if h not in response.headers]

        return {
            "url": url,
            "status": response.status_code,
            "missing_headers": missing,
            "server_banner": response.headers.get("Server"),
        }

    except requests.exceptions.Timeout:
        return {"error": "Request timed out."}
    except requests.exceptions.ConnectionError:
        return {"error": "Website unreachable or invalid URL."}
    except requests.exceptions.RequestException:
        return {"error": "Request failed."}

if __name__ == "__main__":
    result = check_security_headers("https://safaricom.com")

    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Status: {result['status']}")

        if result["missing_headers"]:
            print("Missing headers:", ", ".join(result["missing_headers"]))
        else:
            print("All required headers present.")

        if result["server_banner"]:
            print(f"Server: {result['server_banner']}")
