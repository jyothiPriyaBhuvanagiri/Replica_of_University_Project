import requests

# Overpass API endpoint
overpass_url = "http://overpass-api.de/api/interpreter"

# Define Overpass query to get places in Berlin (cities, towns, villages)
overpass_query = """
[out:json];
area["name"="Berlin"]->.searchArea;
(node["place"](area.searchArea););
out body;
"""

# Send request to Overpass API
response = requests.get(overpass_url, params={'data': overpass_query})

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # List to store data
    places_data = []

    # Loop through the data to extract place names and coordinates
    for element in data['elements']:
        name = element.get('tags', {}).get('name', 'N/A')
        lat = element['lat']
        lon = element['lon']
        places_data.append([name, lat, lon])

    # Print the results
    if places_data:
        for place in places_data:
            print(f"Place: {place[0]}, Latitude: {place[1]}, Longitude: {place[2]}")
    else:
        print("No places found for the query.")
else:
    print(f"Error: Unable to fetch data from Overpass API (Status Code: {response.status_code})")
