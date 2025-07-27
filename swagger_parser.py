import requests
import json

def fetch_swagger_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch Swagger JSON: {e}")
        return None

def parse_swagger(swagger_data):
    print("Available API Endpoints:\n")
    paths = swagger_data.get("paths", {})
    
    for endpoint, methods in paths.items():
        print(f"Endpoint: {endpoint}")
        for method, details in methods.items():
            summary = details.get("summary", "No description provided.")
            print(f"  Method: {method.upper()} - {summary}")
        print()

if __name__ == "__main__":
    # Swagger Petstore URL
    swagger_url = "http://petstore.swagger.io/v2/swagger.json"
    
    swagger_json = fetch_swagger_json(swagger_url)
    
    if swagger_json:
        parse_swagger(swagger_json)
