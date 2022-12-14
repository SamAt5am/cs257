#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2022

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.

    Edited by Sam Hiken and Barry Nwike, 9/24

    Revised by Sam Hiken 10/7
'''

import csv

class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None, books = []):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year
        self.books = books

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name
    
    def __lt__(self, other):
        if self.surname == other.surname:
            return self.given_name < other.given_name
        else:
            return self.surname < other.surname

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = int(publication_year)
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title

class BooksDataSource:

    def __init__(self, books_csv_file_name):
        ''' The books CSV file format looks like this:

                title,publication_year,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''
        with open(books_csv_file_name) as file:
            csv_reader = csv.reader(file, delimiter=',')
            self.Authors = []
            self.Books = []
            for row in csv_reader:
                is_present = False
                author_list = self.create_author(row)
                book = self.create_book(row, author_list)
                self.Books.append(book)
                for author in author_list:
                    author.books.append(book)
                    if(self.Authors != None):
                        for other_author in self.Authors:
                            if author.__eq__(other_author):
                                is_present = True
                                other_author.books.append(book)
                        if not is_present:
                            self.Authors.append(author)
                    else:
                        self.Authors.append(author)
        
        #self.sort_authors()
        self.Authors = sorted(self.Authors)

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Bront?? comes before Charlotte Bront??).
        '''
        search_result = []
        for author in self.Authors:
            full_name = author.given_name + ' ' + author.surname
            if search_text == None or (search_text.lower()) in full_name.lower():
                search_result.append(author)
        
        return search_result

    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''
        search_result = []
      
        for book in self.Books:
            if search_text == None or search_text.lower() in book.title.lower():
                search_result.append(book)

        if sort_by == 'year':
            search_result = sorted(search_result, key= lambda book:book.publication_year)
        else:
            search_result = sorted(search_result, key= lambda book:book.title)

        return search_result

    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''
        results = []
        if start_year == None: 
            start_year = -10000000
        if end_year == None:
            end_year = 1000000000
        bookList = self.sort_books_year(self.Books)
        for book in bookList:
            if book.publication_year >= start_year and book.publication_year <= end_year:
                results.append(book)
        results = self.sort_books_title(results)
        return results
    
    def create_author(self, row):
        name_string = row[2]
        mult_authors = name_string.split(' and ')
        author_list = []
        for name in mult_authors:
            name_list = name.split(' ')
            surname = name_list[len(name_list) - 2]
            given_name = name_list[0]
            n = 1
            while n < len(name_list) - 2:
                given_name = given_name + ' ' + name_list[n]
                n+=1
            range = name_list[len(name_list)-1]
            range = range[1: len(range)-1]
            year_list = range.split('-')
            birth_year = year_list[0]
            death_year = None
            if year_list[1] != '':
                death_year = year_list[1]
            author = Author(surname,given_name,birth_year,death_year,[])
            author_list.append(author)

        return author_list

    def create_book(self, row, author):
        title = row[0]
        publish_year = int(row[1])
        authors = author

        book = Book(title, publish_year, authors)
        return book
    
if __name__ == "__main__":
    source = BooksDataSource("books1.csv")