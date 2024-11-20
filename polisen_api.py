import requests



### API endpoints: 
# Events https://polisen.se/api/events (Get all 500 events)

# Datetime https://polisen.se/api/events?DateTime, example /api/events?DateTime=2019-01-04

# Location https://polisen.se/api/events?locationname=, example https://polisen.se/api/events?locationname=Stockholm

# Type of event https://polisen.se/api/events?type, example https://polisen.se/api/events?type=Misshandel


url = "https://polisen.se/api/events"

# Example code on how to query the API for all events.

# Send a GET request to the API
response = requests.get(url)
# Raise an exception for HTTP errors
response.raise_for_status()
# Parse the JSON response
events = response.json()


# Print nummber of events
print(len(events))

print(events[:5])