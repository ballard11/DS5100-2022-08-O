import unittest 
import numpy as np
import pandas as pd
import random as rm
from MonteCarlo import Die,Game,Analyzer

class MonteCarloTest(unittest.TestCase):
    
    def test_1_Die_create_die(self):    
        sixsided = [1,2,3,4,5,6]
        testdie1 = Die(sixsided)
        
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
        

if __name__ == '__main__':
    unittest.main()
                                   
        
if __name__ == '__main__':
    pass

