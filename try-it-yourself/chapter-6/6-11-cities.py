# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.

cities = {
    'Chicago': {
        'Country': 'United States'
        , 'Population': 401_002_112
        , 'Fact': 'It is my favorite city.'
    }
    , 'Atlanta': {
        'Country': 'United States'
        , 'Population': 5
        , 'Fact': 'It is my second favorite city.'
    }
    , 'New York': {
        'Country': 'United States'
        , 'Population': 500_000
        , 'Fact': 'I have not been in a while, but I may like it again.'
    }
    ,
}

for city, facts in cities.items():
    print(" - " + f"{city}" + " - ")
    # print(f"Here is a city named {city}")
    print(f"First fact is that it is in {facts.get('Country')}")
    print(f"Second fact is that it has a population of: {facts.get('Population')}")
    print(f"Random fact is: {facts.get('Fact')}")


