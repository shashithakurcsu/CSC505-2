import requests

def get_people_in_space():
  
    api_url = 'http://api.open-notify.org/astros.json'
    
    try:
        response = requests.get(api_url)
        data = response.json()
        
        # Check if the API returned an error
        if response.status_code != 200 or 'people' not in data:
            print("Error fetching data from the API.")
            return
        
        number_of_people = data['number']
        people = data['people']
        
        print(f"Total number of people in space: {number_of_people}\n")
        print("Names of people currently in space:")
        for person in people:
            print(f"- {person['name']} on the {person['craft']}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    get_people_in_space()
