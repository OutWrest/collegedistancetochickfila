from scrape import Scrape

url = 'https://www.chick-fil-a.com/'
endpoint = '/locations/browse/'
state = 'al'

def parse_div(data):
    name = data.a.contents[0]
    address = ' '.join([content for i, content in enumerate([str(content).strip() for content in data.p.contents]) if i%2==0])
    
    if '(' in address:
        address = address[:address.index('(')-1]
    

    return [name, address]


sc = Scrape(url)

locations = sc.scrape(endpoint+state, 'div', attrs={'class':'location'})

scraped = [parse_div(location) for location in locations]

with open('chickfilas.txt', 'w') as f:
    for item in scraped:
        f.write("{}:{}\n".format(item[0], item[1]))