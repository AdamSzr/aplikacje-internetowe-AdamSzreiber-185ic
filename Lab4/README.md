# Lab_4 REST API z DRF
##[Strona Główna](https://adam-szreiber-api.herokuapp.com/)
##[Swagger](https://adam-szreiber-api.herokuapp.com/swagger/)

### Wykorzystano:
* Python - Django
* HTML
* CSS
* Django Rest Framework
***

## Poniżej przedstawiam osiągnięte efekty:

#### Wykożysatłem 2 narzędzia do wstawiania elementów.
* za pomocą Postman'a
* za pomocą Swagger'a

#### Postman, tworzenie user'a

- w pierwszej kolejności zmieniłem verb i wpisałem url.
![](md_files/heroku/userCreateMethod.png) 

- następnie w zakładce body wrzuciłem model usera opisany w formacie json.
![](md_files/heroku/userCreateBody.png) 

- ostatnia modyfikacja to zmiana nagłówka content-type .
![](md_files/heroku/userCreateHeaders.png) 
Wyrzuciłem domyślny wpis Content-Type: text/plain, i w ostatniej lini dopisałem application/json.
Można również ten krok zrobić w zakładce body (patrz zakładka 'Body'), wybierając odpowiedni format wpisu (również jest 'json').

- Stworzenie 1 postu.
![](md_files/heroku/postCreate.png) 

#### Swagger, tworzenie user'a
- Tutaj wszystko jest 'prostsze' lecz, jest to znacznie mniej powerfull narzędzie.
- Natomiast fajną opcją jest podgląd komendy curl - kolejne bradzo popularne narzędzie do testowania aplikacji sieciowych.
![](md_files/heroku/userCreateSwagger.png) 

- Oto odpowiedź na ryc wyżej.
![](md_files/heroku/userCreateSwaggerResponse.png) 

#### Ostateczny efekt:
- 5 użytkowników
![](md_files/heroku/userCreate5Elements.png) 
- Kilka postów, które widoczne są na stronie głównej.
![](md_files/heroku/results.png) 

