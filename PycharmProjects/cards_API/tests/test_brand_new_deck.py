import json
from unittest import TestCase

from infra.api_wrapper import APIWrapper
from logic.Brand_new_deck import BrandNewDeck


class TestBrandNewDeck(TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        config_path = '../config.json'
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)
        self.new_deck_url=self.config["new_deck"]
        self.new_deck = BrandNewDeck(self.my_api,self.new_deck_url)



    def test_check_new_deck(self):
        self.new_deck.create_brand_new_deck()
        self.result = self.new_deck.result
        self.assertEqual(self.result['remaining'], 52)

    def test_create_more_than_1_deck(self,deck_count=5):
        self.new_deck.create_brand_new_deck(deck_count)
        self.result = self.new_deck.result
        self.assertEqual(self.result['remaining'], deck_count*52)
