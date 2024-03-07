import json
import unittest
import requests
from infra.api_wrapper import APIWrapper
from logic.Brand_new_deck import BrandNewDeck


class MainTester(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        config_path = '/config.json'
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)
        self.new_deck_url=self.config["Brand_new_deck"]
        self.new_deck=BrandNewDeck(self.my_api)


    def test_check_status_code_in_houses(self):
        self.new_deck.create_brand_new_deck(self.new_deck_url)
        result =self.new_deck.result
        print(self.new_deck.get_deck_id())
        print(self.new_deck.get_deck_remaining_cards())
        self.assertEqual(result['remaining'], 52)


