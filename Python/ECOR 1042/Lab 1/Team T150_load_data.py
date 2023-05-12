''' Written by Shadman Sakib Rashid (101200114)
    Reviewed by Corson Haywood (101193309), Joey Thomas (101200614), 
    Hasan Suriya (101193772)
    Code Review: The keys are not set up properly, the output isn't a set, 
    and the dictionary isn't a list
'''

#function Definition
def book_catagory_dictionary_list(data_file:str):

    ''' This function returns the list with Book genere/catagory as key and the
    other columbs in the data sheet as the values.
    '''
    import csv
    genere_index = tuple()
    file_csv = open(data_file)
    reader= csv.reader(file_csv)
    next(reader)
    for columb in reader:



        class_data = {}

        genere_index = genere_index + (columb[6],class_data,) 

        class_data['title'] = (columb[1])

        class_data['authors'] = (columb[2])

        class_data['rating'] = (columb[3])

        class_data['publisher'] = (columb[4])

        class_data['page_count'] = (columb[5])

        class_data['language'] = (columb[7])

    return genere_index

#Main Script
g=book_catagory_dictionary_list("Google_Books_Dataset.csv")
print(g)