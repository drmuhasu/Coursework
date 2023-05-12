"""
Written by Shadman Sakib Rashid (101200114)
Reviewed by Corson Haywood (101193309), Joey Thomas (101200614),
Hasan Suriya (101193772)
12/10/2021- Version 1.0
"""

# Dictionary by Hasan Suriya
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


# Funciton Made by Hasan Suriya
def load_file():
    with open('Google_Books_Dataset.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for i in csv_reader:
            if line_count == 0:
                print(f'The Data stored within "Google_Books_Dataset.csv" includes : {", ".join(i)}')
                line_count += 1
            else:
                print(f'\t{i[0]} The Title of the book is {i[1]}.')
                line_count += 1
        return


# Funciton Made by Hasan Suriya
def add_book(new_book):
    row_num = len(dataHolder)
    for book in dataHolder:
        if len(new_book) == 7:
            dataHolder[row_num] = t1
            row_num = row_num + 1
            print("Book has been added in 'Google_Books_Dataset.csv'.")
            show_dict = input('Input S if you would like to see the new Dictionary, if not input another key: ')
            if show_dict == 's' or show_dict == 'S':
                return print(dataHolder)
            else:
                print('Thank You')
                return
        else:
            print("Book has not added")
            return

# Funciton Made by Hasan Suriya
def remove_book(key: int):
    for book in dataHolder:
        if key > 0:
            print(str(dataHolder[key]["title"]) + " has been removed")
            del dataHolder[key]
            show_dict = input('Input S if you would like to see the new Dictionary, if not input another key: ')
            if show_dict == 's' or show_dict == 'S':
                return print(dataHolder)
            else:
                print('Thank You')
                return
        else:
            print("Book isn't in the dataset")
            return

# Funciton Made by Hasan Suriya
def find_book_by_title():
    title = input('Please input the title of the book: ')
    var = False
    for i in dataHolder:
        if dataHolder[i]['title'] == title:
            print(dataHolder[i])
            var = True
    if len(title) == 0:
        print('No input was detected.')
    elif not var:
        print('Print')

# Funciton Made by Shadman Sakib Rashid
def get_author_categories(author:str, dictionary:list):
    value = False
    for element in dataHolder:
        if dataHolder[element]["author"] == author:
            print(dataHolder[element])
            value = True
    if len(author) == 0:
        print('---------')
    else:
        value != True
        print('Above are the categories related to the author')      

# Funciton Made by Shadman Sakib Rashid
def all_categories_for_book_title(title:str, dictionary:list):
    value = False
    for element in dataHolder:
        if dataHolder[element]["title"] == title:
            print(dataHolder[element])
            value = True
    if len(title) == 0:
        print('--------')
    else:
        value != True
        print('Above are the categories/genres related to the book')
        
# Function Made By Joey Thomas
def get_books_by_publisher(publisher:str, dictionary:list):
    var = False
    for i in dataHolder:
        if dataHolder[i]['publisher'] == publisher:
            print(dataHolder[i])
            var = True
    if len(publisher) == 0:
        print('No input was detected.')
    elif var != True:
        print('Print')      

# Function Made By Joey Thomas
def get_books_by_rate(rating:float, bookList:list):
    var = False
    for i in dataHolder:
        if dataHolder[i]['rating'] == rating:
            print(dataHolder[i])
            var = True
    if len(rating) == 0:
        print('No input was detected.')
    elif var != True:
        print('Print')        
        
# Function Made By Joey Thomas
def get_books_by_author(author:str, bookList:list): 
    var = False
    for i in dataHolder:
        if dataHolder[i]['author'] == author:
            print(dataHolder[i])
            var = True
    if len(author) == 0:
        print('No input was detected.')
    elif var != True:
        print('Print')    

# Function Made By Joey Thomas
def get_books_by_category(category:str, bookList: list):
    var = False
    for i in dataHolder:
        if dataHolder[i]['genre'] == category:
            print(dataHolder[i])
            var = True
    if len(category) == 0:
        print('No input was detected.')
    elif var != True:
        print('Print')      

# Function Made By Joey Thomas
def check_category_and_title(genre:str, title:str, dictionary:list):
    var = False
    for i in dataHolder:
        if dataHolder[i]['title'] == title and dataHolder[i]['genre'] == genre:
            print(dataHolder[i])
            var = True
    if len(genre) == 0:
        print('No input was detected.')
    elif var != True:
        print('Print')         
        
# Function Made By Joey Thomas
def get_books_by_category_and_rating(category:str, rating, bookList: list):
    var = False
    for i in dataHolder:
        if dataHolder[i]['genre'] == category and dataHolder[i]['rating'] == rating:
            print(dataHolder[i])
            var = True
    if len(category) == 0:
        print('No input was detected.')
    elif var != True:
        print('Print')  

# Function Made By Corson Haywood
def sort_books_title(booklist: dict):
    lst = [val for val in booklist.values()]
    for val in range(len(lst)):
        for num in range(val+1, len(lst)):
            if lst[num]["title"] < lst[val]["title"]:
                lst[val], lst[num] = lst[num], lst[val]              
    for val in lst:
        print(val["title"])
    return 

# Function Made By Corson Haywood
def sort_books_ascending_rate(booklist: dict):
    lst = [i for i in booklist.values()]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j]['rating'] < lst[i]['rating']:
                lst[i], lst[j] = lst[j], lst[i]
    for i in lst:
        print(i['rating'])

