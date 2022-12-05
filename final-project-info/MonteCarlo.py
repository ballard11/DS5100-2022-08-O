import numpy as np
import pandas as pd
import random as rm

class Die():
    """"" This class represents a Die """

    def __init__(self, faces):
        """"" This is the Create_Die docstring"""
                   
        flag = len(set(faces)) == len(faces)
        if flag == 0:
            raise ValueError("Each value must be Unique.") 
    
        #Faces
        #Asigns FACES to self, the length of the User Inputted array
        self.faces = faces
        self.n_faces = len(faces)
        self.weights = np.ones(len(faces))
    
        #Create Dataframe to save values        
        self.my_die= pd.DataFrame({
            'Face':range(1,self.n_faces+1),
            'Weight':self.weights})


    def change_weight(self, f_change, weight):
        # Changes_Weight Method: changes the weight of a single face provided (x) - Seems to work overall. 
        
        weight = float(weight)
        
        if f_change in self.faces:
            f_change = f_change - 1
            weight = float(weight)
            
            self.weights[f_change]=weight
            self.my_die = pd.DataFrame({
                'Face':range(1,self.n_faces+1),
                'Weight':self.weights})
            print(self.my_die)
        else:
            print("Value is not on the Die.  (i.e. User provided value is not in the array.)")

    def roll_die(self, n_rolls=1):
        Rolled_faces_and_weights_df = self.my_die.sample(n=n_rolls, replace = True, weights = "Weight").reset_index(drop= True)
        return list(Rolled_faces_and_weights_df['Face'])    

                                                
    def show(self, wide_or_narrow = "wide"):
       # A method to show the user the die’s current set of faces and weights (since the latter can be changed). (X)
    
        if wide_or_narrow == 'wide':
            return self.my_die
        
        elif wide_or_narrow =='narrow':
            my_die_narrow = self.my_die.stack().to_frame('Faces')
            my_die_narrow.index.rename(["Roll Number","Dice"], inplace = True)
            return my_die_narrow
        else:
            raise ValueError("Arrgument must be either \"narrow\" or \"wide\"")
    
        print(self.my_die)

        
        
class Game(Die): 
    """"" This class takes Dies and simulates a game."""

    def __init__(self,die_list):
        """Game class docstring: A game consists of rolling of one or more dice of the same kind one or more times."""      
        self.die_list=die_list       
        self.results = pd.DataFrame()
                        

    def play(self, num_rolls):
        self.my_die = pd.DataFrame()
        self.my_die.index.rename("Roll Number", inplace = True)
        
        for die in range(0, len(self.die_list)):
            self.my_die[die] = self.die_list[die].roll_die(num_rolls)
        
    
    def show(self, wide_or_narrow = "wide"):
        """"" This method shows the state of the Die."""

       # A method to show the user the die’s current set of faces and weights (since the latter can be changed). (X)
       # Returns the dataframe created in the initializer but possibly updated by the weight changing method. (X)
    
        if wide_or_narrow == 'wide':
            return self.my_die
        
        elif wide_or_narrow =='narrow':
            my_die_narrow = self.my_die.stack().to_frame('Faces')
            my_die_narrow.index.rename(["Roll Number","Dice"], inplace = True)
            return my_die_narrow
        else:
            raise ValueError("Arrgument must be either \"narrow\" or \"wide\"")
    
    
class Analyzer(Game): 

    face_count = pd.DataFrame()
    jackpot = pd.DataFrame()
    combos = pd.DataFrame()

    number_of_dice = 0

    game_results = pd.DataFrame()
    temp_df = pd.DataFrame()
    
    def __init__(self, game):
        self.game_results = game.show()
        self.number_of_dice = len(list(self.game_results))
        
    def get_face_count(self):
        self.temp_df = pd.DataFrame(self.game_results.transpose().melt(var_name='rolls',value_name='faces'))
        self.face_counts = pd.crosstab(index=self.temp_df['rolls'],columns=self.temp_df['faces'])
                
    def get_jackpot(self):
        temp_df_2 = self.temp_df.groupby(['rolls','faces'], as_index = False).value_counts()
        self.jackpots = temp_df_2.loc[temp_df_2['count'] == self.number_of_dice]
        return len(self.jackpots)    
    
    def get_combo(self):
        self.combos = self.face_counts.groupby(list(self.face_counts), as_index = False).value_counts()
        
        
        
if __name__ == '__main__':
    unittest.main()