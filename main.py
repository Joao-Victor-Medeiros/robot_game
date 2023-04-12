from random import random
from classes.Reward import Reward
from classes.Robot import Robot

r1 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')
r2 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')
r3 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')
r4 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')
r5 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')
r6 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')
r7 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')

rewards = [r1, r2, r3, r4, r5, r6, r7]
print(r1) 
rewards

robot = Robot(random.randint(0, 10), random.randint(0, 10))
print(robot.x, robot.y)


def check_reward(robot, rewards):
  ok = False
  for reward in rewards:
    if robot.x == reward.x and robot.y == reward.y:
      print("recompensa ganha %s" % reward.name)
      ok = True
    
  return ok;

for i in range(10):
  moviment = input('Digite up, down, left, right para o movimento')
  if(moviment == 'up'):
    robot.move_up()
  elif(moviment == 'down'):
    robot.move_down()
  elif(moviment == 'left'):
      robot.move_left
  elif(moviment == 'right'):
    robot.move_right()
  else:
    print("movimento inválido")
    continue
  print(robot)

  
check_reward(robot, rewards)
