# 7. Python + Redis + Django


## Modyfikacje:
- Dodano licznik wejść.
- Licznik ma ustawiony czas na 1-minutę, zamiast 1 dnia.


## Ćwiczenia z redis'em

W celu sprawdzenia połączenia z redisem stosuje się metodę ping().

![](md_files/zadania/zad1.png) 

rpush(nazwaListy,*values) ➔ wrzuca po kolei wartości na koniec listy.

lrange(nazwaListy,startPos,endPos) ➔ pobiera wartości od lewej strony. endPos = -1 mówi `zabierz wszystkie wartości - do końca listy`

![](md_files/zadania/zad_2_python.png) 

Widok w bazie danych.

![](md_files/zadania/zad_2_db.png) 

lrange ➔ w tym przypadku wybierane sa wartości od elementu 1 (indexowanie startuje od 0), 3 kolejne elementy.

![](md_files/zadania/zad3.png) 

set(key,value) ➔ przypisuje kluczom podane wartości.
![](md_files/zadania/zad4.png) 

Podgląd bazy DB0

![](md_files/zadania/zad_4_db0.png) 

Podgląd bazy DB1, brak klucza 'key', ponieważ konstruktor domyślnie łączy z baza DB0. Tam wlasnie był utworzony klucz.
pełen konstruktor ➔ Redis(host, port, db)

![](md_files/zadania/zad_4_db1.png) 

setex(name, time, value) ➔ przypisuje wartość do klucza, lecz w raz z wygaśnięciem czasu klucz znika.

set(name, value)  oraz expire(name, time) ➔ powyższa funkcja to ich złożenie.
![](md_files/zadania/zad5.png) 

sadd(name, *values) ➔ dodaje wartości do zbioru, reprezentowanego przez wskazany klucz 

smembers(name) ➔ zwraca wszystkie wartości przypisane do klucza.

![](md_files/zadania/zad6.png) 

sadd(name, *values) ➔ dodaje wartości do zbioru, reprezentowanego przez wskazany klucz

zrange(name, start, end) ➔ zwraca część posortowanej kolekcji, end = -1 oznacza `aż do konca.` 

![](md_files/zadania/zad7.png) 

hset(name, key, value) ➔ przypisuje wartości do klucza, brak możliwości dodania 2 wartości do tego samego klucza. (relacja 1==1)

![](md_files/zadania/zad8.png) 

Widok w bazie danych.

![](md_files/zadania/zad8db.png) 

pubsub(**kwargs) ➔ zwraca publikujący/subskrybujacy objekt, można zasubskrybować kanał, aby nasłuchiwać na wiadomości wrzucone do kanału.
listen() ➔ nasłuchuje na wiadomość, po otrzymaniu zwraca.
![](md_files/zadania/zad9.png) 

psubscribe(*args,**kwargs) ➔ pattern subsciribe, oznacza że wiadomości będziemy odbierać, gdy nazwa kanału będzie pasowała do podanego wzoru.
![](md_files/zadania/zad10.png) 



## Poniżej przedstawiam osiągnięte efekty:


Ręczne dodanie zadania.
![](md_files/task_view.png) 


Widok przygotowanej strony.
![](md_files/page.png) 

Wybór pliku do wytworzenia miniaturki.
![](md_files/wybor_pliku.png) 

Widok ruchu po stronie serwera.
![](md_files/consolelog.png) 

Przesłany kompresowany plik trafia do /media/images.

![](md_files/zip.png) 

Wypakowane pliki: 

![](md_files/wypakowac.png) 

Porównanie wypakowanych zdjęć.
![](md_files/bothimg.png) 