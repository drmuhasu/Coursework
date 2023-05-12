#dictionary
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
     

# Function 10
def get_books_by_category(category: str, booklist: dict):
    ''' This function takes in two inputs one which is the category and the 
    other is a dictionary. The result should be the printing books title that 
    match the category inputed.
    
    >>>get_books_by_category("Epic", dataHolder) 
    The category Epic has the following books:
    1-The Tower of the Swallow: Witcher 6
    2-The Way Of Shadows: Book 1 of the Night Angel

    >>>get_books_by_category("Comics", dataHolder) 
    The category Comics has the following books:
    1-Deadpool Kills the Marvel Universe
    2-Young Justice Vol. 1
    3-Ultimate Spider-Man Vol. 11: Carnage
    4-Immortal Hulk Vol. 1: Or Is He Both?
    5-Watchmen (2019 Edition)
    6-The Joker
    7-Venomized

    >>>get_books_by_category("Sci-fi", dataHolder) 
    The category Sci-fi has the following books:
    No book was found with the specified category 
    '''
    books = []
    counter = 0
    print('The category ' + category + ' has the following books:') 
    for items in booklist:
        if (items["genre"] == category):
            counter = counter + 1
            print(str(counter) +'-'+ items["title"])
            books.append(items)
    if (books.__len__() == 0):
        print("No book was found with the specified category")

# Function 11
def get_books_by_category_and_rating(category:str, rating, booklist:dict):
    ''' This function takes in three inputs one which is the category , one the 
    rating and the last is a excel file. The result should be the printing 
    books title that match the category and the with the rating inputed being 
    the minimum rating of the books being printed.
    
    >>>get_books_by_category_and_rating("Economics", 4.5, dataHolder) 
    These books with the 4.6 and Economics are the following:
    1-Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth
    2-Principles: Life and Work
    3-The Magic of Thinking Big
    4-Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk
    5-Platform: Get Noticed in a Noisy World

    >>>get_books_by_category_and_rating("Comics", 4.3, dataHolder) 
    These books with the 4.3 and Comics are the following:
    1-Immortal Hulk Vol. 1: Or Is He Both?
    2-The Joker
    3-Venomized


    >>>get_books_by_category_and_rating("Sci-fi", 3, dataHolder) 
    These books with the 3 and Sci-fi are the following:
    No book was found with the specified category and rating

    '''
    books = []
    counter = 0
    print('These books with the ' + str(rating) + ' and ' + category + ' are the following:') 
    for items in booklist:
        if (items['genre'] == category) and (items["rating"] >= str(rating)):
            counter = counter + 1
            print(str(counter) +'-'+ items["title"])
            books.append(items)
    if (books.__len__() == 0):
        print("No book was found with the specified category and rating")



# Function 12
def get_author_categories(author: str, booklist:dict):
    '''This function takes in two inputs one which is the author, the other is 
    a excel file. The result should be the printing the category of books the 
    author has written.
    
    >>>get_author_categories("Blake Pierce", dataHolder) 
    The  author Blake Pierce has  published  books  under  the  following categories:
    1-Mystery
    2-Fiction
    3-Thrillers
    4-Detective
    
    >>>get_author_categories("Brian Tracy", dataHolder) 
    The  author Brian Tracy has  published  books  under  the  following categories:
    1-Economics
    2-Business
    3-Business
    4-Management
    >>>get_author_categories("Joseph Anderson", dataHolder) 
    The  author Joseph Anderson has  published  books  under  the  following categories:
    The specified author is invalid
    '''
    books = {}
    counter = 0
    print('The  author ' + author + ' has  published  books  under  the  following categories:') 
    for items in booklist:
        if (items["author"] == author):
            counter = counter + 1
            print(str(counter) +'-'+ items["genre"])
            books.update(items)
    if (books.__len__() == 0):
        print("The specified author is invalid")



# Issue with this code is the fact that duplicate categories are being printed. 
# please provide feedback on how I can fix this