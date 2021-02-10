import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **kwargs):
        self.content = []
        
        for key in kwargs:
            for value in range(kwargs[key]):
                self.content.append(key)
    
    def __str__(self):
        a = ''
        
        for ball in self.content:
            a = a + ball + ', '
            
        return a


#def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
