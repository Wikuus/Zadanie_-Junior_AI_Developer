# Zadanie_rekrutacyjne-Junior_AI_Developer - Wiktoria Łazarz

W celu uruchomienia aplikacji należy zainstalować na komputerze interpreter pythona, pobierając go ze strony:
"https://www.python.org/downloads/"

Następnie trzeba wejść w terminal lub aplikację Python, przejść do folderu, gdzie znajduje się aplikacja.py i wpisać polecenie:
"python aplikacja.py"


W aplikacji znajdują się 4 funkcje (licząc z main):
-> send_prompt(prompt) - przekształca podany jako argument prompt na format JSON, konfiguruje i wysyła zapytanie do API oraz odczytuje zwróconą odpowiedź
-> read_article(file_path) - odczytuje zawartość pliku, którego ścieżkę podajemy jako argument funkcji
-> save_html(file_path, content) - zapisuje dane podane w argumencie content do pliku, którego ścieżkę z nazwą pliku podajemy w pierwszym argumencie file_path
-> main() -  odpowiada za działanie programu i wywoływanie powyższych funkcji

W funkcji main() przypisujemy wynik funkcji read_article() do zmiennej article. Następnie tworzymy zmienną prompt, do której wpisujemy zawartość zapytania, które chcemy przekazać do OpenAI. Wywołujemy funkcję send_prompt(), wpisując jako argument zmienną prompt (czyli nasze zapytanie) i przypisujemy zwróconą odpowiedź do zmiennej new_article. A teraz wpisujemy tą zmienną jako drugi argument funkcji save_html() (pierwszym jest ścieżka pliku wraz z jego nazwą). 