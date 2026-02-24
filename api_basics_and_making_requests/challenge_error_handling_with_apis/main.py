import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    # Write your code here
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()['fact']
            response.raise_for_status()
            data = response.json()['fact']
            print(data)
        else:
            print('Failed to retrieve cat fact.')
    except Exception:
            print('Failed to retrieve cat fact.')

get_cat_fact()
