import json
from unittest import TestCase

from infra.api_wrapper import APIWrapper
from logic.Brand_new_deck import BrandNewDeck
from logic.draw_a_card import CardsAPI


class TestDrawACard(TestCase):
    def setUp(self) :
        self.my_api = APIWrapper()
        config_path = '../config.json'
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)
        self.deck_url= self.config["new_deck"]
        self.new_deck = BrandNewDeck(self.my_api,self.deck_url)
        self.new_deck.create_brand_new_deck()
        self.deck_id=self.new_deck.flow_create_new_deck_return_id()
        self.draw_cards=CardsAPI(self.my_api,self.new_deck.new_url,self.deck_id)
        print(self.deck_id)

    def test_draw_a_card(self):
        self.draw_cards.draw_a_card()
        print(self.draw_cards.get_number_of_cards_drawn())
        print(self.draw_cards.get_deck_remaining_cards())
        print(self.draw_cards.get_cards_drawn_codes())
        self.assertEqual(self.draw_cards.number_of_cards_drawn,1)

    def test_draw_more_than_one_card(self,num_of_cards=3):
        self.draw_cards.draw_a_card(num_of_cards)
        self.assertEqual(self.draw_cards.number_of_cards_drawn,num_of_cards)

    def test_remaining_cards_in_deck(self,num_of_cards=3):
        self.draw_cards.draw_a_card(num_of_cards)
        remaining_cards_in_deck=self.new_deck.get_updated_remaining_cards()
        remaining_cards=self.draw_cards.get_deck_remaining_cards()
        self.assertEqual(remaining_cards,remaining_cards_in_deck)