''' Muhammad Hasan Suriya - 101193772 - T- 150 '''


#Function Definitions
def book_tuple_dictionary(file :str):
    ''' Input the name of the file which is stored inside the folder of the 
    code, and get a return of a dictionary. 
    
    >>>book_tuple_dictionary('books')
    book_tuple = ({'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 
    'author': 'Barbara Allan', 'rating': '3.3', 'publisher': 
    'Kensington Publishing Corp.', 'page_count': 
    '288', 'generes': 'Fiction', 'language': 'English'}, ... )
    '''
    import csv
    with open(file) as i: 
        records = list(csv.DictReader(i))

    for book_tuple in records:  
        book_tuple.pop('')

        book_tuple = 'book_tuple = ' + str(tuple(records))
    return book_tuple

