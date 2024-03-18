Cards API Automation Testing Project
This project is an automation suite for a Cards API that allows users to interact with a virtual deck of cards. It includes functionalities to create a new deck, draw cards, add cards to piles, shuffle the deck, and list cards within piles. The automation is achieved using a series of Python scripts and an API wrapper around the Cards API.

Project Structure
The project is divided into the following directories and key files:

infra:

api_wrapper.py: Contains the APIWrapper class that handles API requests.
logic:

Brand_new_deck.py: Script to create a new deck.
draw_a_card.py: Script to draw cards from the deck.
adding_to_pile.py: Script to add cards to a pile.
drawing_from_piles.py: Script for drawing cards from piles.
listing_cards_in_piles.py: Script to list cards in a pile.
shuffle_the_cards.py: Script to shuffle the cards in the deck.
tests:

test_brand_new_deck.py: Tests the creation of a new deck.
test_draw_a_card.py: Tests drawing a card from the deck.
test_add_to_pile.py: Tests adding cards to a pile.
test_pile_listing.py: Tests listing cards in a pile.
test_shuffle_cards.py: Tests shuffling the cards in the deck.
config.json: Configuration file for the API endpoints and other settings.

Prerequisites
Python 3.6+
Requests library for Python
Installation
Clone this repository to your local machine.

Install the required Python dependencies:

sh
Copy code
pip install requests
Configure the config.json file with your specific API endpoints and any required parameters.

Running Tests
To run the tests, navigate to the root directory of the project and use the following command:

sh
Copy code
python -m unittest discover -s tests
This will discover all test cases in the tests directory and execute them.
