#Mimick api with data locally
def get_people_in_space():

    data = {
        'number': 7,
        'people': [
            {'name': 'Sergey Prokopyev', 'craft': 'ISS'},
            {'name': 'Dmitry Petelin', 'craft': 'ISS'},
            {'name': 'Frank Rubio', 'craft': 'ISS'},
            {'name': 'Fei Junlong', 'craft': 'Tiangong'},
            {'name': 'Deng Qingming', 'craft': 'Tiangong'},
            {'name': 'Zhang Lu', 'craft': 'Tiangong'},
            {'name': 'Sultan Al Neyadi', 'craft': 'ISS'}
        ]
    }
    return data

def display_people_in_space(): 
    data = get_people_in_space()
    number_of_people = data['number']
    people = data['people']

    print(f"Total number of people in space: {number_of_people}\n")
    print("Names of people currently in space:")
    for person in people:
        print(f"- {person['name']} on the {person['craft']}")

if __name__ == '__main__':
    display_people_in_space()
