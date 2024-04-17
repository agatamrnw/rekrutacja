Ten skrypt na bieżąco sprawdza zawartość folderu wejściowego, dokonująć konwersję plików JSON do formatu XML.
W razie błędów pliki się przemieszczają do folderu "errors". Jeżeli plik nie jest na razie w całości zapisany, wyświetla się komunikat o tym.
Jeżeli folder wejściowy jest pusty, użytkownik dostaje pytanie o zakończeniu działania programu.

Odpowiedź odnośnie umieszczania i uruchamiania danego skryptu:
    *Skrypt można uruchomić jako usługę systemową lub w tle jako proces demon.
    *Można również skonfigurować harmonogram zadania, który regularnie uruchamia skrypt w określonych interwałach czasowych.
    *Trzeba się upewnić, że foldery wejściowy i wyjściowy są odpowiednio skonfigurowane z odpowiednimi uprawnieniami dostępu dla użytkownika uruchamiającego skrypt.
    *Można również zabezpieczyć skrypt poprzez dodanie logiki autoryzacji, jeśli to jest potrzebne.