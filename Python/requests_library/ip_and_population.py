import requests

ip_addr = requests.get('https://httpbin.org/ip')
population = requests.get('https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.json')

print "Database connection HTTP Status Code:", population.status_code
print('Your IP address is {0}'.format(ip_addr.json()['origin']) + "\n")

title = population.json()['meta']['view']['columns'][12]['name']

print('The database is {0}'.format(population.json()['meta']['view']['name']) + " in New York City")
print('The query is ' + title)
print('The ZIP code is {0}'.format(population.json()['data'][18][8]))
print('The ' + title + ' amount is ' '{0}'.format(population.json()['data'][18][4]))