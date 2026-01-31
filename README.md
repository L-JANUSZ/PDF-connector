# PDF Connector

PDF Connector to prosta i intuicyjna aplikacja do łączenia wielu plików PDF w jeden dokument. Aplikacja posiada graficzny interfejs użytkownika w języku polskim.

## ✨ Funkcje

- 📄 Łączenie wielu plików PDF w jeden dokument
- 🔄 Zmiana kolejności plików przed scaleniem
- 📁 Wygodne wybieranie plików poprzez interfejs graficzny
- 💾 Możliwość wyboru lokalizacji i nazwy pliku wynikowego
- 🎨 Intuicyjny interfejs użytkownika

## 📥 Pobieranie

Najłatwiejszy sposób na korzystanie z PDF Connector:

1. Przejdź do zakładki [Releases](https://github.com/L-JANUSZ/PDF-connector/releases) w tym repozytorium
2. Pobierz najnowszą wersję pliku `PDF_Connector.exe`
3. Zapisz plik w wybranej lokalizacji na swoim komputerze

**Alternatywnie:** Możesz również pobrać plik bezpośrednio z folderu `dist/`:
- Kliknij [tutaj](https://github.com/L-JANUSZ/PDF-connector/raw/main/dist/PDF_Connector.exe), aby pobrać `PDF_Connector.exe`

### Opcja 2: Uruchom ze źródła (wymagany Python)

Jeśli preferujesz uruchomienie z kodu źródłowego:

1. Sklonuj repozytorium:
```bash
git clone https://github.com/L-JANUSZ/PDF-connector.git
cd PDF-connector
```

2. Zainstaluj wymagane biblioteki:
```bash
pip install -r requirements.txt
```

3. Uruchom aplikację:
```bash
python pdf_connector.py
```

## 🚀 Jak używać

1. **Uruchom aplikację**
   - Kliknij dwukrotnie na plik `PDF_Connector.exe`
   - Aplikacja nie wymaga instalacji!

2. **Dodaj pliki PDF**
   - Kliknij przycisk "➕ Dodaj pliki PDF"
   - Wybierz jeden lub więcej plików PDF z dysku

3. **Uporządkuj pliki** (opcjonalnie)
   - Użyj przycisków "⬆️ Przesuń w górę" i "⬇️ Przesuń w dół" do zmiany kolejności
   - Kliknij "❌ Usuń zaznaczony", aby usunąć niepotrzebny plik

4. **Wybierz nazwę i lokalizację pliku wynikowego**
   - Wpisz nazwę w polu "Nazwa pliku wynikowego"
   - Lub kliknij "📁 Wybierz lokalizację", aby wybrać folder i nazwę

5. **Połącz pliki**
   - Kliknij "🔗 Połącz pliki PDF"
   - Gotowe! Twój nowy plik PDF został utworzony

## 💡 Wymagania

### Dla wersji .exe:
- System operacyjny: Windows 7 lub nowszy

### Dla wersji źródłowej:
- Python 3.6 lub nowszy
- Biblioteki wymienione w `requirements.txt`:
  - PyPDF2
  - tkinter (zazwyczaj dołączony do Pythona)

## 📝 Licencja

Ten projekt jest dostępny na licencji określonej przez autora.

## 👤 Autor

L-JANUSZ

## 🤝 Współpraca

Zgłoszenia błędów i propozycje ulepszeń są mile widziane! Prosimy o tworzenie issues w repozytorium GitHub.
