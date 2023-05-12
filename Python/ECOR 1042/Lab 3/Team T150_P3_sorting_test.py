#Dictionary
import csv
dataHolder = {}
with open('Google_Books_Dataset.csv') as csvfile:
    spamreader = csv.reader(csvfile, quoting=csv.QUOTE_NONE)
    for index, row in enumerate(spamreader):
        dataHolder[index] = {
            "title": row[1],
            "author": row[2],
            "rating": row[3],
            "publisher": row[4],
            "pagecount": row[5],
            "genre": row[6],
            "language": row[7]
        }
dataHolder2 = ()        


#Test for Function 1 by Corson Haywood
from T150_P3_sorting import sort_books_title
def check_sort_books_title(description, outcome, expected) -> None:
    print(description)
    if outcome == expected:
        print('PASSED')
    else:
        print('FAILED, expected was ' + expected)
    print('-------')
           
def test_check_sort_books_title():
    check_sort_books_title('Sorting of dataHolder', sort_books_title(dataHolder), 'Sorted by Title')
    check_sort_books_title('Sorting of dataHolder', sort_books_title(dataHolder), sort_books_title(dataHolder))
test_check_sort_books_title()

#Test for Function 2 by Hasan Suriya
from T150_P3_sorting import sort_books_ascending_rate

def check_sort_books_ascending_rate(description, outcome, expected) -> None:
    print(description)
    if outcome == expected:
        print('PASSED')
    else: 
        print('FAILED, expected output is ' + expected)
    print('--------')

def test_sort_books_ascending_rate():
    check_sort_books_ascending_rate('Sorting of dataHolder', sort_books_ascending_rate(dataHolder), 'Sorted by Rating')
    check_sort_books_ascending_rate('Sorting of dataHolder2', sort_books_ascending_rate(dataHolder2), 'An Error Occured')
    
test_sort_books_ascending_rate()

#Test for Function 3 by Joey Thomas
from T150_P3_sorting import sort_books_descending_rate

def test_sort_books_descending_rate(desc, outcome, expected)-> None:
    if outcome == expected:
        print('TEST PASSED')
    else: 
        print('TEST FAILED', 'the expected output was' + expected)
    print('++++++++++++++++++++')
    

test_sort_books_descending_rate('Sort by Rating (descending)', sort_books_descending_rate(dataHolder), 'Sorted in descending order by rating')  

#Test for Function 4 by Joey Thomas
from T150_P3_sorting import sort_books_publisher

def test_sort_books_publisher(desc, outcome, expected)-> None:
    if outcome == expected:
        print('TEST PASSED')
    else:
        print('TEST FAILED', 'the expected output was' + expected)
    print('++++++++++++++++++++')
    
test_sort_books_publisher('Sort by Publisher', sort_books_publisher(dataHolder), 'Sorted by publisher')


#Test for Function 5 by Shadman Skakib Rashid 
from T150_P3_sorting import sort_books_pageCount

def check_sort_books_pageCount(description_of_function:str, outcome, expected) -> None:
    print(description_of_function)
    
    if outcome == expected:
        
        print('PASSED')
        print('--------')        
    else: 
        
        print('FAILED, expected output is ' + expected)
        print('--------')
        
    print('end')


def test_sort_books_pageCount():
    
    check_sort_books_pageCount('dataHolder sorting by pageCount', sort_books_pageCount(dataHolder), 'Sorted by pagecount')
    check_sort_books_pageCount('dataHolder sorting by pageCount', sort_books_pageCount(dataHolder), 'An Error Occured')
    
test_sort_books_pageCount()
    

#Function 6 by Shadman Sakib Rashid
from T150_P3_sorting import sort_books_category

def check_sort_books_category(description_of_function:str, outcome,expected) -> None:
    
    print(description_of_function)
    
    if outcome == expected:
        
        print('PASSED')
        
    else: 
        
        print('FAILED, expected output is ' + expected)
        
    print('New line')

def test_sort_books_category():
    
    check_sort_books_category('dataHolder sorting, by category', sort_books_category(dataHolder), 'Sorts by Category')
    check_sort_books_category('dataHolder sorting, by category', sort_books_category(dataHolder), 'Error Occured')
    
test_sort_books_category()