
# Phone Number Geolocation 

This project allows you to determine the country and service provider of a given phone number, convert the location to geographic coordinates using the OpenCage Geocode API, and visualize this location on a map using `folium`.

 Features

- Phone Number Parsing: Extracts the country and service provider associated with a phone number.
- Geocoding: Converts the location to latitude and longitude using the OpenCage Geocode API.
- Map Visualization: Generates an interactive map displaying the location.

 Prerequisites

Before running the project, ensure that you have the following:

- Python 3.x installed.
- OpenCage API Key: Sign up for an API key at [OpenCage Geocoder](https://opencagedata.com/).

 Installation

# Step 1: Install Required Libraries

Ensure you have `pip` installed, then run the following command to install the necessary libraries:

pip install phonenumbers folium opencage

Alternatively, create a `requirements.txt` file:

phonenumbers==8.12.34
folium==0.14.0
opencage==2.0.0


# Step 2: Set Up the Project

1. Open the `geolocation.py` file in your preferred text editor.
2. Replace the placeholder phone number with the actual phone number you want to analyze:

   number = "+1234567890"

3. Replace the placeholder API key with your OpenCage API key:

   key = "your_opencage_api_key"

 Usage

Run the script using Python:

python geolocation.py

# Example Output

The script will output:

Country: United States
Service Provider: AT&T
Latitude: 37.7749
Longitude: -122.4194

Additionally, an HTML file named `mylocation.html` will be generated in the project directory. Open this file in your web browser to view the map.

 Detailed Explanation

1. Phone Number Parsing:
   - The `phonenumbers` library is used to parse the phone number and extract the country and service provider information.

2. Geocoding:
   - The country name is passed to the OpenCage Geocode API to retrieve the geographic coordinates (latitude and longitude).

3. Map Visualization:
   - The coordinates are used to generate an interactive map with a marker at the specified location using `folium`.
