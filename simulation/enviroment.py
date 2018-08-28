import random
import agent

class Environment:
  def __init__(self):
    self.dynamism = random.random()

class Issue:
  def __init__(self):
    self.degree_of_urgency = random.random()
    self.type = random.randint(0, 1)      	  #0: Threat, 1: Opportunity
    self.relevant_department = random.randint(1,5)#5 departments

class Firm:
  def __init__(self,num,resposiviness,interfunctional):
    agents = [Agent() for i in range(num)]
    issues = [] 


