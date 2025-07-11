import copy
import random

class Hat:
    
    

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []

        for color in self.kwargs.keys():
            count = self.kwargs[color]
            
            self.contents += [color for _ in range(count)]
            

    def draw(self, balls):
        drawn_balls = []
        if balls > len(self.contents):
            all_contents = self.contents
            self.contents = []
            return all_contents

        for _ in range(balls):
            rand = random.randint(0, len(self.contents) - 1)
            drawn_balls.append(self.contents[rand])
            self.contents.pop(rand)

        return drawn_balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    
    for _ in range(num_experiments):
        
        copyhat = copy.deepcopy(hat)
        draw = copyhat.draw(num_balls_drawn)
        
        count = 0
        for color, ball_count in expected_balls.items():
            if draw.count(color) < ball_count:
                break
            elif count != len(expected_balls) - 1:
                count += 1
            else: 
                success += 1
        
    print(success)
    return (success)/num_experiments


hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=20)
print(probability)