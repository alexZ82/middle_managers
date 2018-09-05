import random
import networkx as nx
from agent import Agent

class Environment:
  def __init__(self):
    self.dynamism = random.random()

class Issue:
  def __init__(self,id,rel):
    self.id =str(id)
    self.degree_of_urgency = random.random()
    self.type = random.randint(0, 1)              #0: Threat, 1: Opportunity
    self.relevant_department = random.randint(0,rel-1)#5 departments
    self.impact_on_agents = random.random()
    self.resolved = False
    self.promoted = False
  def __str__(self):
    return "id:"+ str(self.id) + ",degree_of_urgency:"+ str(self.degree_of_urgency)

class Firm:
  def __init__(self,num_agents,num_dep,resposiviness,interfunctional):
    self.num_agents = num_agents
    self.num_dep = num_dep
    self.agents = [Agent(num_dep,i) for i in range(self.num_agents)]
    self.issues = {}
    #tmp = self.generate_department_connectivity(num_dep,interfunctional)
    #self.connectivity = tmp[1]
    firm_c = self.generate_department_connectivity(num_dep,interfunctional)

  def generate_department_connectivity(self,num_dep,interfunctional):
    N,P = num_dep, interfunctional
    G = nx.generators.random_graphs.gnp_random_graph(N, P)
    #nx.draw(G)
    #plt.show()
    return G#, G.edges()

  def add_issue(self,new_issue):
    self.issues[new_issue]=False
    dep = new_issue.relevant_department
    for a in self.agents:
        a.add_issue(new_issue,self.firm_c.neighbors(dep))


  def resolved_issues(self):
    return sum(self.issues.values())/len(self.issues)
