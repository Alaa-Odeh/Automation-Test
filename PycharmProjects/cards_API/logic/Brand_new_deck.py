class BrandNewDeck:
    def __init__(self,api_object,url):
        self.api_object = api_object
        self.new_url = url+"new/"

    def create_brand_new_deck(self,deck_count=1):
        if deck_count != 1:
            self.new_url =self.new_url +"?deck_count="+str(deck_count)
        response = self.api_object.api_get_request(self.new_url)
        self.result= response.json()

    def get_deck_id(self):
        return self.result['deck_id']

    def get_deck_remaining_cards(self):
        return self.result['remaining']

    def flow_create_new_deck_return_id(self):
        self.create_brand_new_deck()
        return self.get_deck_id()

    def get_updated_remaining_cards(self):
        self.new_url=self.new_url.replace("new",str(self.get_deck_id()))
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()
        return self.get_deck_remaining_cards()