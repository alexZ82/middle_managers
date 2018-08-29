import random
import networkx as nx
from agent import Agent

class Environment:
  def __init__(self):
    self.dynamism = random.random()

class Issue:
  def __init__(self,id):
    self.id = id
    self.degree_of_urgency = random.random()
    self.type = random.randint(0, 1)      	  #0: Threat, 1: Opportunity
    self.relevant_department = random.randint(1,5)#5 departments
    self.resolved = False

  def __str__(self):
    return "id:"+ str(self.id) + ",degree_of_urgency:"+ str(self.degree_of_urgency)

class Firm:
  def __init__(self,num_agents,num_dep,resposiviness,interfunctional):
    self.num_agents = num_agents
    self.num_dep = num_dep
    self.agents = [Agent() for i in range(self.num_agents)]
    self.issues = {}
    self.connectivity = self.generate_department_connectivity(num_dep,interfunctional)[1]

  def generate_department_connectivity(self,num_dep,interfunctional):
    N,P = num_dep, interfunctional
    G = nx.generators.random_graphs.gnp_random_graph(N, P)
    #nx.draw(G)
    #plt.show()
    
    return G, G.edges()

  def add_issue(self,new_issue):
    self.issues[new_issue]=False

  def resolved_issues(self):
    return sum(self.issues.values())/len(self.issues)