# Function Made By Corson Haywood
def sort_books_publisher(booklist: dict):
    lst = [i for i in booklist.values()]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j]['publisher'] < lst[i]['publisher']:
                lst[i], lst[j] = lst[j], lst[i]
    for i in lst:
        print(i['publisher'])
    return   

# Function Made By Corson Haywood
def sort_books_category(booklist: dict):
    lst = [i for i in booklist.values()]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j]['genre'] < lst[i]['genre']:
                lst[i], lst[j] = lst[j], lst[i]
    for i in lst:
        print(i['genre'])
    return 

# Function Made By Corson Haywood
def sort_books_pageCount(booklist: dict):
    lst = [i for i in booklist.values()]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j]['pagecount'] < lst[i]['pagecount']:
                lst[i], lst[j] = lst[j], lst[i]
    for i in lst:
        print(i['pagecount'])
    return 

# Function Made by Hasan Suriya
def quit_commmand():
    print('Thank you')
    exit()
        
        
# User Interface
Commands = (
    "1- Command Line L)oad file\n" "2- Command Line A)dd book \n" "3- Command Line R)emove book\n" "4- Command Line "
    "F)ind book by title \n" "5- Command Line NC) Number of books in a category\n" "6- Command Line CA) Categories "
    "for an author\n" "7- Command Line CB) Categories for a book title\n" "8- Command Line G)et book\n R)ate   "
    "A)uthor   P)ublisher   C)ategory   CT) Category and Title   CR) Category and Rate\n" "9- Command Line S)ort "
    "book\n T)itle   R)ate   P)ublisher   C)ategory   P)ageCount\n" "10- Command Line Q)uit")


def get_command():
    print(Commands)
    function = input("Please input the Function you'd like to run:")
    while len(function) != 1:
        print('Please use the letter used to identidy the codes above')
        get_command()
        break
    if function == 'L' or function == 'l':
        load_file()
        repeat = input('Would you like it to run the original code again input Y else input a key: ')
        if repeat == 'Y' or repeat == 'y':
            get_command()
        else:
            print('Thank you')
    elif function == 'A' or function == 'a':
        a = input('Title: ')
        b = input('Author: ')
        c = float(input('Rating: '))
        d = input('Publisher: ')
        e = int(input('Pagecount: '))
        f = input('Genre: ')
        g = input('Language: ')
        new_book = {'title': a, 'author': b, 'rating': c, 'publisher': d, 'pagecount': e, 'genre': f, 'language': g}
        add_book(new_book)
        repeat = input('Would you like it to run the original code again input Y else input a key: ')
        if repeat == 'Y' or repeat == 'y':
            get_command()
        else:
            print('Thank you')
    elif function == 'R' or function == 'r':
        key = int(input('Please Input the key for the book you want to remove: '))
        remove_book(key)
        repeat = input('Would you like it to run the original code again input Y else input a key: ')
        if repeat == 'Y' or repeat == 'y':
            get_command()
        else:
            print('Thank you')
    elif function == 'F' or function == 'f':
        find_book_by_title()
        repeat = input('Would you like it to run the original code again input Y else input a key: ')
        if repeat == 'Y' or repeat == 'y':
            get_command()
        else:
            print('Thank you')
    elif function == 'CA':
        input_rating = input('Please enter the author: ')
        get_author_categories(dataHolder, input_rating)
    elif function == 'CB':
        input_rating = input('Please enter the author: ')
        all_categories_for_book_title(dataHolder, input_rating)    
    elif function == 'g'or function == 'G':
        function1= input('Input a valid command:')
        if function1 == 'R':
            input_rating = input('Please enter the rating of the books you want to find: ')
            get_books_by_rate(dataHolder, input_rating)
        
        elif function1 == 'A':   
            input_author = input('Please enter the author of the books you want to find: ')
            get_books_by_author(input_author, dataHolder)
            
        elif function1 == 'P':
            input_publisher = input('Please enter the publisher of the books you want to find: ')
            get_books_by_publisher(input_publisher, dataHolder)
            
        elif function1 == 'C':
            input_category = input('Please enter the category of the books you want to find: ')
            get_books_by_category(input_category, dataHolder)
        
        elif function1 == 'CT':
            input_category = input('Please enter the category of the books you want to find: ')
            input_title = input('Please enter the title of the books you want to find: ')
            check_category_and_title(input_category, input_title, dataHolder)
        
        elif function1 == 'CR':  
            input_category = input('Please enter the category of the books you want to find: ')
            input_rating = input('Please enter the rating of the books you want to find: ')
            get_books_by_category_and_rating(input_category, input_rating, dataHolder)
        elif function1 == 'T':   
            sort_books_title(dataHolder)
        else:
            print('Invalid Command')        
        
    elif function == 's' or function == 'S':
        function2= input('Input a valid command:')

        if function2 == 'R':
            sort_books_ascending_rate(dataHolder)
        
        elif function2 == 'P':
            sort_books_publisher(dataHolder)
            
        elif function2 == 'C':
            sort_books_category(dataHolder)
            
        elif function2 == 'PA':
            sort_books_pageCount(dataHolder)
        else:
            print('Invalid Command')                    
            
    elif function == 'Q' or function == 'q':  
        print('Thank You')
get_command()
