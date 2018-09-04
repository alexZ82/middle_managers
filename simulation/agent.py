import random
class Agent:

  def __init__(self,num_dep):
    self.years_in_company = random.randint(1,5)#https://www.ft.com/content/ded1823a-370e-11e7-99bd-13beb0903fa3
    self.previous_experience = random.randint(1,8)
    self.belongigness = random.random()        #THINK
    self.issues = []
    self.department = random.randint(0,num_dep-1)
  def add_issue(self,issue,rel_deps):
    print('agent depart ',self.department)
    print('issue depart ',issue.relevant_department)
    print('rel departs',rel_deps)
    print('in?',self.department in rel_deps)
    if issue.relevant_department == self.department or self.department in rel_deps:
        self.issues.append(issue)
