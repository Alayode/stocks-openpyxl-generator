#  Parse a document by passing it into the BeautifulSoup Constructor
from bs4 import BeautifulSoup

with open ("sp500.html") as markup:
    soup = BeautifulSoup(markup, 'html.parser')


table = soup.find_all('tr')
print(table[0])
headerRow = table[0]
tableSoup = BeautifulSoup(str(headerRow), 'html.parser')
headers =  tableSoup.find_all('th')

# print(headers[1].getText())

# Define the Headers in table
# headers[0] '#'
# headers[1] 'Company'
# headers[3] 'Symbol'
# headers[4] 'Weight'
# headers[5] 'Price' # TODO Strip whitespace
# headers[6] 'Chg'
# headers[7] '%Chg'


# Define the content of the corresponding columns
cols = table[1]
columnSoup = BeautifulSoup(str(cols), 'html.parser')
columnsTDS =  columnSoup.find_all('td')

print(columnsTDS[1].getText())

# First Row after headers
# columnsTDS[0].getText() '1'
# columnsTDS[1].getText() 'Microsoft Corporation'
# columnsTDS[3].getText() 'MSFT'
# columnsTDS[4].getText() '5.66254'
# columnsTDS[5].getText() '  189.34' # TODO Strip whitespace
# columnsTDS[6].getText() '7.51'
# columnsTDS[7].getText() '(-3.81%)'




# bsTable = BeautifulSoup(table, 'html.parser')
# print(table[1].td , 'Number of  Company')
# print(table[1].find_all('td'))

tableStocks = table[1].find_all('td')
companies = []


# print(table[0].contents)
firstRow = table[0].contents
# print(len(firstRow[1]))
# print(firstRow)

# for row in table:

        # companies.append(row.getText())
    # for tr in row:
    #         print(
    #     tableSoup = BeautifulSoup(tr, 'html.parser')

# print(len(companies))
# print(companies[0])

# Find the table elements <table> that the stocks sit in 

