import requests
from bs4 import BeautifulSoup
import csv
import re;
# krótki wstęp do web scrapingu z Pythonem,
# krótki wstęp do web scrapingu z BS4,
# Beautiful Soup,
# XPath i lxml,
# implementacja wyszukiwania elementów do scrapowania za pomocą formularza w Django,
# należy przeanalizować i wdrożyć kod z repozytorium do zajęć,
# plusy za własne przemyślenia, analizę dokumentacji i idące za nimi modyfikacje w projekcie.




################################# 4-web-scraping-example4.py #############################################

# page = requests.get(
#     "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"
# )
# soup = BeautifulSoup(page.content, "html.parser")

# # Create all_h1_tags as empty list
# all_h1_tags = []

# # Set all_h1_tags to all h1 tags of the soup
# for element in soup.select("h1"):
#     all_h1_tags.append(element.text) # there is only 2 elements.

# # Create seventh_p_text and set it to 7th p element text of the page
# seventh_p_text = soup.select("p")[6].text # returns '7 reviews'

# print(all_h1_tags, seventh_p_text)  

################################# 4-web-scraping-example5.py #############################################

# #Make a request
# page = requests.get(
#     "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"
# )
# soup = BeautifulSoup(page.content, "html.parser")

# # Create top_items as empty list
# top_items = []

# # Extract and store in top_items according to instructions on the left
# products = soup.select("div.thumbnail") # wybierz wszystkie div-y z przypisana klasa 'thumbnail'
# print("Liczba top items = ", len(products))
# for elem in products:
#     title = elem.select("h4 > a.title")[0].text
#     # DOCS
#     # It is called as element > element selector. 
#     # It is also known as the child combinator selector which means that it selects only those elements which are direct children of a parent. 
#     # Elements which are not the direct child of the specified parent is not selected.
#     # ZATEM. wybieramy  wszystkie elemenety 'a' z przypisana klasa title, takie które znajdują się w wewnątrz znacznika h4, 
#     # znacznik h4 jest bezposrednim rodzicem dla znaczkina 'a'
#     review_label = elem.select("div.ratings")[0].text # wszystkie div'y z przypisana klasa 'ratings'
#     info = {"title": title.strip(), "review": review_label.strip()} # strip returns a copy of the string with both leading and trailing characters removed
#     """
#     string.strip([chars])
#     Parameter: 
#     There is only one optional parameter in it:
#     1)chars - a string specifying 
#     the set of characters to be removed. 
#     """
#     top_items.append(info)

# print(top_items)


################################# 4-web-scraping-example6.py #############################################


# # Make a request
# page = requests.get(
#     "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"
# )
# soup = BeautifulSoup(page.content, "html.parser")

# # Create top_items as empty list
# image_data = []

# # Extract and store in top_items according to instructions on the left
# images = soup.select("img")
# print("Liczba obrazków =", len(images))
# for image in images:
#     # print(type(image))
#     src = image.get("src")
#     alt = image.get("alt")
#     image_data.append({"src": src, "alt": alt})

# print(image_data) # ten przykład jest zbyt prosty aby cokolwiek opisywać.

################################# 4-web-scraping-example6_lab.py  #############################################


# # Make a request
# page = requests.get(
#     "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"
# )
# soup = BeautifulSoup(page.content, "html.parser")

# # Create top_items as empty list
# all_links = []

# # Extract and store in top_items according to instructions on the left
# links = soup.select("a")
# print("Liczba linków = ", len(links))
# for ahref in links:
#     text = ahref.text # wybiera text pomiedzy znaczkikami 'a'
#     text = text.strip() if text is not None else ""  # returns  copy of text, after whitespace removing, if text != None, else returns string.empty
#     href = ahref.get("href")
#     href = href.strip() if href is not None else ""
#     all_links.append({"href": href, "text": text})

# print(all_links)

################################# 4-web-scraping-example7.py  #############################################



# # Make a request
# page = requests.get(
#     "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
# soup = BeautifulSoup(page.content, 'html.parser')

# # Create top_items as empty list
# all_products = []

# # Extract and store in top_items according to instructions on the left
# products = soup.select('div.thumbnail')
# for product in products:
#     name = product.select('h4 > a')[0].text.strip().replace("\"","") # wybierz element 'a' taki który jest rodzicem 'h4', potem wez element 'a' pod idx[0], wybierz text tego elementu i wykonaj func strip() 
#     description = product.select('p.description')[0].text.strip() #.replace("\"","").replace(",",'').replace('\t','').replace('\n','') 
#     description = re.sub("[\n\t.,\"]","",description)
#     # wybierz elementy p taki który ma przypisana klase 'descrption', potem wez element 'p' z pod idx[0], wybierz text tego elementu i wykonaj func strip()
#     price = product.select('h4.price')[0].text.strip().replace("\"","")# 'h4' z klasa 'price'
#     reviews = product.select('div.ratings')[0].text.strip().replace("\"","") # 'div' z klasa 'ratings'
#     image = product.select('img')[0].get('src').replace("\"","") # wybierz wszystkie znaczniki 'img', wez ten o idx[0]. wybierz z tego elementu atrybut 'src' -> konkretnie  wartość  klucza 'src'

#     all_products.append({
#         "name": name,
#         "description": description,
#         "price": price,
#         "reviews": reviews,
#         "image": image
#     })


