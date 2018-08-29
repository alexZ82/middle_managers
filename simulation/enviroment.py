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
  def __init__(self,num_agents,num_dep,resposiviness,interfunctional):
    self.num_agents = num_agents
    self.num_dep = num_dep
    agents = [Agent() for i in range(self.num_agents)]
    issues = [] 

  def generate_department_connectivity(num_dep,interfunctional):
    N,P = num_dep, interfunctional
    G = nx.generators.random_graphs.gnp_random_graph(N, P)
    return G, G.edges()
    #nx.draw(G)
    #plt.show()
