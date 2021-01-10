# 10. Django + React (aplikacja typu ToDo)

- Modyfikacje jakie wprowadziłem :

<i>backend/settings.py</i>
CORS_ORIGIN_ALLOW_ALL = True

W wyżej wymienionej zmiennej deklaruję informacje, iż nie ważne z jakiego addresu przyjdzie request, zostanie on zawsze obsłużony. W dokumentacji opisali, iż definiowanie cors_all = true może być niebezpieczne, niemniej jednak aplikacja frontend miał problem aby połączyć się z backend, a jedyna opcja która działa to własnie cors_all.

Domyślnie wartość jest false, i należy zdefiniować jedną z poniższych zmiennych, która definiuje dostęp.
- CORS_ALLOWED_ORIGINS = ['',]
- CORS_ALLOWED_ORIGIN_REGEXES = ['',]




### Widok stworzonej aplikacji - backend
![](md_files/clear_backend.png) 

### Widok stworzonej aplikacji - frontend
![](md_files/clear_frontend.png) 

### Dodawanie nowego zadania - wykonanego
![](md_files/add_completed.png) 

### Widok dodanego zadania - wykonanego
![](md_files/view_completed.png) 

### Dodawanie nowego zadania - oczekującego
![](md_files/add_uncompleted.png) 

### Widok dodanego zadania - oczekujacego
![](md_files/view_uncompleted.png) 

### Dodałem jeszcze 1 wpis o tytule "ROZDZIAL III"
### Poniżej przedstawiam pełną listę zadań.
![](md_files/full_backend.png) 


### Edycja wpisu o tytule "ROZDZIAL III" na "Scena III"
![](md_files/edit.png) 

### Zmiany jakie wprowadziła edycja.
![](md_files/edited.png) 

### Usuwanie wpisu. - Sceny III
![](md_files/delete.png) 

### Widok zadań po usunięciu.
![](md_files/deleted.png) 


### Ostateczny widok listy wpisów.
![](md_files/end.png) 





