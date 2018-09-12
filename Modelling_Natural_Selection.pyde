from random import shuffle, sample
def setup():
  global red_pop
  global blue_pop
  global black_pop
  global total_pop
  global organism_list
  global y
  global blue_history
  global red_history
  global black_history
  fullScreen()
  frameRate(2)
  background(255)
  red_pop = 3
  blue_pop = 3
  black_pop = 3
  y = 70
  organism_list = []
  blue_history = []
  red_history = []
  black_history = []
  total_pop = 0

def mouseClicked():
    global blue_history
    global black_history
    global red_history
    print(black_history)
    print(blue_history)
    print(red_history)

def draw():
  global red_pop
  global blue_pop
  global black_pop
  global total_pop
  global organism_list
  global y
  global blue_history
  global red_history
  global black_history
  
  #Records the current population levels as history.
  blue_history.append(blue_pop)
  red_history.append(red_pop)
  black_history.append(black_pop)
  
  organism_list = []
  #Builds list of organisms based on current population values.
  for organism in range(red_pop):
      organism_list.append("red")
  for organism in range(blue_pop):
      organism_list.append("blue")
  for organism in range(black_pop):
      organism_list.append("black")
  #Calculates the overall population
  total_pop = red_pop + blue_pop + black_pop
  
  infected = int(round(total_pop*0.2))
  
  blue_removed = 0
  red_removed = 0
  
  shuffle(organism_list)
  organisms_sampled = sample(range(total_pop), infected)
  for value in organisms_sampled:
      if organism_list[value] == "blue":#Marks how many blue organisms to remove.
          blue_removed += 1
  
  organisms_sampled = sample(range(total_pop), infected)
  for value in organisms_sampled:
      if organism_list[value] == "red":#Marks how many red organisms to remove.
          red_removed += 1

  for i in range(red_removed):#Removes appropriate number of red organisms.
      organism_list.remove("red")
      red_pop -= 1

  for i in range(blue_removed):#Removes appropriate number of blue organisms.
      organism_list.remove("blue")
      blue_pop -= 1
  
  blue_pop = int(round(blue_pop*1.5))#Multiplies the current populations as if by reproducing.
  red_pop = int(round(red_pop*1.5))
  black_pop = int(round(black_pop*1.5))
  
  
  organism_list.sort()#Sorts the list of organisms in preparation to display them.
  x = 70
  for organism in organism_list:#Draws the organisms as coloured circles in a line across the display.
    if organism == "red":
      fill(255,0,0)
      stroke(255,0,0)
    if organism == "blue":
      fill(0,0,255)
      stroke(0,0,255)
    elif organism == "black":
      fill(0)
      stroke(0)
    ellipse(x, y, 6, 6)
    x += 10
  y += 50
    
