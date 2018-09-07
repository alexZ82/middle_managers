import random
import numpy as np
class Agent:

  def __init__(self,num_dep,id,firm):
    self.id = id#str(id)
    self.years_in_company = np.random.normal(loc=5,scale=4.67)#sample from normal distribution mean = 5, sd = 4.67
    self.previous_experience = random.randint(1,5)#https://www.ft.com/content/ded1823a-370e-11e7-99bd-13beb0903fa3
    self.belongigness = random.random()        #THINK
    self.intuition =0.182*firm.empowerment+0.189*firm.env_dynamism+0.185*firm.resources+0.159*firm.control-0.367*self.years_in_company+0.163*firm.years_in_operation #random.random()
    self.issues = []
    self.department = random.randint(0,num_dep-1)
  def add_issue(self,issue,rel_deps):
    if issue.relevant_department == self.department or self.department in rel_deps:
        self.issues.append(issue)
        print("adding issue: {} to agent: {}".format(issue.id,self.id))
  def __str__(self):
      return ("years_in_company:"+ str(self.years_in_company) + 
              "\n ,previous_experience:"+ str(self.previous_experience)+
              "\n ,department:"+ str(self.department)+
              "\n ,belongignes9"+ str(self.belongigness)+
              "\n ,previous_experience:"+ str(self.previous_experience)+
              "\n ,issues:"+ str(self.issues))
 # def promote(self,issue):
 #   tmp = 0.41*intuition + 0.33*issue.impact_on_agents + 0.11*issue.degree_of_urgency
 #   print("will promote: {}".format(tmp))
 #   if tmp > 0.5
 #     issue.promote = True

  def stats(self):
    issues_st = {"num_issues":len(self.issues),"promoted":sum([1 for i in self.issues if i.promoted]),"resolved":sum([1 for i in self.issues if i.resolved])} 
    stats = dict(self.__dict__, **issues_st)
    return stats
