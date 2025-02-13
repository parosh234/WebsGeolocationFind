import socket
import requests
import json
import pprint

def get_geolocation(domain):
    try:
        # Resolve domain to IP address
        ip_address = socket.gethostbyname(domain)
        print(f"Resolved IP Address: {ip_address}")

        # API URL for geolocation lookup
        request_url = f"https://geolocation-db.com/json/{ip_address}&position=true"

        # Send request to API
        response = requests.get(request_url)

        # Check for successful response
        if response.status_code == 200:
            geolocation = response.json()

            # Pretty print geolocation data
            print("\nGeolocation Information:")
            pprint.pprint(geolocation)
        else:
            print("Error: Unable to retrieve geolocation data.")
    except socket.gaierror:
        print("Error: Invalid domain name or network issue.")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

if __name__ == "__main__":
    domain_name = input("Enter a domain name: ")
    get_geolocation(domain_name)
