import requests

def print_three_cat_facts():
    # Your code goes here
    for i in range(3):
        response = requests.get("https://catfact.ninja/fact")
        data = response.json()['fact']
        print(data)
    

print_three_cat_facts()
