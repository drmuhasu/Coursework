import csv
# Dictionary
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

# Test for Function 1 by Hasan Suriya
from T150_P2_func import print_dictionary_category

def check_print_dictionary_category(description: str, outcome, expected:str):
    truth = True
    if type(outcome) == str:
        print("PASSED")
    else:
        for item in outcome: 
            if item['category'] == expected:
                continue 
            else:
                print('failed the expected was ' + expected)
                truth = False 
                break
        if truth == True:
            print('PASSED')
    print("------")

def test_print_dictionary_category():      
    check_print_dictionary_category('Comics ', print_dictionary_category('Comics', dataHolder), 'Comics')
    check_print_dictionary_category('Epic ', print_dictionary_category('Epic', dataHolder ),  'Epic' )
    check_print_dictionary_category('Sci-fi ', print_dictionary_category('Sci-fi', dataHolder), 'Sci-fi')
test_print_dictionary_category()


# Test for Function 2 by Hasan Suriya
from T150_P2_func import add_book

t1={'row': '', 'title': "The Butterfly Lion", 'author': "Michael Morpurgo", 'rating': 4.6, 'publisher': 'Collins', 'pagecount': 128, 'genre': 'Fiction', 'language': 'English'}
t2={'row': '', 'title': "Harry Potter and the Philosopher's Stone", 'author': "J.k Rowling", 'rating': 3.8, 'publisher': 'Bloomsbury', 'pagecount': 128, 'genre': 'Fiction', 'language':'English'}
t3={'row': '', 'title': "Jungle book", 'rating': 4.1, 'pagecount': 89, 'genre': 'real'}


def check_add_book(description, outcome:str, expected:str) -> None:
    print(description)
    if outcome == expected:
        print('PASSED')
    else: 
        print('failed the expected was ' + expected)
    print('--------')

def test_add_book():
    check_add_book('t1 ', add_book(dataHolder,t1), 'Book has been added')
    check_add_book('t2 ', add_book(dataHolder,t2), 'Book has been added')
    check_add_book('t3 ', add_book(dataHolder,t3), 'Book has not added')
test_add_book()


# Test for Function 3 by Hasan Suriya
from T150_P2_func import remove_book

def check_remove_book(description, outcome:str, expected:str) -> None:
    print(description)
    if outcome == expected:
        print('PASSED')
    else: 
        print('Failed the expected outcome was ' + (expected))
    print('--------')

def test_remove_book():
    check_remove_book('After Anna, Fiction ', remove_book('After Anna','Fiction',dataHolder), 'The book has been removed correctly.')
    check_remove_book('Total Control, Mystery', remove_book('Total Control','Mystery',dataHolder), 'The book has been removed correctly.')
    check_remove_book('Jungle book, Fiction', remove_book('Jungle book','Fiction',dataHolder), 'There was an error removing the book. Book not found.')
test_remove_book()
