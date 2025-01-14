import unittest
from booklover import BookLover
import pandas as pd

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test1 = BookLover("Ben","bkq5nt@virginia.edu","History")
        test1.add_book("Harry Potter",1)       
        actual = test_1.book_list
        
        #Build Expected - to Test
        book_list = pd.DataFrame({'Harry Potter':[], 1:[]})
        expected = BookLover("Ben","bkq5nt@virginia.edu","History",book_list)
        self.assertEqual(actual.book_list, expected.book_list)
        
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test2 = BookLover("Ben","bkq5nt@virginia.edu","History")
        test2.add_book("Harry Potter",1)       
        test2.add_book("Harry Potter",1)                

        count = test2.book_list['book_name'].value_counts()["Harry Potter"]
        self.assertEqual(count, 1)
        
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test3 = BookLover("Ben","bkq5nt@virginia.edu","History")
        test3.add_book("Harry Potter",1)       
        Result = test3.has_read("Harry Potter")        
        
        self.assertEqual(Result, True)

        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test4 = BookLover("Ben","bkq5nt@virginia.edu","History")
        test4.add_book("Harry Potter",1)       
        Result = test4.has_read("Harry Potter 2: The Pottering Returns")        
        
        self.assertEqual(Result, False)
        
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test5 = BookLover("Ben","bkq5nt@virginia.edu","History")
        test5.add_book("Harry Potter",1)       
        test5.add_book("Harry Potter 2",1.5) 
        test5.add_book("Harry Potter 3",2)       
        test5.add_book("Harry Potter 4",0) 
        test5.add_book("Harry Potter 5",0) 

        numbooks = test5.book_list.shape[0]
        self.assertEqual(numbooks, 5)

        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test6 = BookLover("Ben","bkq5nt@virginia.edu","History")
        test6.add_book("Harry Potter",3.5)       
        test6.add_book("Harry Potter 2",4) 
        test6.add_book("Harry Potter 3",5)       
        test6.add_book("Harry Potter 4",3) 
        test6.add_book("Harry Potter 5",4) 
        
        return fav['book_rating'] > 3
        
        
if __name__ == '__main__':
    unittest.main(verbosity=3)
