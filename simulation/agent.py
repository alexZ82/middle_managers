import random
class Agent:

  def __init__(self,num_dep,id):
    self.id = str(id)
    self.years_in_company = random.randint(1,5)#https://www.ft.com/content/ded1823a-370e-11e7-99bd-13beb0903fa3
    self.previous_experience = random.randint(1,8)
    self.belongigness = random.random()        #THINK
    self.issues = []
    self.department = random.randint(0,num_dep-1)
  def add_issue(self,issue,rel_deps):
    if issue.relevant_department == self.department or self.department in rel_deps:
        self.issues.append(issue)
        print("adding issue: {} to agent: {}".format(issue.id,self.id))
  def _str__(self):
      return ("years_in_company:"+ str(self.years_in_company) + 
              "\n ,previous_experience:"+ str(self.previous_experience)+
              "\n ,department:"+ str(self.department)+
              "\n ,belongignes9"+ str(self.belongigness)+
              "\n ,previous_experience:"+ str(self.previous_experience)+
              "\n ,issues:"+ str(self.issues))
  def stats(self):
    issues_st = {"num_issues":len(self.issues),"promoted":sum([1 for i in self.issues if i.promoted]),"resolved":sum([1 for i in self.issues if i.resolved])} 
    stats = dict(self.__dict__, **issues_st)
    return stats
