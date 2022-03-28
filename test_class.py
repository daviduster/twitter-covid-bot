import requests
import json

from tweepy import Client

from credentials import BEARER_TOKEN
from credentials import API_KEY
from credentials import API_KEY_SECRET
from credentials import ACCESS_TOKEN
from credentials import ACCESS_TOKEN_SECRET

from constants import BOT_USERNAME
from constants import COVID_DATA_API_URL
from constants import REGIONS
from constants import ANDALUCIA_SUB_REGIONS
from constants import COUNTRY

ANDALUCIA_REGION = "andalucia"


class TestClass:

    def test_tweepy_authentication(self) -> None:
        client = Client(bearer_token=BEARER_TOKEN,
                        consumer_key=API_KEY,
                        consumer_secret=API_KEY_SECRET,
                        access_token=ACCESS_TOKEN,
                        access_token_secret=ACCESS_TOKEN_SECRET)

        assert BOT_USERNAME == client.get_me().data.username

    def test_get_regions(self) -> None:
        r = requests.get(f"{COVID_DATA_API_URL}/countries/{COUNTRY}/regions")
        regions = []
        data = json.loads(r.text)

        assert len(data.get('countries')[0].get(COUNTRY)) != 0
        for e in data.get('countries')[0].get(COUNTRY):
            regions.append(e.get("name"))
        assert REGIONS == regions

    def test_get_subregions(self) -> None:
        r = requests.get(f"{COVID_DATA_API_URL}/countries/{COUNTRY}/regions/{ANDALUCIA_REGION}/sub_regions")
        sub_regions = []
        data = json.loads(r.text)
        assert len(data.get('countries')[0].get(COUNTRY).get(ANDALUCIA_REGION)[0])
        for e in data.get('countries')[0].get(COUNTRY).get(ANDALUCIA_REGION):
            sub_regions.append(e.get("name"))
        assert ANDALUCIA_SUB_REGIONS == sub_regions

    def test_get_covid_data(self) -> None:
        date = "2022-03-22"
        sub_region = "granada"

        r = requests.get(
            f"{COVID_DATA_API_URL}{date}/country/{COUNTRY}/region/{ANDALUCIA_REGION}/sub_region/{sub_region}")
        data = json.loads(r.text)

        assert data.get("dates").get(date).get("countries").get("Spain").get("regions")[0].get("sub_regions")[0] != 0
