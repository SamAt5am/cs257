
import booksdatasource
import sys

def main():
    input = sys.argv
    command = input[1]
    parameter1 = None
    parameter2 = None
    if(len(input) > 2):
        parameter1 = input[2]
        if(len(input)>3):
            parameter2 = input[3]
    dataSource = booksdatasource.BooksDataSource("books1.csv")
    if(command == "--author"):
        list = dataSource.authors(parameter1)
        display_author(list)
    elif command == "--book":
        if (parameter1 != '-n'):
            display_book(dataSource.books(parameter1, parameter2))
        else:
            display_book(dataSource.books(None, parameter2))

    elif command == "--book_yby":
        if((parameter1 != None and parameter1.isnumeric()) or (parameter2 != None and parameter2.isnumeric())):
            if(parameter1 != None and parameter1.isnumeric()):
                parameter1 = int(parameter1)
            else:
                parameter1 = None
            if(parameter2 != None and parameter2.isnumeric()):
                parameter2 = int(parameter2)
            else:
                parameter2 = None
            display_book(dataSource.sort_books_year(dataSource.books_between_years(parameter1, parameter2)))
        else:
            display_book(dataSource.sort_books_year(dataSource.Books))
            
    else:
        file = open('usage.txt')
        print(file.read())
        file.close()


def display_author(authorList):
    for author in authorList:
        author_name = author.given_name + " " + author.surname
        author_years = ""
        if author.birth_year != None and author.death_year != None:
            author_years = "(" + author.birth_year + "-" + author.death_year + ")"
        elif author.birth_year == None:
            author_years = "(-" + author.death_year + ")"
        else:
            author_years = "(" + author.birth_year + "-)"
        print(author_name + ": " + author_years)
        print_author_books(author)

def print_author_books(author):
    book_string = ""
    for book in author.books:
        
        book_string = book_string + "\n" + book.title
        
    print(book_string[1:]+"\n")

def display_book(bookList):
    for book in bookList:
        book_title = book.title
        book_authors = ""
        for author in book.authors:
            book_authors = book_authors + author.given_name + " " + author.surname + ", "
        book_year = str(book.publication_year)
        print(book_title + ": " + book_authors + book_year)

if __name__ == '__main__':
	main()

    