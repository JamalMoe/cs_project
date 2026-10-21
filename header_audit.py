"""Check a web server for missing HTTP security headers."""
import requests
REQUIRED_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
]

def check_security_headers(url: str) -> dict:
    """Return the status code and any required headers that are missing."""
    response = requests.get(url, timeout=5)
    missing = [h for h in REQUIRED_HEADERS if h not in response.headers]
    server_banner = response.headers.get("Server")
    return {
        "url": url,
        "status": response.status_code,
        "missing_headers": missing,
        "server_banner": server_banner,
    }

if __name__ == "__main__":
    result = check_security_headers("https://google.com")
    print(f"URL: {result['url']}")
    print(f"Status: {result['status']}")
    if result["server_banner"]:
        print(f"Server banner exposed: {result['server_banner']}")
    if result["missing_headers"]:
        print("Missing headers:")
        for header in result["missing_headers"]:
            print(f" - {header}")
    else:
        print("All required headers present.")