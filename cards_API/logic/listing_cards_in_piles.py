class ListingCardsInPile:
    def __init__(self,api_object,url,deck_id,pile_name):
        self.api_object = api_object
        self.new_url = url.replace("deck_name", deck_id).replace("pile_name", pile_name)
        self.pile_name=pile_name
        self.cards_codes=[]

    def listing_cards_in_pile(self):
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()

    def get_cards_coeds_in_pile(self):
        self.cards_codes=[card['code'] for card in self.result['piles'][str(self.pile_name)]['cards']]