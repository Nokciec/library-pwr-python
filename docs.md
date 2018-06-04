# 1. Założenia i opis funkcjonalny programu
##### Poruszany problem:
Program będzie obsługiwał system zarządzania biblioteką.
##### Użytkownik docelowy:
Program dedykowany jest dla klientów biblioteki oraz jej pracowników.
##### Założenia:
Klientom zostanie umożliwione m. in.: rejestracja, logowanie, przeglądanie zasobów
biblioteki, rezerwacja pozycji oraz prolongowanie wypożyczonych już dzieł.
Pracownicy będą mogli wypożyczać zasoby klientom, dodawać nowe pozycje oraz usuwać istniejące. Tak jak i klienci będą mieli dostęp do rejestracji, logowania oraz katalogu bibliotek.
##### Dodatkowe założenia:
Klient będzie mógł wyświetlić swój profil, a w nim sprawdzić historię wypożyczeń, listę swoich rezerwacji, usunąć swoje konto oraz wylogować się.
##### Użyte języki, środowiska i frameworki:
- C++, Qt Creator
- Python, CSS, HTML, Jinja2, FireBase,
# 2. Diagramy UML
## a) diagram przypadków użycia
![](https://i.imgur.com/piaUrhz.png)
## b) diagram klas
do zrobienia i wklejenia
# 3. Kod klas C++
Z kodu klas zostały usunięte fragmenty dotyczące GUI.
### AddBookForm class
```c++
class addbookform : public QDialog
{
public:
    explicit addbookform(QWidget *parent = 0);
    ~addbookform();
private:
    /**
Adds a new book. It takes: title, author, ISBN number, publication date, publication place, publisher and number of pages as arguments. 
    */
    void addNewBook(QString title, QString author, QString ISBN, QString publicationDate, QString publicationPlace, QString publisher, QString pagesNumber);
};
```
### Book class
```c++
class Book
{
public:
        long m_bookID;
        std::string m_title;
        std::string m_author;
        long m_ISBN;
        int m_publicationDate;
        std::string m_publicationPlace;
        std::string m_publisher;
        int m_pagesNumber;
        bool m_availability;
        std::string m_borrowerlogin;
        QDateTime m_startdate;
        QDateTime m_enddate;
        bool m_reservation;
        std::string m_reserveLogin;
/** 
Getters
*/
        long getBookID() const { return m_bookID; }
        std::string getTitle() const {return m_title;}
        std::string getAuthor() const {return m_author;}
        long getISBN() const {return m_ISBN;}
        int getPublicationDate() const {return m_publicationDate;}
        std::string getPublicationPlace() const {return m_publicationPlace;}
        std::string getPublisher() const {return m_publisher;}
        int getPagesnumber() const {return m_pagesNumber;}
        bool getAvailability() const {return m_availability;}
        std::string getBorrowerLogin() const {return m_borrowerlogin;}
        QDateTime getStartDate() const {return m_startdate;}
        QDateTime getEndDate() const {return m_enddate;}
        bool getReservation() const {return m_reservation;}
        std::string getReserveLogin() const{return m_reserveLogin;}
        Book()=default;
/**
Creates a book given its data.
*/
        Book(long i_bookID,
             std::string i_title,
             std::string i_author,
             long i_ISBN,
             int i_publicationDate,
             std::string i_publicationPlace,
             std::string i_publisher,
             int i_pagesNumber,
             bool i_availability,
             std::string i_borrowerlogin,
             QDateTime i_startdate,
             QDateTime i_enddate,
             bool i_reservation,
             std::string i_reserveLogin);
};

```
### BookManager class
```c++
class bookmanager
{
public:
/**
Converts the raw database text data into a vector of Books.
*/
    std::vector<Book> showBooks();
/**
Loads the raw database text data.
*/
    std::vector<QString> getContent();
/**
Deletes a book given its row.
*/
    void deleteBook(int row);
    
/**
Rents a book given its row and reservers login.
*/
    void rentABook(int row, QString login);
    
/**
Reserves a book given its row and reservers login.
*/
    void reserveABook(int row, QString login);
    
/**
Renews a book given its row
*/
    void renewABook (int row);
};
```

### LoginManager class
```c++
class LoginManager : public QDialog
{
public:
/**
Helper functions
*/
    QString getLogin();
    QString getPassword();
    bool getAccess() const {return access;}
    int getPermissions() const {return permissions;}

/**
Helper variable
*/
    bool isAccepted;

    
private:
/**
Helper variables
*/
    int permissions=0;
    bool access=false;
    
/**
Verifies if password and login match. Takes login and password as arguments.
*/
    void verifyPassword(QString user_login, QString user_password);
};
```
#### MainWindow class
```c++
class MainWindow : public QMainWindow
{
public:
    LoginManager *loginmanager;
    User::Type type;
    RegisterManager *registermanager;
    addbookform *addbookdialog;
    rentbookform *rentbookdialog;
/**
Changes the users permissions.
*/
    void setTypeOfUser(int permissions);
    
/**
Contains currently selected row.
*/
    int activeRow;

/**
The following functions have self-explanatory names

To clear the confusion: they use the GUI to do their job,
so they take no arguments.
*/
    void userRegister();
    void userLogin();
    void displayBooks();
    void addBook();
    void deleteBook();
    void rentBook();
    void reserveBook();
    void renewBook();
    void logOut();
};
```
### RegisterManager class
```c++
class RegisterManager : public QDialog
{
/**
Getters
*/
    QString getLogin();
    QString getPassword();
    
/**
Safety check, used in operations on users.
*/
    bool isUserInDatabase(QString login);

private:
/**
Creates a new user. Takes login, password, name, surname and type as arguments.
*/
    void createNewUser(QString login, QString password, QString name, QString surname, QString type);
};
```
### User class
```c++
class User
{
public:
    std::string name;
    std::string surname;
    std::string login;
    std::string password;
    enum class Type
    {
        Guest,
        Client,
        Librarian
    };
    Type type;
    User();
};
```
### UserManager class
```c++
class userManager
{
public:
/**
Helper variables
*/
    bool access;
    int type;

/**
Helper functions
*/
    bool accessAccepted() const {return access;}
    int getPermissions() const{return type;}
/**
Searches user in database.
*/
    bool userSearching(std::string login, std::string password);

    userManager();
};
```
# 4. Schematy blokowe oraz kod własnych funkcji 
Poniższe schematy blokowe ukazują działanie dwóch wybranych przeze mnie funkcji. Jedna z nich jest używana do wyświetlania wszystkich książek, natomiast druga służy do rejestrowania nowego użytkownika.
|![](https://i.imgur.com/iNPPzvA.png)  |  ![](https://i.imgur.com/cnyoSMv.png)|
:-------------------------:|:-------------------------:
|Schemat blokowy funkcji showBooks           | Schemat blokowy funkcji rejestrującej użytkownika|
# 5. Opis użytkowy programu C++ 
Poruszanie się po programie jest bardzo intuicyjne. Po uruchomieniu aplikacji użytkownikowi ukazuje się menu biblioteki, w którym może się zarejestrować, zalogować lub wybrać opcje "Show Catalogue", która wyświetli tytuły wszystkich dostępnych książek. 

|![](https://i.imgur.com/BmS47tO.png)  |  ![](https://i.imgur.com/qQBTneO.png)|
:-------------------------:|:-------------------------:
|Menu główne            |   Menu po wybraniu opcji wyświetlenia katalogu|

Po wybraniu opcji rejestracji wyświetla się formularz do wypełnienia. Jeżeli rejestracji próbuje dokonać użytkownik, który istnieje już w bazie, program informuje o tym. Pozostawienie któregoś z pól pustym również wyświetla ostrzeżenie. Dodatkowym udogodnieniem, które ułatwia rejestracje jest opcja, która sprawdza czy oba podane hasła są identyczne. 

|![](https://i.imgur.com/KnS2zRj.png)  |  ![](https://i.imgur.com/2mtZ8EB.png)|
:-------------------------:|:-------------------------:
|Menu rejestracji            |   Panel rejestracyjny z przykładowymi danymi|

Po wybraniu opcji logowania wyświetla się formularz do wpisania loginu i hasła. W przypadku wpisania złego hasła, otrzymujemy komunikat o tym informujący lub w przypadku, gdy program podejrzewa ze podanego użytkownika nie ma w bazie, również otrzymujemy stosowny komunikat.

|![](https://i.imgur.com/5y6i7AF.png)  |  ![](https://i.imgur.com/LX2JGKP.png) ![](https://i.imgur.com/VMT9OND.png)|
:-------------------------:|:-------------------------:
|Menu logowania          |   Przykładowe komunikaty|

Po zalogowaniu się jako klient uzyskujemy dostęp do podstawowych funkcji programu. Otrzymujemy katalog książek wraz z większością ich danych: autorem, numerem ISBN, liczba stron, informacje dotyczące publikacji (miejsce, czas i wydawnictwo) oraz dostępności książki (czy jest wypożyczona, czy jest zarezerwowana). Możemy zarezerwować książkę, którą chcemy wypożyczyć lub prolongować wypożyczoną już przez nas pozycje. Po wykonaniu czynności które nas interesują możemy się wylogować. 

| ![](https://i.imgur.com/bpitYQ6.png)  |
|---|
| Wygląd programu dla klienta |

Po zalogowaniu się jako bibliotekarz uzyskujemy dostęp do większości funkcji programu. Otrzymujemy katalog książek wraz z ich wszystkimi danymi: autorem, numerem ISBN, liczba stron, informacje dotyczące publikacji (miejsce, czas i wydawnictwo) oraz dostępności książki (czy jest wypożyczona, kto ja wypożyczył, od kiedy i do kiedy, czy jest zarezerwowana, jeśli tak to przez kogo). Mamy możliwość dodania nowej książki, usunięcia istniejącej lub wypożyczenia/zarezerwowania jej istniejącemu użytkownikowi. Po wykonaniu czynności które nas interesują możemy się wylogować.

| ![](https://i.imgur.com/VWsY5qt.png)  |
|---|
| Wygląd programu dla bibliotekarza |

Do uruchomienia programu w systemie Windows potrzebne są pliki konfiguracyjne *.dll, które znajdują się w folderze wraz z plikiem wykonywalnym.  

# 6. Listing kodu C++ - wraz z komentarzami
pliki cpp
# 7. Wnioski
- Realizacja projektu uświadomiła mi, jak ważne jest oddzielenie warstwy logicznej programu od warstwy graficznej.
- W pythonie o wiele prostsze jest instalowanie zewnętrznych bibliotek 
- wirtualne środowisko pythona (virtualenv) jest zupełnie inne niż c++'owskie dynamiczne/statyczne linkowanie bibliotek
- //deploy aplikacji webowej opartej na dockerze jest interesującym konceptem
- w przypadku pythona oddzielenie warstwy logicznej od graficznej jest wymuszone, gdzie w c++ nie (da się bez tego obejść, chociaż odbywa się to kosztem przejrzystości kodu)
- 



dotyczące realizacji własnego programu. Tutaj należy napisać co udało się państwu
oprogramować oraz czego zabrakło a chcielibyście jeszcze zaimplementować.
