"""
Written by Shadman Sakib Rashid (101200114)
Reviewed by Corson Haywood (101193309), Joey Thomas (101200614),
Hasan Suriya (101193772)
12/10/2021- Version 1.0
"""


def book_category_dictionary_list(filename):
    """ In this case, the dictionary keys are the generes\categories such as Fiction, Fantasy, Biography,
    etc. The function will store the dictionary using the following format: book_dictionary = { "Fiction":[ {"title":
    "Antiques Roadkill: A Trash 'n' Treasures Mystery", "authors": " Barbara Allan", "language ": "English",
    "rating": 3.3, "publisher": " Kensington Publishing Corp.", "pageCount": 288 }, {another element}, ...


    >>>book_category_dictionary_list("Google_Books_Dataset.csv") ( 'Fiction', {'title': "Antiques Roadkill: A Trash
    'n' Treasures Mystery", 'authors': 'Barbara Allan', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.',
    'page_count': '288', 'language': 'English'}, 'Fiction', {'title': 'The Painted Man (The Demon Cycle, Book 1)',
    'authors': 'Peter V. Brett', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'page_count': '544', 'language':
    'English'}, 'Fiction', {'title': 'Edgedancer: From the Stormlight Archive', 'authors': 'Brandon Sanderson',
    'rating': '4.8', 'publisher': 'Tor Books', 'page_count': '226', 'language': 'English'}, 'Fiction',
    {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'authors': 'Andrzej Sapkowski', 'rating': '4.8',
    'publisher': 'Hachette UK', 'page_count': '400', 'language': 'English'}, 'Comics', {'title': 'Deadpool Kills the
    Marvel Universe', 'authors': 'Cullen Bunn', 'rating': '4.2', 'publisher': 'Marvel Entertainment', 'page_count':
    '96', 'language': 'English'}, ...) """
    import csv
    books = {}
    with open(filename, 'r') as file:
        read = csv.reader(file)

        for row in read:
            class_data = {}
            for i in range(1, len(row)):
                if i == 1:
                    class_data["title"] = row[1]
                elif i == 2:
                    class_data["authors"] = row[2]
                elif i == 3:
                    class_data["language"] = row[3]
                elif i == 4:
                    class_data["rating"] = row[4]
                elif i == 5:
                    class_data["publisher"] = row[5]
                elif i == 6:
                    class_data["pageCount"] = row[6]
            books[row[0]] = []
            books[row[0]].append(class_data)
        book_list = sorted(books.items())
        final_book_list = []
        for i in book_list:
            if i not in final_book_list:
                final_book_list.append(i)

    return final_book_list


book_category_dictionary_list('Google_Books_Dataset.csv')
