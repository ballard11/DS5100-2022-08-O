import unittest 
import numpy as np
import pandas as pd
import random as rm
from MonteCarlo import Die,Game,Analyzer

class MonteCarloTest(unittest.TestCase):
    
    def test_1_Die_create_die(self):    
        testdie = [1,2]
        df2 = Die(testdie)
        df1 = pd.DataFrame({'Face':[1,2],'Weight':[1,2]})
        self.assertTrue(df1, df2)

 # add a book and test if it is in `book_list`.
        test1 = BookLover("Ben","bkq5nt@virginia.edu","History")
        test1.add_book("Harry Potter",1)       
        actual = test_1.book_list
        
        #Build Expected - to Test
        book_list = pd.DataFrame({'Harry Potter':[], 1:[]})
        expected = BookLover("Ben","bkq5nt@virginia.edu","History",book_list)
        self.assertEqual(actual.book_list, expected.book_list)
        
        
        
df = pd.DataFrame({"col1": ["sap", "hi"], "col2": [3, 4]})
startswith_s(df, "col1", "col1_startswith_s")
expected = pd.Series([True, False], name="col1_startswith_s")
pd.testing.assert_series_equal(df["col1_startswith_s"], expected)

        
        
    def test_2_Die_change_weight(self):
        firstDie = Die(["1","2","3",4,5,6,7,8,9])
        firstDie.change_weight(9,"6")        
        
    def test_4_Die_roll_die(self):
        firstDie = Die(["1","2","3",4,5,6,7,8,9])
        firstDie.roll_die2(4)
        
    def test_5_Die_show(self):           
        firstDie = Die(["1","2","3",4,5,6,7,8,9])
        firstDie.show("narrow")
        firstDie.show("wide")
    
    def test_6_Game_play(self):
        first = Die(["1","2","3",4])
        second = Die([1,2,3,4])
        third = Die([1,2,3,4])
        testGame=Game([first,second,third])
        testGame.play2(3)
    
    def test_7_Game_show(self):
    
    def test_8_Analyzer_get_face_count(self):
    
    def test_9_Analyzer_get_jackpot_Analyzer(self):
    
    def test_9_Analyzer_get_combo(self):

    #https://python.plainenglish.io/unit-tests-with-pandas-bf4c596baeda

if __name__ == '__main__':
    unittest.main()
                                   

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