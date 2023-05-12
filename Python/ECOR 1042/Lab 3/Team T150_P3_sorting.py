# Group T150: Shadman Sakib Rashid, Corson Haywood, Joey Thomas, Hasan Suriya

#Dictionary for testing
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


#Function 1 by Shadman Sakib Rashid
def sort_books_title(booklist: dict):
    '''The function takes a dictionary parameter where the books
    are stored.The function returns a list with the book data stored as a 
    dictionary where the books are sorted alphabetically by title.
    
    unsorted_book_data= dict({
    {"title": "The Painted Man (The Demon Cycle, Book 1)", "author": "Peter V. Brett", "language ": "English", "rating": 4.5, "publisher": "HarperCollins UK", "genres": "Fiction", "pageCount": 544}, 
    {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery", "author": "Barbara Allan", "language ": "English", "rating": 3.3, "publisher": "Kensington Publishing Corp.", "genres": "Fiction", "pageCount": 288},
    {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery", "author": "Barbara Allan", "language ": "English", "rating": 3.3, "publisher": "Kensington Publishing Corp.", "genres": "Mystery", "pageCount": 288},
    {"title": "A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)", "author": "George R.R. Martin", "language ": "English", "rating": 4.5, "publisher": "HarperCollins UK", "genres": "Fantasy", "pageCount": 4544}})

    
    sort_books_title(unsorted_book_data)
    >>>A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
    >>>Antiques Roadkill: A Trash 'n' Treasures Mystery
    >>>Antiques Roadkill: A Trash 'n' Treasures Mystery
    >>>The Painted Man (The Demon Cycle, Book 1)
    
    ''' 
    lst = [i for i in booklist.values()]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j]['title'] < lst[i]['title']:
                lst[i], lst[j] = lst[j], lst[i]
                
    for i in lst:
        print(i['title'])
    print("Dictionary sorted by title: " + str(lst))
    return 


#Function 2 by Joey Thomas 
def sort_books_ascending_rate(booklist: dict):
    ''' Returns a list with the book data stored as a 
    dictionary book where the books are sorted by rating in ascending order. 
    
    unsorted_book_data= dict({
    1 : {"title": "The Painted Man (The Demon Cycle, Book 1)", "author": "Peter V. Brett", "language ": "English", "rating": 4.5, "publisher": "HarperCollins UK", "genres": "Fiction", "pageCount": 544}, 
    2 : {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery", "author": "Barbara Allan", "language ": "English", "rating": 3.3, "publisher": "Kensington Publishing Corp.", "genres": "Fiction", "pageCount": 288},
    3 : {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery", "author": "Barbara Allan", "language ": "English", "rating": 3.3, "publisher": "Kensington Publishing Corp.", "genres": "Mystery", "pageCount": 288},
    4 : {"title": "A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)", "author": "George R.R. Martin", "language ": "English", "rating": 4.5, "publisher": "HarperCollins UK", "genres": "Fantasy", "pageCount": 4544}})

    
    sort_books_ascending_rate(unsorted_book_data)
    >>>3.3
    >>>3.3
    >>>4.5
    >>>4.5
    >>>Sorted by Rating : [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language ': 'English', 'rating': 3.3, 'publisher': 'Kensington ..Publishing Corp.', 'genres': 'Fiction', 'pageCount': 288}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language ': 'English', 'rating': ..3.3, 'publisher': 'Kensington Publishing Corp.', 'genres': 'Mystery', 'pageCount': 288}, {'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'language ': ..'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'genres': 'Fiction', 'pageCount': 544}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A ..Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'language ': 'English', 'rating': 4.5, 'publisher': ..'HarperCollins UK', 'genres': 'Fantasy', 'pageCount': 4544}]
    >>>    
    ''' 
    if (len(booklist) != 0):
        lst = [i for i in booklist.values()]
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[j]['rating'] < lst[i]['rating']:
                    lst[i], lst[j] = lst[j], lst[i]
        print('Sorted by Rating: ' + str(lst))   
        return 'Sorted by Rating'
    else: 
        print('An Error Occured')
        return 'An Error Occured'


