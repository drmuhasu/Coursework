"""
Written by Shadman Sakib Rashid (101200114)
Reviewed by Corson Haywood (101193309), Joey Thomas (101200614),
Hasan Suriya (101193772)
12/10/2021- Version 1.0
"""

# Dictionary by Hasan Suriya
import csv

dataHolder = []
with open('Google_Books_Dataset.csv') as csvfile:
    spamreader = csv.reader(csvfile, quoting=csv.QUOTE_NONE)
    for row in spamreader:
        dataHolder.append({
            "row": row[0],
            "title": row[1],
            "author": row[2],
            "rating": row[3],
            "publisher": row[4],
            "pagecount": row[5],
            "genre": row[6],
            "language": row[7]
        })


# function 1 by Shadman Sakib Rashid
def print_dictionary_category(category: str, booklist: dict):
    lines = []
    counter = 0
    for items in booklist:
        if items["genre"] == category:
            counter = counter + 1
            lines.append({
                'text': f"{counter} - {items['title']}, was written by {items['author']}, has the rating "
                        f"{items['rating']}, was published by {items['publisher']}, has the page count of "
                        f"{items['pagecount']},  and is in {items['language']}",
                'category': items['genre']})

    print('The category ' + category + ' has ' + str(
        counter) + ' books.  This is the list  of books in the category ' + category + ' :  ')
    for line in lines:
        print(line['text'])
    if lines.__len__() == 0:
        print("No book was found with the specified category")
        return 'False'
    return lines


# function 2 by Shadman Sakib Rashid
def add_book(booklist: list, new_book: dict):
    """This functions adds a book to the dictionary"""
    if len(new_book) == 8:
        dataHolder.append(new_book)
        print("Book has been added")
        return "Book has been added"
    else:
        print("Book has not added")
        return "Book has not added"


t1 = {'row': '', 'title': "The Butterfly Lion", 'author': "Michael Morpurgo", 'rating': 4.6, 'publisher': 'Collins',
      'pagecount': 128, 'genre': 'Fiction', 'language': 'English'}
t2 = {'row': '', 'title': "Harry Potter and the Philosopher's Stone", 'author': "J.k Rowling", 'rating': 3.8,
      'publisher': 'Bloomsbury', 'pagecount': 128, 'genre': 'Fiction', 'language': 'English'}
t3 = {'row': '', 'title': "Jungle book", 'rating': 4.1, 'pagecount': 89, 'genre': 'real'}


# Function 3 by Shadman Sakib Rashid
def remove_book(title, category, booklist):
    """Removes a book from the dictionary"""
    books = []
    for items in booklist:
        if (items['title'] == title) and (items['genre'] == category):
            books.append(items)
            dataHolder.remove(items)
            print('The book has been removed correctly.')
            return 'The book has been removed correctly.'
    if books.__len__() == 0:
        print("There was an error removing the book. Book not found.")
        return "There was an error removing the book. Book not found."


# Function 4 by Corson Haywood
def get_books_by_rate(rating, bookList: list):
    books = []
    counter = 0
    print('the books with a rating between ' + str(rating) + ' and ' + str(rating + 1) + ' are:')
    for items in bookList:
        if items["rating"] <= str(rating + 1):
            counter = counter + 1
            print(str(counter) + '-' + "title:", items["title"], "-""Authors:", items["author"], "-""Rating:",
                  items["rating"], "-" "Publisher:", items["publisher"], "-""Category:", items["genre"],
                  "-""Page Count:", items["pagecount"])
            books.append(items)
    if books.__len__() == 0:
        print("No book was found with the specified rating")


# Function 5 by Corson Haywood
def find_books_by_title(title, bookList: list):
    for items in bookList:
        if items["title"] == title:
            print('The book has been found')

            return True

    else:
        print('The book has NOT been found')
        return False

    # Function 6 by Corson Haywood


def get_books_by_author(author, bookList: list):
    books = []
    counter = 0
    print('The author ' + str(author) + ' has published the following books:')
    for items in bookList:
        if items["author"] == author:
            counter = counter + 1
            print(str(counter) + '-' + items["title"])
            books.append(items)
    if books.__len__() == 0:
        print("No book was found with the specified rating")


# Function 7 by Joey Thomas
def get_books_by_publisher(publisher, dictionary: list):
    b = []
    count = 0
    print('The publisher ' + str(publisher) + ' has published the following books:')
    for items in dictionary:
        if items["publisher"] == publisher:
            count = count + 1
            print(str(count) + '-' + items["title"])
            b.append(items)
    if b.__len__() == 0:
        print("There are no books with that Publisher.")


# Function 8 by Joey Thomas
def check_category_and_title(genre, title, dictionary: list):
    for items in dictionary:
        if items["title"] == title and items["genre"] == genre:
            print("The category " + str(genre) + " has the book title " + str(title) + ".")
            return True

    else:
        print("The category " + str(genre) + " does not have the book title " + str(title) + ".")
        return False


# Function 9 by Joey Thomas
def all_categories_for_book_title(title, dictionary: list):
    b = []
    print('The book title ' + str(title) + ' has the following categories:')
    for items in dictionary:
        if items["title"] == title:
            print(items["genre"])
            b.append(items)
    if b.__len__() == 0:
        print("That book does not exist.")


# Function 10 by Hasan Suriya
def get_books_by_category(category: str, bookList: list):
    books = []
    counter = 0
    print(bookList[69])
    print('The category ' + category + ' has the following books:')
    for items in bookList:
        if items["genre"] == category:
            counter = counter + 1
            print(str(counter) + '-' + items["title"])
            books.append(items)
    if books.__len__() == 0:
        print("No book was found with the specified category")


# Function 11 by Hasan Suriya
def get_books_by_category_and_rating(category: str, rating, bookList: list):
    books = []
    counter = 0
    print(bookList[69])
    print('These books with the ' + str(rating) + ' and ' + category + ' are the following:')
    for items in bookList:
        if (items['genre'] == category) and (items["rating"] >= str(rating)):
            counter = counter + 1
            print(str(counter) + '-' + items["title"])
            books.append(items)
    if books.__len__() == 0:
        print("No book was found with the specified category and rating")


# Function 12 by Hasan Suriya
def get_author_categories(author: str, booklist: dict):
    books = {}
    counter = 0
    print('The  author ' + author + ' has  published  books  under  the  following categories:')
    for items in booklist:
        if items["author"] == author:
            counter = counter + 1
            print(str(counter) + '-' + items["genre"])
            books.update(items)
    if books.__len__() == 0:
        print("The specified author is invalid")
