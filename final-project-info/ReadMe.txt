This is the Read Me file for Ben's Final Project in DS 5100.  This project ties together key concepts learned in the course for programming in Python.


Name: Ballard's Monte Carlo Simulator).

Synopsis: The project utilizes features 3 classes acting as a Monte Carlo simulation.
    
installing: 

To install run !pip install -e. 

Importing: 

To import the packages call import MonteCarlo

Creating dice objects:



Playing games:

Analyzing games:

API description:

A list of all classes with their public methods and attributes.

First Class is the Die Class.  

class Die(builtins.object)
 |  Die(faces)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, faces)
 |      This is the Create_Die docstring
 |      
 |      Attributes
 |      ==========
 |      faces: int or str
 |          the number of str on the face of the 'die'
 |      weights: int
 |          weight of each corresponding face, relating to liklihood of rolling that face.
 |      
 |      Methods
 |      =======
 |      change_weight:
 |          changes the weight of the die
 |      roll_die:
 |          plays the dice 'game'
 |      show:
 |          shows the results
 |  
 |  change_weight(self, f_change, weight)
 |      f_change is the name of the face - it could be a str or int
 |  
 |  roll_die(self, n_rolls=1)
 |      A method to roll the die one or more times.
 |  
 |  show(self, wide_or_narrow='wide')
 |      A method to show the user the dies current set of faces and weights (since the latter can be changed).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)


The second class it the Game Class: 

class Game(Die)
 |  Game(die_list)
 |  
 |  Method resolution order:
 |      Game
 |      Die
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, die_list)
 |      Game class docstring: A game consists of rolling of one or more dice of the same kind one or more times.
 |      
 |      Attributes
 |      ==========
 |      die list:
 |          Must be passed a list of die created using the Die class.
 |      faces: int or str
 |      weights: int
 |      
 |      Methods
 |      =======
 |      play:
 |          Takes a parameter to specify how many times the dice should be rolled.
 |      get_results:
 |          method shows the user the results of the most recent play.
 |  
 |  get_results(self, wide_or_narrow='wide')
 |  
 |  play(self, num_rolls)
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Die:
 |  
 |  change_weight(self, f_change, weight)
 |      f_change is the name of the face - it could be a str or int
 |  
 |  roll_die(self, n_rolls=1)
 |      A method to roll the die one or more times.
 |  
 |  show(self, wide_or_narrow='wide')
 |      A method to show the user the dies current set of faces and weights (since the latter can be changed).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Die:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)


Finally, the Analyzer class.

class Analyzer(Game)
 |  Analyzer(game)
 |  
 |  An analyzer takes the results of a single game and computes various descriptive statistical properties about it.
 |      
 |  Methods
 |  =======
 |  get_face_count:
 |      A face counts per roll method to compute how many times a given face is rolled in each event.
 |  get_permutation:
 |      A combo method to compute the distinct combinations of faces rolled, along with their counts.
 |  get_jackpot:
 |      A jackpot method to compute how many times the game resulted in all faces being identical.
 |  
 |  Method resolution order:
 |      Analyzer
 |      Game
 |      Die
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, game)
 |      Game class docstring: A game consists of rolling of one or more dice of the same kind one or more times.
 |      
 |      Attributes
 |      ==========
 |      die list:
 |          Must be passed a list of die created using the Die class.
 |      faces: int or str
 |      weights: int
 |      
 |      Methods
 |      =======
 |      play:
 |          Takes a parameter to specify how many times the dice should be rolled.
 |      get_results:
 |          method shows the user the results of the most recent play.
 |  
 |  get_combo(self)
 |      A combo count, i.e. how many combination types of faces were rolled and their counts.
 |  
 |  get_face_count(self)
 |      A face counts per roll, i.e. the number of times a given face appeared in each roll. 
 |      For example, if a roll of five dice has all sixes, then the counts for this roll would be 6 for the face value '6' and 0 for the other faces.
 |  
 |  get_jackpot(self, game)
 |      A jackpot count, i.e. how many times a roll resulted in all faces being the same, e.g. six ones for a six-sided die.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Game:
 |  
 |  get_results(self, wide_or_narrow='wide')
 |  
 |  play(self, num_rolls)
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Die:
 |  
 |  change_weight(self, f_change, weight)
 |      f_change is the name of the face - it could be a str or int
 |  
 |  roll_die(self, n_rolls=1)
 |      A method to roll the die one or more times.
 |  
 |  show(self, wide_or_narrow='wide')
 |      A method to show the user the dies current set of faces and weights (since the latter can be changed).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Die:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)



