# import libraries
from dataclasses import dataclass
import requests  # Library for making HTTP requests
import pandas as pd  # Library for data manipulation and analysis

# Using dataclass decorator to define the FedyAPI class as a dataclass
@dataclass
class FedyAPI:
    number_of_papers: int
    search_keyword: str

    # Function to call the API and retrieve the data
    def API_Call(self):
        api_key = '790713ded66fe0dd637dd61f70925146'
        headers = {'Authorization': 'Bearer {}'.format(api_key)}  # Setting the authorization key in the headers
        search_api_url = 'https://api.springernature.com/metadata/json'  # URL for the API endpoint
        payload = {'api_key': api_key, 'q': self.search_keyword, 'p': self.number_of_papers}  # Payload for the GET \
        # request
        response = requests.get(search_api_url, headers=headers, params=payload).json()

        # Convert response to Pandas DataFrame
        return pd.DataFrame(response['records'])

    # Function for processing the data
    def Processed_Table(self):
        messy_data = self.API_Call()


class Application(FedyAPI):
    pass
