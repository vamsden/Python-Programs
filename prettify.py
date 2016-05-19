from bs4 import BeautifulSoup

soup = BeautifulSoup(
    '<html> <p> <a href="http://www.codestinger.com"> <h2> Hello-World </html>', 'html.parser'
)

print(soup.prettify())
