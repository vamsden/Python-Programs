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

soup = BeautifulSoup(html_doc, "html.parser")

# creates a list of content within the title tag
title_cont = soup.title
print(title_cont.contents)

body_tag = soup.body

for i in body_tag.children:  # body_tag.children
    print(i)

print("------------------------------------------------------------------")
print("------------------------------------------------------------------")

for i in body_tag.descendants:
    print(i)

# string function
head_tag = soup.head
print(head_tag.string)

# Goes one up the level
print(head_tag.string.parent)
