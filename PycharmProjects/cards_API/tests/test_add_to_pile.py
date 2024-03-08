import json
from unittest import TestCase

from infra.api_wrapper import APIWrapper
from logic.Brand_new_deck import BrandNewDeck
from logic.adding_to_pile import AddToPile
from logic.draw_a_card import CardsAPI


class TestAddToPile(TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        config_path = '../config.json'
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)
        self.deck_url = self.config["new_deck"]
        self.new_deck = BrandNewDeck(self.my_api, self.deck_url)
        self.new_deck.create_brand_new_deck()
        self.deck_id = self.new_deck.flow_create_new_deck_return_id()
        self.new_deck.get_updated_remaining_cards()
        self.pile_name = self.config["pile_name"]
        self.add_to_pile = AddToPile(self.my_api, self.new_deck.new_url, self.deck_id,self.pile_name)
        self.draw_cards=CardsAPI(self.my_api,self.new_deck.new_url,self.deck_id)
        self.draw_cards.draw_a_card(3)
        self.list_of_cards = self.draw_cards.get_cards_drawn_codes()
        self.add_to_pile.add_to_pile(self.list_of_cards)

    def test_add_to_pile(self):
        self.add_to_pile.get_remaining_cards_in_current_pile()
        remaining_cards_in_pile=self.add_to_pile.remaining_cards_in_pile
        self.assertEqual(len(self.list_of_cards),remaining_cards_in_pile)

    def test_add_to_pile_remaining_in_deck(self ):
        remaining_crads_in_deck_before = self.new_deck.get_deck_remaining_cards()
        remaining_crads_in_deck_after=self.add_to_pile.get_remaining_cards_in_deck(self.new_deck)
        self.assertEqual(remaining_crads_in_deck_before-len(self.list_of_cards), remaining_crads_in_deck_after)