# keys = all_products[0].keys()
# print("keys = ", keys)
# print("\nvalues = ",all_products)

# with open('products.csv', 'w', newline='') as output_file:
#     # DOCS
#     # If newline is '', no translation takes place.
#     # if newline is None, any '\n' characters written are translated to the system default line separator, os.linesep
#     # os.linesep
#     # The string used to separate (or, rather, terminate) lines on the current platform. 
#     # This may be a single character, such as '\n' for POSIX, or multiple characters, for example, '\r\n' for Windows.
#     #  Do not use os.linesep as a line terminator when writing files opened in text mode (the default); use a single '\n' instead, on all platforms.
#     dict_writer = csv.DictWriter(output_file, keys,dialect='excel')
#     dict_writer.writeheader()
#     dict_writer.writerows(all_products)


################################# 4-web-scraping-part1.py #############################################


print('---------------------------- Test 1 ------------------------------------\n')
odpowiedz = requests.get("https://pl.wikipedia.org/wiki/Zygmunt_III_Waza")
print("odpowiedź = \n", odpowiedz)
print(odpowiedz.status_code)
html_text: str = odpowiedz.text # str <-- cast to string type.
print("Strona o Wazie = \n", html_text[0:30]) # wyswietl 1-szych 30 znaków 
print('---------------------------- Test 2 ------------------------------------\n')
user1 = requests.get("https://jsonplaceholder.typicode.com/users/1")
json_text: dict = user1.json()
print("url = ", user1.url)
print("json_text = ", json_text)
print("history = ", user1.history) #  We can use the history property of the Response object to track redirection.

# The Response.history list contains the Response objects that were created in order to complete the request. The list is sorted from the oldest to the most recent response.
# For example, GitHub redirects all HTTP requests to HTTPS:
# >>> r = requests.get('http://github.com/')
# >>> r.url
# 'https://github.com/'
# >>> r.status_code
# 200
# >>> r.history
# [<Response [301]>]
# prevent redirections = requests.get('http://github.com/', allow_redirects=False)
print('---------------------------- Test 3 ------------------------------------\n')
html_doc = """<html>
<head>
    <title>Moja pierwsza strona!</title>
</head>
<body>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec posuere elit at malesuada tempor. Donec eget ligula in ante auctor luctus. Phasellus iaculis porttitor gravida. Donec eget sem lorem. Morbi a libero imperdiet, viverra tellus ac, consequat tortor. Suspendisse nibh massa, accumsan non neque a, vestibulum commodo dui.</p>
<p>Phasellus vestibulum ut <br>erat sit amet ullamcorper. Nam at elit feugiat, dapibus ante vitae, ullamcorper dui. Nunc rutrum at nibh tincidunt mattis. In finibus sed ante vel mollis. Donec at semper metus. Aenean quis consectetur risus. Sed suscipit felis sed ex pretium euismod. In fermentum mi a odio porttitor, dapibus aliquet leo accumsan. Suspendisse pretium augue et faucibus euismod. Quisque risus metus, ultricies nec tortor at, efficitur convallis nunc.</p>
<ul>
    <li>Pierwszy punkt</li>
    <li>Drugi punkt</li>
    <li>Trzeci punkt</li>
</ul>
<ol>
    <li>Pierwszy punkt</li>
    <li>Drugi punkt</li>
    <li>Trzeci punkt</li>
</ol>
<table border="3" bgcolor="#ff00ff" class="tabela blog">
    <tr><th>Naglowek 1</th><th>Naglowek 2</th></tr>
    <tr><td>komorka 11</td><td>komorka 12</td></tr>
    <tr><td>komorka 21</td><td>komorka 22</td></tr>
</table>
<a href="http://google.pl">Arcyciekawa strona</a>
</body>
</html>"""

url_amw = "https://www.amw.gdynia.pl/"
# page = requests.get(url_amw)
# soup = BeautifulSoup(page.content, "html.parser")
soup = BeautifulSoup(html_doc, "lxml") # lxml ne jest domyslnie zainstalowany

# Extract head of page
page_head = soup.head
print("Typ = ", type(page_head))

first_p = soup.select("p")[0].text
print("First p =\n", first_p)

another_p = soup.select("p")[1].text
print("Another p =\n", another_p)

print("Liczba zanaczników 'p' = ", len(soup.select("p")))

# title
print("TITLE")
print(soup.title) # returns  '<title>Moja pierwsza strona!</title>'
print(soup.title.name) # returns 'title'
print(soup.title.string) #  ret 'Moja pierwsza strona!'
print(soup.title.text) # ret 'Moja pierwsza strona!'
print(soup.title.contents[0]) # array of string, with 'Moja pierwsza strona!' at idx 0.


# ul
print("UL")
print(soup.ul.text) # returns text from all childs <li> elements 
print("\n")


# atrybuty
print("ATRYBUTY")
print(soup.table["border"]) # returns 3 because atribute 'border' in table elelement is set to 3.
print(soup.table.has_attr("border")) #  true, no jasna sprawa
print(soup.table.has_attr("href")) # false ... tez.
print(soup.table.attrs) # returns key value pair, where attributes are keys, like {'border': '3', 'bgcolor': '#ff00ff', 'class': ['tabela', 'blog']}
print("\n")



