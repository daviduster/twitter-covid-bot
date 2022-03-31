import requests
import json

COVID_API_BASE_URL = "https://api.covid19tracking.narrativa.com/api/"


def get_regions_from_country(country: str) -> list:
    regions = []
    country = country.lower()

    response = __covid_api_request(f"/countries/{country}/regions")
    country_to_regions = __get_countries_from_response(response).get(country)

    if len(country_to_regions) != 0:
        for region in country_to_regions:
            regions.append(region.get("name"))

    return regions


def get_sub_regions_from_country_region(country: str, region: str) -> list:
    sub_regions = []
    country = country.lower()
    region = region.lower()

    response = __covid_api_request(f"/countries/{country}/regions/{region}/sub_regions")
    region_to_sub_regions = __get_countries_from_response(response).get(country).get(region)

    if len(region_to_sub_regions) != 0:
        for sub_region in region_to_sub_regions:
            sub_regions.append(sub_region.get("name"))

    return sub_regions


def __get_countries_from_response(response: requests.Response) -> dict:
    return json.loads(response.text).get("countries")[0]


def __covid_api_request(url: str) -> requests.Response:
    try:
        response = requests.get(f"{COVID_API_BASE_URL}{url}")
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)

    return response
