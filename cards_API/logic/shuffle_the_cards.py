


class ShuffleCards:
    def __init__(self,api_object,url,deck_id):
        self.api_object = api_object
        self.new_url = url.replace("deck_name", deck_id)

    def shuffle_the_cards(self,deck_count=1,dont_shuffle_remaining=True):
        if deck_count > 1:
            self.new_url = self.new_url + "?deck_count="+str(deck_count)
        if dont_shuffle_remaining:
            self.new_url =self.new_url + "?remaining=" + str(dont_shuffle_remaining)
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()


    def get_deck_remaining_cards(self):
        return self.result['remaining']

    def get_deck_shuffled(self):
        return self.result['shuffled']

