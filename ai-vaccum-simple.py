import random

mantra = {(0,0):'right',(0,1):'suck',(1,0):'left',(1,1):'suck'}
world, loc = [0, 0], 0

for i in range(10):
  if random.random()<0.2: world[0]=1
  if random.random()<0.2: world[1]=1
  print('iter', i+1, ': A is', 'clean' if world[0]==0 else 'dirty', ', B is', 'clean' if world[1]==0 else 'dirty')
  action = mantra[(loc, world[loc])]
  print('Agent is in room', 'A' if loc==0 else 'B', end=', ')
  if action=='right':
    print('moving to room B')
    loc = 1
  elif action=='left':
    print('moving to room A')
    loc = 0
  else:
    print('cleaning')
    world[loc]=0