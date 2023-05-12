'''
Team T150 : Shadman Sakib Rashid, Corson Haywood, Joey Thomas, Hasan Suriya
This document was made by Hasan Suriya, with assistance from the rest of the team
'''

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


# Test for Function 1 by Hasan Suriya
from T150_P2_search_modify_dataset import print_dictionary_category

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
from T150_P2_search_modify_dataset import add_book

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
from T150_P2_search_modify_dataset import remove_book

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
# test for Function 4 by Joey Thomas


# test for Function 5 by Joey Thomas
from T150_P2_search_modify_dataset import find_books_by_title

def check_find_books_by_title(desc, outcome:str, expected:str and bool) -> None:
    if outcome == expected:
        print('TEST PASSED')
    else:
        print('TEST FAILED the expected was ' + expected)
    print('-------')
def test_find_books_by_title():
    check_find_books_by_title('After Anna', find_books_by_title('After Anna', dataHolder), 'The book has been found' and True)
    check_find_books_by_title('Deadpool Kills the Marvel Universe', find_books_by_title('Deadpool Kills the Marvel Universe', dataHolder), 'The book has been found' and True)
    #check_find_books_by_title()

test_find_books_by_title()

# test for Function 6 by Joey Thomas


# test for Function 7 by Corson Haywood

from T150_P2_search_modify_dataset import get_books_by_publisher
from T150_P2_search_modify_dataset import dataHolder

def check_equal(description: str, outcome:str, expected) -> None:

        print(description)
        if outcome == expected:
                print('passed')
        else: 
                print('failed expected was ' + expected)

        outcome_type = type(outcome)
        expected_type = type(expected)
        if outcome_type != expected_type:

        # The format methods is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.

                print("{0} FAILED: expected ({1}) has type {2}, " \
                      "but outcome ({3}) has type {4}".
                      format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
                print('-----')
        elif outcome != expected:
                print("{0} FAILED: expected {1}, got {2}".
                      format(description, expected, outcome))

                print('-----')                
        else:
                print("{0} PASSED".format(description))
                print("------")
                

def test_get_books_by_publisher() -> None:

    check_equal('get_books_by_publisher("Tor Books", dataHolder)', get_books_by_publisher("Tor Books", dataHolder),"The publisher Tor Books has published the following books: 1-Edgedancer: From the Stormlight Archive 2-Mistborn Trilogy: The Final Empire, The Well of Ascension, The Hero of Ages 3-Edgedancer: From the Stormlight Archive") 

test_get_books_by_publisher()

# test for Function 8 by Corson Haywood


# test for Function 9 by Corson Haywood


# test for Function 10 by Shadman Sakib Rashid


# test for Function 11 by Shadman Sakib Rashid
from T150_P2_search_modify_dataset import get_books_by_category_and_rating

def check_get_books_by_category_and_rating(description, outcome:str, expected:str) -> None:
    print(description)
    if outcome == expected:
        print('passed')
    else: 
        print('failed expected was ' + expected)
    print('-------')
    
def test_check_get_books_by_category_and_rating():
    check_get_books_by_category_and_rating('Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth,Principles: Life and Work,The Magic of Thinking Big,Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk,Platform: Get Noticed in a Noisy World ', get_books_by_category_and_rating("Economics", 4.5, dataHolder) , 'Book has been sorted')
    check_get_books_by_category_and_rating('Immortal Hulk Vol. 1: Or Is He Both?,The Joker,Venomized ', get_books_by_category_and_rating("Comics", 4.3, dataHolder), 'Book has been sorted')
    check_get_books_by_category_and_rating('no book was found ', get_books_by_category_and_rating("Sci-fi", 3, dataHolder), 'Book has been sorted') 

test_check_get_books_by_category_and_rating()

# test for Function 12 by Shadman Sakib Rashid