#Function 3 by Hasan Suirya
def sort_books_publisher(booklist: dict):
    ''' Returns a list with the book data stored as a 
    dictionary book where the books are sorted alphabetically by publisher. 
    
    unsorted_book_data= dict({
    1 : {"title": "The Painted Man (The Demon Cycle, Book 1)", "author": "Peter V. Brett", "language ": "English", "rating": 4.5, "publisher": "HarperCollins UK", "genres": "Fiction", "pageCount": 544}, 
    2 : {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery", "author": "Barbara Allan", "language ": "English", "rating": 3.3, "publisher": "Kensington Publishing Corp.", "genres": "Fiction", "pageCount": 288},
    3 : {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery", "author": "Barbara Allan", "language ": "English", "rating": 3.3, "publisher": "Kensington Publishing Corp.", "genres": "Mystery", "pageCount": 288},
    4 : {"title": "A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)", "author": "George R.R. Martin", "language ": "English", "rating": 4.5, "publisher": "HarperCollins UK", "genres": "Fantasy", "pageCount": 4544}})

    sort_books_publisher(unsorted_book_data)
    >>>Dictionary sorted by publisher HarperCollins UK : [{'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'language ': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', ..'genres': 'Fiction', 'pageCount': 544}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance ..with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'language ': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'genres': 'Fantasy', 'pageCount': 4544}, ..{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language ': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'genres': ..'Mystery', 'pageCount': 288}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language ': 'English', 'rating': 3.3, 'publisher': 'Kensington ..Publishing Corp.', 'genres': 'Fiction', 'pageCount': 288}]
   ++++++++++++++++++++
    >>>

    '''    
    if (len(booklist) != 0):
        lst = [i for i in booklist.values()]
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[j]['publisher'] < lst[i]['publisher']:
                    lst[i], lst[j] = lst[j], lst[i]
                
            for i in lst:
                print('Dictionary sorted by publisher ' +i['publisher']+ ':' + str(lst))
                return 'Sorted by publisher'
    else:
        print('Error')
        return 'Error'


#Function 4 by Hasan Suriya
def sort_books_descending_rate(booklist: dict):
    ''' Returns a list with the book data stored as a 
    dictionary book where the books are sorted alphabetically by title. 
    
    unsorted_book_data= dict({
    1 : {"title": "The Painted Man (The Demon Cycle, Book 1)", "author": "Peter V. Brett", "language ": "English", "rating": 4.5, "publisher": "HarperCollins UK", "genres": "Fiction", "pageCount": 544}, 
    2 : {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery", "author": "Barbara Allan", "language ": "English", "rating": 3.3, "publisher": "Kensington Publishing Corp.", "genres": "Fiction", "pageCount": 288},
    3 : {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery", "author": "Barbara Allan", "language ": "English", "rating": 3.3, "publisher": "Kensington Publishing Corp.", "genres": "Mystery", "pageCount": 288},
    4 : {"title": "A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)", "author": "George R.R. Martin", "language ": "English", "rating": 4.5, "publisher": "HarperCollins UK", "genres": "Fantasy", "pageCount": 4544}})

    
    sort_books_descending_rate(unsorted_book_data)
    >>>Sorted in descending order by rating: [{'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'language ': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', ..'genres': 'Fiction', 'pageCount': 544}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance ..with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'language ': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'genres': 'Fantasy', 'pageCount': 4544}, ..{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language ': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'genres': ..'Mystery', 'pageCount': 288}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language ': 'English', 'rating': 3.3, 'publisher': 'Kensington ..Publishing Corp.', 'genres': 'Fiction', 'pageCount': 288}]
    ++++++++++++++++++++
    >>>
    '''    

    if (len(booklist) != 0):
        lst = [i for i in booklist.values()]
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[j]['rating'] > lst[i]['rating']:
                    lst[i], lst[j] = lst[j], lst[i]
        print('Sorted in descending order by rating:' + str(lst))   
        return 'Sorted in descending order by rating'
    else: 
        print('Error')    
        return 'Error'

