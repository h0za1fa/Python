travel_log=[
    {
        'name': 'France',
        'visits': 12,
        'cities': ['Paris','lille','Dijon'],
    },
    {
        'name': 'Germany',
        'visits': 23,
        'cities': ['Berlin','Hamburg','Stuttgart'],
    }
]

def add_country(country, visits, cities):
    new_country = {}
    new_country['name'] = country
    new_country['visits'] = visits
    new_country['cities'] = cities
    return new_country

country = input('Enter country name: ')
visits = int(input('How many visits: '))
cities = input('Cities you visited: ').split()
travel_log.append(add_country(country, visits, cities))

print(travel_log)
