import re
from bs4 import BeautifulSoup


html_doc = """
    <HTML>
    <HEAD><TITLE>Your Title Here</TITLE></HEAD>
    <BODY BGCOLOR="FFFFFF">
    <CENTER><IMG SRC="clouds.jpg" ALIGN="BOTTOM"> </CENTER>
    <HR>
    <a href="http://somegreatsite.com">Link Name</a>
    is a link to another nifty site
    <H1 id="red">This is a Header</H1>
    <H2 class="blue">This is a Medium Header</H2>
    Send me mail at <a href="mailto:support@yourcompany.com">
    support@yourcompany.com</a>
    <P> This is a new paragraph!
    <P> <B>This is a new paragraph!</B>
    <BR> <B><I>This is a new sentence without a paragraph break, in bold
    italics.
    </I></B>
    <HR>
    </BODY>
    </HTML>
"""

soup = BeautifulSoup(html_doc, "html.parser")

# Find function
print(soup.find_all(id="red"))
print(soup.find_all(class_="blue"))
print()

for tag in soup.find_all("b"):
    print(tag.name)  # tag returns the whole body of the tag

print()
print(soup.find_all(href=re.compile("site")))
