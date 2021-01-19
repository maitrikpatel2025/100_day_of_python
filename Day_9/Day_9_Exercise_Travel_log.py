travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_name,no_visit,cities_visited):
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = no_visit
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
    print(f"You've visited {cities_visited} {no_visit} times.")
    print(f"You've been to {cities_visited[0]}, {cities_visited[1]}")



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
