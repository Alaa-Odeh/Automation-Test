import json
from unittest import TestCase

from infra.api_wrapper import APIWrapper
from logic.shuffle_the_cards import ShuffleCards


class TestShuffleCards(TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        config_path = '../config.json'
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)
        self.url=self.config["Shuffle_the_cards"]
        self.deck_id = "jhtoyu7oqdb7"
        self.shuffle_deck = ShuffleCards(self.my_api, self.url,self.deck_id)

    def test_shuffle_cards(self):
        self.shuffle_deck.shuffle_the_cards()
        deck_shuffle_status=self.shuffle_deck.get_deck_shuffled()
        self.assertTrue(deck_shuffle_status)