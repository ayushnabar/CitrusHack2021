
import requests

API_KEY = '2f82479a70b61e8898c5a891d16804bc'
APP_ID = '8520a617'

response = requests.get('https://api.edamam.com/api/nutrition-data?app_id=' + APP_ID + '&app_key=' + API_KEY + '&ingr=1%20large%20apple')
json = response.json()

def get_fat():
    return json['totalNutrients']['FAT']['quantity']
def get_protein():
    return json['totalNutrients']['PROCNT']['quantity']
def get_carbs():
    return json['totalNutrients']['CHOCDF']['quantity']



