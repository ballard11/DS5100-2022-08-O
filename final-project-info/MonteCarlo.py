import numpy as np
import pandas as pd
import random as rm

class Die():

    def __init__(self, faces):
        """"" This is the Create_Die docstring
        
        Attributes
        ==========
        faces: int or str
            the number of str on the face of the 'die'
        weights: int
            weight of each corresponding face, relating to liklihood of rolling that face.
        
        Methods
        =======
        change_weight:
            changes the weight of the die
        roll_die:
            plays the dice 'game'
        show:
            shows the results

        """
        
    # The Initializer Method: Takes an array of faces as an argument.
           
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
          #  'Face':range(1,self.n_faces+1),
            'Face':faces,
            'Weight':self.weights})


    def change_weight(self, f_change, weight):
        """ f_change is the name of the face - it could be a str or int"""
        # Changes_Weight Method: changes the weight of a single face provided (x) - Seems to work overall. 

        weight = float(weight)

        #Re-evaluate for string
        if f_change in self.faces:
            #self.my_die.loc[df['Face'] == f_change , "Weight" ] = weight
            self.my_die.loc[self.my_die['Face'] == f_change , "Weight" ] = weight

            #I'm finding 'H/T' and changing the weight.
            print(self.my_die)
        else:
            print("Value is not on the Die.  (i.e. User provided value is not in the array.)")
            #Raise an Error instead.

            
    def roll_die(self, n_rolls=1):
        """A method to roll the die one or more times. """
        Rolled_faces_and_weights_df = self.my_die.sample(n=n_rolls, replace = True, weights = "Weight").reset_index(drop= True)
        return list(Rolled_faces_and_weights_df['Face'])    

                                                
    def show(self, wide_or_narrow = "wide"):
        """A method to show the user the dies current set of faces and weights (since the latter can be changed). """   
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
    
    def __init__(self,die_list):
        """Game class docstring: A game consists of rolling of one or more dice of the same kind one or more times.
        
        Attributes
        ==========
        die list:
            Must be passed a list of die created using the Die class.
        faces: int or str
        weights: int
        
        Methods
        =======
        play:
            Takes a parameter to specify how many times the dice should be rolled.
        get_results:
            method shows the user the results of the most recent play.        
        
        """      
        self.die_list=die_list
        self.num_rolls = len(die_list)
        self.results = pd.DataFrame()
        self.my_die = pd.DataFrame()                      

    def play(self, num_rolls):
        self.my_die.index.rename("Roll Number", inplace = True)
        
        for die in range(0, len(self.die_list)):
            self.my_die[die] = self.die_list[die].roll_die(num_rolls)
        
    
    def get_results(self, wide_or_narrow = "wide"):
       # A method to show the user the die’s current set of faces and weights (since the latter can be changed). (X)
       # Returns the dataframe created in the initializer but possibly updated by the weight changing method. (X)
    
        if wide_or_narrow == 'wide':
            return self.my_die
        
        elif wide_or_narrow =='narrow':
            my_die_narrow = self.my_die.stack().to_frame('Faces')
            my_die_narrow.index.rename(["Roll Number","Die"], inplace = True)
            return my_die_narrow
        else:
            raise ValueError("Arrgument must be either \"narrow\" or \"wide\"")
    
    
    class Analyzer(Game): 
    """An analyzer takes the results of a single game and computes various descriptive statistical properties about it.
            
        Methods
        =======
        get_face_count:
            A face counts per roll method to compute how many times a given face is rolled in each event.
        get_permutation:
            A combo method to compute the distinct combinations of faces rolled, along with their counts.
        get_jackpot:
            A jackpot method to compute how many times the game resulted in all faces being identical.

        """
    
    def __init__(self, game):
        self.game_results = game.get_results()
        self.number_of_dice = len(list(self.game_results))
 
        self.face_count = pd.DataFrame()
        self.jackpot = 0
        self.combos = {}
        self.temp_df = pd.DataFrame()
    
        number_of_dice = 0


    def get_face_count(self):
        """A face counts per roll, i.e. the number of times a given face appeared in each roll. 
         For example, if a roll of five dice has all sixes, then the counts for this roll would be 6 for the face value '6' and 0 for the other faces."""
        self.temp_df = pd.DataFrame(self.game_results.transpose().melt(var_name='rolls',value_name='faces'))
        self.face_counts = pd.crosstab(index=self.temp_df['rolls'],columns=self.temp_df['faces'])
        return self.face_counts
    
    def get_combo(self):
        """A combo count, i.e. how many combination types of faces were rolled and their counts."""
        face_count = self.get_face_count()  
        listtest = face_count.values.tolist()
        for i in listtest:
            value_string = ' '.join(str(e) for e in i)
            self.combos[value_string] = listtest.count(i)    
        return self.combos
          
    def get_jackpot(self, game):
        """A jackpot count, i.e. how many times a roll resulted in all faces being the same, e.g. six ones for a six-sided die."""
        # iterate over the resulting dataframe and find any time a value includes the number of dice rolled and every time that's true you add to jackpot
        face_count = self.get_face_count()
        listtest = face_count.values.tolist()
        print(game.num_rolls)
        for i in listtest:
            if game.num_rolls in i:
                self.jackpot += 1
        return self.jackpot    
    
        
if __name__ == '__main__':
    unittest.main()