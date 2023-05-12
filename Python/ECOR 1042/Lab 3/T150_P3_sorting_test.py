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
