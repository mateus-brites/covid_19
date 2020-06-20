# this is a software that show the rank of covid-19 in the world
#                                        start

# libraries:
from urllib.request import urlopen
from bs4 import BeautifulSoup


# variable
website = urlopen('https://www.bbc.com/portuguese/internacional-51718755')  # website that we are using
html = BeautifulSoup(website, "html.parser")  # get the site html
countries = html.findAll("", {"aria-label":"País"})
cases = html.findAll("", {"aria-label":"Total de casos"})
death = html.findAll("", {"aria-label":"Mortes"})
n = len(countries) # Number os countries in rank

print(html.title.string)  # title of the page

# output
for i in range(0, n):
    print(f'Countrie: {countries[i].get_text().strip()}')
    print(f'Cases: {cases[i].get_text().strip()}')
    print(f'death: {death[i].get_text().strip()}')
    print('')
