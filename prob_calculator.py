import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **arguments):
    self.contents = []
    for key, val in arguments.items():
      for i in range(val):
        self.contents.append(key)

  def draw(self, number):
    drawn = []
    if number > len(self.contents):
      return self.contents
    else:
      for i in range(number):
        drawn.append(self.contents.pop(random.randrange(len(self.contents))))
      return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  n = num_experiments
  m = 0

  for i in range(n):
    new_hat = copy.deepcopy(hat)
    balls_drawn = new_hat.draw(num_balls_drawn)
    
    count = 0
    for key, val in expected_balls.items():
      if balls_drawn.count(key) >= val:
        count += 1

    if count == len(expected_balls):
      m += 1 


  return m/n
