class CardsAPI:
    def __init__(self,api_object ,url,deck_id):
        self.api_object = api_object
        self.new_url = url.replace("new", deck_id)+"/draw/"
        self.codes_array = []


    def draw_a_card(self,count=1):
        if count !=1:
            self.new_url=self.new_url+"?count="+str(count)
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()

    def get_number_of_cards_drawn(self):
        self.number_of_cards_drawn=len(self.result["cards"])
        return self.number_of_cards_drawn

    def get_deck_remaining_cards(self):
        return self.result['remaining']

    def get_cards_drawn_codes(self):
        for card in self.result['cards']:
            self.codes_array.append(card['code'])
        return self.codes_array
