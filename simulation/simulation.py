from enviroment import Firm,Issue,Environment
from agent import Agent
import random

number_of_simulations = 10

for i in range(number_of_simulations):
  a = Firm(4,5,0.5,0.4)
  x = Issue(1,a.num_dep)
  #print(x)
  a.add_issue(x)
