import unittest
import pandas as pd

class BookLover:
    """this is the BookLover class"""

    def __init__(self, name, email, fav_genre, num_books = 0, book_list = None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    #Method 1
    def add_book(self, book_name, rating):
        if self.book_list["book_name"].eq(book_name).any():
            print("This book is already in the dataframe.")
        else:           
            update_list = {'book_name': book_name, 'book_rating': rating}
            print(update_list)

            self.book_list = self.book_list.append(update_list, ignore_index = True)
            return self.book_list
    
    #Method 2
    def has_read(self, book_name):       
        if self.book_list["book_name"].eq(book_name).any():
            #print ("Found")   
            return True
        else:    
            return False
    
    #Method 3
    def num_books_read(self):
        return self.num_books
    
    #Method 4
    def fav_books(self):
        favbooks = test6.book_list[test6.book_list['book_rating'] > 3]
        return favbooks

    
if __name__ == '__main__':
    unittest.main()
    print("hello")

  #  unittest = BookLover("Ben","bkq5nt@virginia.edu","History")
  #  unittest.add_book("Harry Potter")