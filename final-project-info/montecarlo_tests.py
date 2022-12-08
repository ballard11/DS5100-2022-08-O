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
        ######################
        testdie = [1,2]
        df1 = Die(testdie)
        df1.change_weight(1,2)
        df2 = pd.DataFrame({'Face':[1,2],'Weight':[2,1]})
        self.assertTrue(df1, df2)     
        
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
                                   