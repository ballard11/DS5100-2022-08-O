import unittest 
import numpy as np
import pandas as pd
import random as rm
from MonteCarlo import Die,Game,Analyzer

class MonteCarloTest(unittest.TestCase):
    
    def test_1_Die_create_die(self):    
        sixsided = [1,2,3,4,5,6]
        testdie1 = Die(sixsided)
        testdie2 = Die(sixsided)
        testdie3 = Die(sixsided)
        testdie4 = Die(sixsided)
        testdie5 = Die(sixsided)
        testdie6 = Die(sixsided)
        testdielist = [testdie1,testdie2,testdie3,testdie4]
        
        
        testgame = Game(testdielist)
        actualresults = testgame.show("wide")
    
    
        #pandas unit test
        #pandas built in function
        #grab columns, convert to list, 
        
        expected = pd.DataFrame({
            'Face':range(1,self.n_faces+1),
            'Weight':self.weights})
        
        self.assertEqual(actualresults, expected)
        
        
    def test_2_Die_change_weight(self):
        
    def test_3_Die_change_weight(self):

    def test_4_Die_roll_die(self):
    
    def test_5_Die_show(self):           
    
    def test_6_Game_play(self):
    
    def test_7_Game_show(self):
    
    def test_8_Analyzer_get_face_count(self):
    
    def test_9_Analyzer_get_jackpot_Analyzer(self):
    
    def test_9_Analyzer_get_combo(self):
        

if __name__ == '__main__':
    unittest.main()
                                   
        
if __name__ == '__main__':
    pass

