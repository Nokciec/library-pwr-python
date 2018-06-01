# 1. Zalozenia i opis funkcjonalny programu
##### Poruszany problem:
Program będzie obsługiwał system zarządzania biblioteką.
![alt text](https://i.imgur.com/BmS47tO.png) 
^ screen1 main
![alt text](https://i.imgur.com/KnS2zRj.png) 
^ screen2 rejestracja
![alt text](https://i.imgur.com/qQBTneO.png) 
^ screen3 katalog smiertelnika
![alt text](https://i.imgur.com/5y6i7AF.png)
^ screen4 logowanie
![alt text](https://i.imgur.com/uRibVVx.png)
^screen5 wyglad bibliotekarza
![alt text](https://i.imgur.com/bpitYQ6.png)
^ screen wybor smiertelnika

##### Użytkownik docelowy:
Program dedykowany jest dla klientów biblioteki oraz jej pracowników.
##### Założenia:
Klientom zostanie umożliwione m. in.: rejestracja, logowanie, przeglądanie zasobów
biblioteki, rezerwacja pozycji oraz prolongowanie wypożyczonych już dzieł.
Pracownicy będą mogli wypożyczać zasoby klientom, dodawać nowe pozycje oraz usuwać istniejace. Tak jak i klienci będą mieli dostęp do rejestracji, logowania oraz katalogu bibliotek.
##### Dodatkowe założenia:
Klient będzie mógł wyświetlić swój profil, a w nim sprawdzić historię wypożyczeń, listę swoich rezerwacji, usunąć swoje konto oraz wylogować się.
##### Użyte języki, środowiska i frameworki:
- C++, Qt Creator
- Python, CSS, HTML, Jinja2, FireBase,
# 2. Diagramy UML
## a) diagram przypadkow uzycia
//do wklejenia
## b) diagram klas
//do zrobienia i wklejenia
# 3. Kod klas C++
Z kodu klas zostaly usuniete fragmenty dotyczace GUI.
#### addBookForm class
```c++
class addbookform : public QDialog
{
public:
    explicit addbookform(QWidget *parent = 0);
    ~addbookform();
private:
    /**
This function adds a new book. It takes: title, author, ISBN number, publication date, publication place, publisher and number of pages as arguments. 
    */
    void addNewBook(QString title, QString author, QString ISBN, QString publicationDate, QString publicationPlace, QString publisher, QString pagesNumber);
};
```
### book class
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
This function creates a book given its data.
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
### bookManager class
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

### class LoginManager
```c++
class LoginManager : public QDialog
{
public:
/**
Helper functions
*/
    QString getLogin();
    QString getPassword();

/**
Helper functions
*/
    bool isAccepted;
    bool getAccess() const {return access;}
    int getPermissions() const {return permissions;}
    
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
#### class mainwindow
```c++
class MainWindow : public QMainWindow
{
protected:
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
### registermanager class
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
### user class
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
### usermanager class
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
# 4. Schematy blokowe oraz kod wlasnych funkcji 
schemat blokowy jeden na pewno
# 5. Opis uzytkowy programu C++ 
//opis jak poruszać się po programie wraz z zrzutami ekranu (zwłaszcza opis menu),wymagania techniczne i uwagi instalacyjne (w przypadku skomplikowanej instalacji,
projekt można wzbogacić opracowanym instalatorem).
# 6. Listing kodu C++ - wraz z komentarzami
pliki cpp
# 7. Wnioski
- Realizacja projektu uswiadomila mi, jak wazne jest oddzielenie warstwy logicznej programu od wartwy graficznej.
- W pythonie o wiele prostsze jest instalowanie zewnetrznych bibliotek 
- wirtualne srodowisko pythona (virtualenv) jest zupelnie inne niz c++'owskie dynamiczne/statyczne linkowanie bibliotek
- //deploy aplikacji webowej opartej na dockerze jest interesujacym konceptem
- w przypadku pythona oddzielenie warswty logicznej od graficznej jest wymuszone, gdzie w c++ nie (da sie bez tego obejsc, chociaz odbywa sie to kosztem przejrzystosci kodu)
- 



dotyczące realizacji własnego programu. Tutaj należy napisać co udało się państwu
oprogramować, oraz czego zabrakło a chcielibyście jeszcze zaimplementować.
