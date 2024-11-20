import requests


### API endpoints: 
# Events https://polisen.se/api/events (Get all 500 events)
# Datetime https://polisen.se/api/events?DateTime -->            example /api/events?DateTime=2019-01-04
# Location https://polisen.se/api/events?locationname= -->       example https://polisen.se/api/events?locationname=Stockholm
# Type of event https://polisen.se/api/events?type -->           example https://polisen.se/api/events?type=Misshandel



# Example code on how to query the API for all events.
# Define the API endpoint
url = 'https://polisen.se/api/events'

try:
    # Send a GET request to the API
    response = requests.get(url, timeout=10)  # Set a timeout to avoid hanging
    # Raise an exception for HTTP errors
    response.raise_for_status()
    # Parse the JSON response
    events = response.json()
    print(f"Successfully retrieved {len(events)} events.")
except requests.exceptions.Timeout:
    print("The request timed out. Please try again later.")
except requests.exceptions.ConnectionError:
    print("There was a connection error. Please check your internet connection.")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred: {req_err}")
except ValueError as json_err:
    print(f"Error parsing JSON response: {json_err}")
