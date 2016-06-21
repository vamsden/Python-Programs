from bs4 import BeautifulSoup

html_doc = """
    <HTML>
    <HEAD>
    <TITLE>Your Title Here</TITLE>
    </HEAD>
    <BODY BGCOLOR="FFFFFF">
    <CENTER><IMG SRC="clouds.jpg" ALIGN="BOTTOM"> </CENTER>
    <HR>
    <a href="http://somegreatsite.com">Link Name</a>
    is a link to another nifty site
    <H1 id="red">This is a Header</H1>
    <H2 id="blue">This is a Medium Header</H2>
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

# Checks the html code and corrects any errors in the code.
soup = BeautifulSoup(html_doc, 'html.parser')
# prettifies html code
print(soup.prettify())

# Looks for title tag within the document.
print("************************")
print(soup.title)
print(soup.body.h1)

# Finds all a tags and they can accessed like an list.
a = soup.find_all("a")
a[0]
a[1]

print("************************")
print(a)
print(a[0])

# Get contents from the file
print("<---------Contents--------->")
b = soup.h2
print(b.contents)
