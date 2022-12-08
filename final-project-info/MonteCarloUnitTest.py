import unittest 
import numpy as np
import pandas as pd
import random as rm
from MonteCarlo import Die,Game,Analyzer

class MonteCarloTest(unittest.TestCase):
    
    def test_1_Die_create_die(self):    
        testdie = [1,2]
        df1 = Die(testdie)
        df2 = pd.DataFrame({'Face':[1,2],'Weight':[1,1]})
        self.assertTrue(df1, df2) 
        
    def test_2_Die_change_weight(self):
        testdie = [1,2]
        df1 = Die(testdie)
        df1.change_weight(1,2)
        df2 = pd.DataFrame({'Face':[1,2],'Weight':[2,1]})
        self.assertTrue(df1, df2)      
        
    def test_3_Die_show(self):
        testdie = [1,2]
        df1 = Die(testdie)
        df1.change_weight(1,2)
        df2 = pd.DataFrame({'Face':[1,2],'Weight':[2,1]})
        self.assertTrue(df1, df2)     
        
    def test_4_Die_roll_die(self):
        first = Die(["1","2","3",4,5,6,7,8,9,10,11,12])
        df1=len(first.roll_die(3))
        df2=3
        self.assertTrue(df1, df2)     
        
    def test_5_Die_show(self):           
        sixsided = [1,2,3,4,5,6]
        testdie1 = Die(sixsided)
        testdie1.roll_die(2)
        testdie1.show()
        df1=len(testdie1.show())
        df2=6
        self.assertTrue(df1, df2)     
        
    def test_6_Game_play(self):
        first = Die(["1","2","3",4])
        second = Die([1,2,3,4])
        third = Die([1,2,3,4])
        testGame=Game([first,second,third])
        testGame.play(1000)
        df1=len(testGame.my_die)
        df2=1000
        self.assertTrue(df1, df2)     

    def test_7_Game_show(self):
        first = Die(["1","2","3",4,5,6,7,8,9,10,11,12])
        second = Die([1,2,3,4,5,6,7,8,9,10,11,12])
        third = Die([1,2,3,4,5,6,7,8,9,10,11,12])
        testGame=Game([first,second,third])
        testGame.play(10)
        testGame.get_results("wide")
        df1=len(testGame.show())
        df2=10
        self.assertTrue(df1, df2)     
    
    def test_8_Analyzer_get_face_count(self):
        first = Die(["1","2","3",4,5,6,7,8,9,10,11,12])
        second = Die([1,2,3,4,5,6,7,8,9,10,11,12])
        third = Die([1,2,3,4,5,6,7,8,9,10,11,12])
        testGame=Game([first,second,third])
        testGame.play(10)
        testGame.get_results("wide")
        analysis = Analyzer(testGame)
        df1=len(analysis.get_face_count())
        df2=1000
        self.assertTrue(df1, df2)     
    
    def test_9_Analyzer_get_jackpot_Analyzer(self):
        first = Die(["1","2","3",4,5,6,7,8,9,10,11,12])
        second = Die([1,2,3,4,5,6,7,8,9,10,11,12])
        third = Die([1,2,3,4,5,6,7,8,9,10,11,12])
        testGame=Game([first,second,third])
        testGame.play(10)
        testGame.get_results("wide")
        analysis = Analyzer(testGame)
        df1=len(analysis.get_combo())
        df2=21
        self.assertTrue(df1, df2)         
    
    def test_9_Analyzer_get_combo(self):
        first = Die(["1","2","3",4,5,6,7,8,9,10,11,12])
        second = Die([1,2,3,4,5,6,7,8,9,10,11,12])
        third = Die([1,2,3,4,5,6,7,8,9,10,11,12])
        testGame=Game([first,second,third])
        testGame.play(10)
        testGame.get_results("wide")
        analysis = Analyzer(testGame)
        df1=len(analysis.get_combo())
        df2=21
        self.assertTrue(df1, df2)    
        #https://python.plainenglish.io/unit-tests-with-pandas-bf4c596baeda

if __name__ == '__main__':
    unittest.main()
                                   