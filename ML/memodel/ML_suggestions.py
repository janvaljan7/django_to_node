# import pandas as pd 
# import numpy as np 
import requests
from django.http import HttpResponse
from rest_framework import status

def ML():
    
    # first = str(first_choice).lower()
    # second = str(second_choice).lower()
    # third = str(third_choice).lower()
    dictionary = {
        "history": "Statue of Liberty and Ellis Island\n Federal Hall\n New-York Historical Society\n",
        "kid-friendly": "Central Park (playgrounds, Central Park Zoo)\nAmerican Museum of Natural History\nBronx Zoo\n",
        "outdoors": "High Line Park\nBrooklyn Bridge Park\nGovernors Island\n",
        "art and culture": "Museum of Modern Art (MoMA)\nGuggenheim Museum\nWhitney Museum of American Art\n",
        "museums": "The Metropolitan Museum of Art\nMuseum of the City of New York\nMuseum of Natural History\n",
        "beaches": "Coney Island\nRockaway Beach\nBrighton Beach\n",
        "architercture": "Empire State Building\nFlatiron Building\nGrand Central Terminal\n",
        "food and culinary places": "Chelsea Market\nSmorgasburg (food market)\nKatz's Delicatessen\n"
    }   
    node_backend_url = "https://7bf69800-c806-4fc1-a8ca-937e2963fcd2.mock.pstmn.io"

    response = requests.get(node_backend_url)
    if response:
        data = response.json()
        
        first = str(data['first']).lower()
        # second = str(data['second']).lower()
        # third = str(data['third']).lower()
    
        result = dictionary[first]
        print(result)
        return result
    else:
        return None
        



