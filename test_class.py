from tweepy import Client

from credentials import BEARER_TOKEN
from credentials import API_KEY
from credentials import API_KEY_SECRET
from credentials import ACCESS_TOKEN
from credentials import ACCESS_TOKEN_SECRET

from utils import get_regions_from_country
from utils import get_sub_regions_from_country_region

BOT_USERNAME = "CovidIncidencia"


class TestClass:
    test_country = "Spain"
    test_region = "andalucia"
    test_regions = ["Ceuta", "Castilla-La Mancha", "Madrid", "Castilla y León", "Asturias", "Galicia", "Melilla",
                    "Murcia", "Canarias", "Baleares", "C. Valenciana", "Extremadura", "Cantabria", "Cataluña", "Aragón",
                    "País Vasco", "Andalucía", "La Rioja", "Navarra"]
    test_sub_regions = ["Almería", "Cádiz", "Córdoba", "Granada", "Huelva", "Jaén", "Málaga", "Sevilla"]

    def test_tweepy_authentication(self) -> None:
        client = Client(bearer_token=BEARER_TOKEN,
                        consumer_key=API_KEY,
                        consumer_secret=API_KEY_SECRET,
                        access_token=ACCESS_TOKEN,
                        access_token_secret=ACCESS_TOKEN_SECRET)

        assert BOT_USERNAME == client.get_me().data.username

    def test_get_regions(self) -> None:
        assert self.test_regions == get_regions_from_country(self.test_country)

    def test_get_subregions(self) -> None:
        assert self.test_sub_regions == get_sub_regions_from_country_region(self.test_country, self.test_region)
