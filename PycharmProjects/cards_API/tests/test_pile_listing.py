import json
from unittest import TestCase

from infra.api_wrapper import APIWrapper
from logic.listing_cards_in_piles import ListingCardsInPile


class TestListingPile(TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        config_path = '../config.json'
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)
        self.url = self.config["listing_cards_in_piles"]
        self.deck_id = "jhtoyu7oqdb7"
        self.pile_name = self.config["pile_name"]
        self.listing_cards = ListingCardsInPile(self.my_api, self.url, self.deck_id,self.pile_name)


    def test_listing_cards_in_pile(self):
        self.listing_cards.listing_cards_in_pile()
        self.listing_cards.get_cards_coeds_in_pile()
        cards_list=self.listing_cards.cards_codes
        self.assertEqual(cards_list,['2H','3H'])