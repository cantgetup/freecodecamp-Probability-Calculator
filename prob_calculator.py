import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **kwargs):
        self.contents = []
        
        for key in kwargs:
            for value in range(kwargs[key]):
                self.contents.append(key)
        
        # record original contents
        self.original_contents = self.contents.copy()
                
                
    def draw(self, num_balls_drawn):
        hat_list = self.contents
        my_draw = []
        
        if num_balls_drawn >= len(hat_list):
            return self.contents
        
        else:        
            for j in range(num_balls_drawn):
                random_ball = random.choice(hat_list)
                hat_list.remove(random_ball)
                my_draw.append(random_ball)
        
        return my_draw

    
    def __str__(self):
        a = ''
        
        for ball in self.contents:
            a = a + ball + ', '
            
        return a


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    # count
    m = 0    
    
    for i in range(num_experiments):        
        
        # reset hat
        hat.contents = hat.original_contents.copy()
        
        # draw balls
        my_draw = hat.draw(num_balls_drawn)

        # count balls in my_draw
        draw_count = {}
        for ball in my_draw:
            draw_count[ball] = draw_count.get(ball, 0) + 1


        # compare to expected_balls
        check_balls = [expected_balls[ball] <= draw_count.get(ball, -1) for ball in expected_balls]

        if len(expected_balls) == sum(check_balls):
            m = m + 1
    
    return m/num_experiments
