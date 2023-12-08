import requests

params = {'ll': "40.7,-74", "query": "tacos"}
params_three = {'ll': "40.7,-74", "query": "tacos",'radius':"10"}
restaurant_id = "5b2932a0f5e9d70039787cf2"
headers = {
    "accept": "application/json",
    "Authorization": "fsq3Zl84MfhLUyF1GVvjxwwUqCk/Tw3l8fFd39N3zsz7hQE="
}
venue = {
  "fsq_id": "5b2932a0f5e9d70039787cf2",
  "categories": [
    {
      "id": 13306,
      "name": "Taco Restaurant",
      "short_name": "Tacos",
      "plural_name": "Taco Restaurants",
      "icon": {
        "prefix": "https://ss3.4sqi.net/img/categories_v2/food/taco_",
        "suffix": ".png"
      }
    }
  ],
  "chains": [],
  "closed_bucket": "LikelyOpen",
  "geocodes": {
    "drop_off": {
      "latitude": 40.702449,
      "longitude": -73.987411
    },
    "main": {
      "latitude": 40.702573,
      "longitude": -73.987408
    },
    "roof": {
      "latitude": 40.702573,
      "longitude": -73.987408
    }
  },
  "link": "/v3/places/5b2932a0f5e9d70039787cf2",
  "location": {
    "address": "141 Front St",
    "census_block": "360470021002009",
    "country": "US",
    "cross_street": "Pearl St",
    "dma": "New York",
    "formatted_address": "141 Front St (Pearl St), New York, NY 11201",
    "locality": "New York",
    "postcode": "11201",
    "region": "NY"
  },
  "name": "Los Tacos Al Pastor",
  "related_places": {},
  "timezone": "America/New_York"
}

def params_string(params:dict) -> str:
    params_list = []
    for k,v in params.items():
        params_list.append(f"{k}={v}")
    query = ("&").join(params_list)
    full_query = f"&{query}"
    return full_query

def extract_details_from_venue(venue:dict) -> dict:
    details = {}
    #fsq_id, name, location
    #location coordinates data struct is dict -> geocodes dict -> main dict
    coordinates = venue["geocodes"]["main"]
    #print(coordinates)
    locations = []
    for k,v in coordinates.items():
        locations.append(v)
    details["id"] = venue["fsq_id"]
    details["name"] = venue["name"]
    details["location"] = locations
    return details
    #print(locations)
    #return(details)

#print(extract_details_from_venue(venue))
#print(params_string(params))

def get_details(restaurant_id: str, auth: dict) -> dict:
    root_url = 'https://api.foursquare.com/v3/places/'
    full_url = f"{root_url}{restaurant_id}"
    response = requests.get(full_url, headers=headers)
    venue = response.json()
    return extract_details_from_venue(venue)
print(get_details(restaurant_id,headers))




