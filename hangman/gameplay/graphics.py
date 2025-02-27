# from gameplay.game import Game



class Graphics:
    """Output stylish graph

    prints out progress in graph based on lives
    printGR function takes integer atribute from 1 to 6 and prints out graphic.

    Typical usage example:

    graph = Graphics()
    graph.printGR(lives)
    """

    def __init__(self):
        self.lives = 6

    def printGR(self, lives):
        if lives == 6:
                print('''													  \n'''
        '''					        _________________			      \n'''
        '''					        |			      \n'''
        '''					        |			      \n''')
        elif lives == 5:
                print('''													  \n'''
        '''					        _________________			      \n'''
        '''					        |			      \n'''
        '''					        |			      \n'''
        '''					_________________			      \n'''
        '''					|   0       0   |			      \n'''
        '''					|       |       |			      \n'''
        '''					|      ---      |			      \n'''
        '''					|_______________|			      \n''')
        elif lives == 4:
                  print('''													  \n'''
        '''					        _________________			      \n'''
        '''					        |			      \n'''
        '''					        |			      \n'''
        '''					_________________			      \n'''
        '''					|   0       0   |			      \n'''
        '''					|       |       |			      \n'''
        '''					|      ---      |			      \n'''
        '''					|_______________|			      \n'''
        '''					        |                         \n'''
        '''					        |                         \n'''
        '''					        |                         \n'''
        '''					        |                         \n'''
        '''					        |                         \n'''              
        '''					        |                         \n'''              
        '''					        |                         \n'''              
        '''					        |                         \n'''              
        '''					        |                         \n''' 
        '''					        |                         \n''' )
        elif lives == 3:
                 print('''													  \n'''
        '''					        _________________			      \n'''
        '''					        |			      \n'''
        '''					        |			      \n'''
        '''					_________________			      \n'''
        '''					|   0       0   |			      \n'''
        '''					|       |       |			      \n'''
        '''					|      ---      |			      \n'''
        '''					|_______________|			      \n'''
        '''					        |                         \n'''
        '''					        |                         \n'''
        '''					        |                         \n'''
        '''				    |___________|             \n'''
        '''					        |                         \n'''              
        '''					        |                         \n'''              
        '''					        |                         \n'''              
        '''					        |                         \n'''              
        '''					        |                         \n''' 
        '''					        |                         \n''' )
        elif lives == 2:
                 print('''													  \n'''
        '''					        _________________			      \n'''
        '''					        |			      \n'''
        '''					        |			      \n'''
        '''					_________________			      \n'''
        '''					|   0       0   |			      \n'''
        '''					|       |       |			      \n'''
        '''					|      ---      |			      \n'''
        '''					|_______________|			      \n'''
        '''					        |                         \n'''
        '''					        |                         \n'''
        '''					        |                         \n'''
        '''				    |___________|___________|             \n'''
        '''					        |                         \n'''              
        '''					        |                         \n'''              
        '''					        |                         \n'''              
        '''					        |                         \n'''              
        '''					        |                         \n''' 
        '''					        |                         \n''' )
        elif lives == 1:
                       print('''													  \n'''
        '''					        _________________			      \n'''
        '''					        |			      \n'''
        '''					        |			      \n'''
        '''					_________________			      \n'''
        '''					|  0        0   |			      \n'''
        '''					|       |       |			      \n'''
        '''					|      ---      |			      \n'''
        '''					|_______________|			      \n'''
        '''					        |                         \n'''
        '''					        |                         \n'''
        '''					        |                         \n'''
        '''				    |___________|___________|             \n'''
        '''					        |                         \n'''              
        '''					        |                         \n'''              
        '''					        |                         \n'''              
        '''					        |                         \n'''              
        '''					        |                         \n''' 
        '''					        |                         \n''' 
        '''					       | |                         \n'''               
        '''					      |                            \n'''                             
        '''					    |                          \n'''                             
        '''					   |                             \n'''                                           
        '''					   |                             \n'''                                           
        '''					   |                             \n'''                                           
        '''					   |                             \n'''                                                         
        '''					   |                             \n'''                                           
        '''					   |                             \n'''                                           
        '''					___|                             \n'''                                                         
        '''	                                                  \n''')
        elif lives == 0:
                        print('''													  \n'''
        '''					        _________________			      \n'''
        '''					        |			      \n'''
        '''					        |			      \n'''
        '''					_________________			      \n'''
        '''					|   --     --   |			      \n'''
        '''					|       |       |			      \n'''
        '''					|     /---\     |			      \n'''
        '''					|_______________|			      \n'''
        '''					        |                         \n'''
        '''					        |                         \n'''
        '''					        |                         \n'''
        '''				    |___________|___________|             \n'''
        '''					        |                         \n'''              
        '''					        |                         \n'''              
        '''					        |                         \n'''              
        '''					        |                         \n'''              
        '''					        |                         \n''' 
        '''					        |                         \n''' 
        '''					       | |                         \n'''               
        '''					      |   |                         \n'''                             
        '''					    |       |                         \n'''                             
        '''					   |         |                         \n'''                                           
        '''					   |         |                         \n'''                                           
        '''					   |         |                         \n'''                                           
        '''					   |         |                         \n'''                                                         
        '''					   |         |                         \n'''                                           
        '''					   |         |                         \n'''       )                      