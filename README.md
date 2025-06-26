Decodes a secret message from a shared Google Doc. The doc is a list of Unicode characters with an x and y coordinate.
This code grabs and parses the HTML, places characters in their position in a 2D grid, and then prints the result - revealing
a hidden ASCII message when viewed in a fixed-width font.

Tools:
- Python
- requests for fetching the document
- BeautifulSoup for parsing the HTML
- Grid building with loops

The data is parsed from the HTML by extracting all the text within <p>, <div>, and <span> elements and then searching for wanted
data with regular expressions.
