from scrape import Scrape
import re

url = 'https://www.chick-fil-a.com/'
endpoint = '/locations/browse/'
states = []

sc = Scrape(url)

def parse_div(data):
    name = data.a.contents[0]
    address = ' '.join([content for i, content in enumerate([str(content).strip() for content in data.p.contents]) if i%2==0])
    
    if '(' in address:
        address = address[:address.index('(')-1]

    return [name, address]

def scrapeState(state):
    states.append(state)
    locations = sc.scrape(endpoint+state, 'div', attrs={'class':'location'})
    scraped = [parse_div(location) for location in locations]

    return scraped

every_chickfila_in_the_country = [scrapeState(state) for state in [re.search(r"\((.*)\)", str(state))[0].replace('(', '').replace(')', '').lower() for state in sc.scrape(endpoint, 'li') if state.a and state.a.has_attr('href') and '/locations/browse/' == state.a['href'][:len('/locations/browse/')]]]

with open('every_chickfila_in_the_country.txt', 'w') as f:
    for i, state in enumerate(every_chickfila_in_the_country):
        for store in state:
            f.write("{}:{}:{}\n".format(states[i], store[0], store[1]))