#Function 5 by Corson Haywood
def sort_books_pageCount(booklist: dict):
    '''The function takes as an input parameter the dictionary where the books
    are stored.The function returns  a list with the book data stored as a 
    dictionary book where the books are sorted alphabetically by title. 
    The function will also print the data.
    
    unsorted_book_data= dict({
    1 : {"title": "The Painted Man (The Demon Cycle, Book 1)", "author": "Peter V. Brett", "language ": "English", "rating": 4.5, "publisher": "HarperCollins UK", "genres": "Fiction", "pageCount": 544}, 
    2 : {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery", "author": "Barbara Allan", "language ": "English", "rating": 3.3, "publisher": "Kensington Publishing Corp.", "genres": "Fiction", "pageCount": 288},
    3 : {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery", "author": "Barbara Allan", "language ": "English", "rating": 3.3, "publisher": "Kensington Publishing Corp.", "genres": "Mystery", "pageCount": 288},
    4 : {"title": "A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)", "author": "George R.R. Martin", "language ": "English", "rating": 4.5, "publisher": "HarperCollins UK", "genres": "Fantasy", "pageCount": 4544}})

    
    sort_books_pageCount(unsorted_book_data)
    >>>Dictionary sorted by : [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language ': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'genres': 'Fiction', 'pageCount': 288}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language ': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'genres': 'Mystery', 'pageCount': 288}, {'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'language ': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'genres': 'Fiction', 'pageCount': 544}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'language ': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'genres': 'Fantasy', 'pageCount': 4544}]
    '''    
    if (len(booklist) != 0):
        lst = [i for i in booklist.values()]
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[j]['pagecount'] < lst[i]['pagecount']:
                    lst[i], lst[j] = lst[j], lst[i]
        print('Sorted by pagecount: ' + str(lst))
        return 'Sorted by pagecount'
    else:
        print('An Error Occured')
        return 'An Error Occured' 



#Function 6 by Corson Haywood
def sort_books_category(booklist: dict):
    '''The function takes as an input parameter the dictionary where the books
    are stored.The function returns  a list with the book data stored as a 
    dictionary book where the books are sorted alphabetically by title. 
    The function will also print the data.
    
    unsorted_book_data= dict({
    1 : {"title": "The Painted Man (The Demon Cycle, Book 1)", "author": "Peter V. Brett", "language ": "English", "rating": 4.5, "publisher": "HarperCollins UK", "genres": "Fiction", "pageCount": 544}, 
    2 : {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery", "author": "Barbara Allan", "language ": "English", "rating": 3.3, "publisher": "Kensington Publishing Corp.", "genres": "Fiction", "pageCount": 288},
    3 : {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery", "author": "Barbara Allan", "language ": "English", "rating": 3.3, "publisher": "Kensington Publishing Corp.", "genres": "Mystery", "pageCount": 288},
    4 : {"title": "A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)", "author": "George R.R. Martin", "language ": "English", "rating": 4.5, "publisher": "HarperCollins UK", "genres": "Fantasy", "pageCount": 4544}})

    
    sort_books_category(unsorted_book_data)
    >>>Dictionary sorted by : [{'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'language ': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'genres': 'Fantasy', 'pageCount': 4544}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language ': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'genres': 'Fiction', 'pageCount': 288}, {'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'language ': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'genres': 'Fiction', 'pageCount': 544}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language ': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'genres': 'Mystery', 'pageCount': 288}]

    '''    
    if (len(booklist) != 0):
        lst = [i for i in booklist.values()]
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[j]['genre'] < lst[i]['genre']:
                    lst[i], lst[j] = lst[j], lst[i]
        print('Sorted by Category: ' + str(lst))
        return 'Sorted by Category'
    else:
        print('An Error Occured')
        return 'An Error Occured' 

