class AddToPile:
    def __init__(self,api_object,url,deck_id,pile_name):
        self.api_object = api_object
        self.new_url =url+"pile/"+str(pile_name)+"/add/"
        self.pile_name=pile_name


    def add_to_pile(self,cards):
        str_cards=",".join(cards)
        self.new_url = self.new_url + "?cards=" + str_cards
        print(str_cards)
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()

    def get_remaining_cards_in_deck(self,deck):
       return deck.get_updated_remaining_cards()


    def get_remaining_cards_in_current_pile(self):
        self.remaining_cards_in_pile = self.result['piles'][str(self.pile_name)]['remaining']
