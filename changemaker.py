import datetime

class node:
    def __init__(self,amount,parent,node_type):
        self.amount = amount
        self.parent = parent
        self.node_type = node_type

    def make_child(self, node_type):
        if (node_type == 'Q' and self.amount >= 25):
            return node(self.amount-25,self, node_type)
        elif (node_type == 'D' and self.amount >= 10):
            return node(self.amount-10,self, node_type)
        elif (node_type == 'N' and self.amount >= 5):
            return node(self.amount-5,self, node_type)
        elif (node_type == 'P' and self.amount >=1):
            return node(self.amount-1,self, node_type)
        else:
            return False

    def make_children(self): # runs in O(2^n) time (BAD)
        if (self.amount == 0):
            leaves.append(self)
            results_set.add(tuple(self.gather_change()))
            return True
        for t in {'Q', 'D', 'N', 'P'}:
            temp_result = self.make_child(t)
            if temp_result != False:
                temp_result.make_children()
        return

    def gather_change(self):
        coin_purse = [0,0,0,0] # quarters, nickles, dimes, and pennies
        temp_node = self;
        while(temp_node.parent != None):
            if (temp_node.node_type == 'Q'):
                coin_purse[0] +=1
            elif (temp_node.node_type == 'D'):
                coin_purse[1] +=1
            elif (temp_node.node_type == 'N'):
                coin_purse[2] +=1
            elif (temp_node.node_type == 'P'):
                coin_purse[3] +=1
            else:
                raise ValueError('A very bad thing happened')
            temp_node = temp_node.parent
        return coin_purse

    def brute_force(self): # runs in O(n^^4) (MODERATELY BAD)
        for quarters in range(0, self.amount//25+1):
            for dimes in range(0,self.amount//10+1):
                for nickels in range(0,self.amount//5+1):
                    for pennies in range(0,self.amount+1):
                        if (self.amount == quarters*25 + dimes*10 + nickels*5 +pennies):
                            results_set.add(tuple([quarters,dimes,nickels,pennies]))
        return

    def make_change_memoized(self,amount): #returns a set of all solutions for making change of the amount
        # runs in O(nlog(n) time (REALLY GOOD)
        if amount in previous_solutions_dict.keys():
            return previous_solutions_dict[amount]
        elif (amount == 0):
            previous_solutions_dict[amount] = [(0,0,0,0)]
            return [(0,0,0,0)]
        else: # we do not have a result yet for this amount
            temp_solution = set()
            minus_quarter_results = set()
            minus_dime_results = set()
            minus_nickel_results = set()
            minus_penny_results = set()
            if amount-25 >= 0:
                minus_quarter_results = self.make_change_memoized(amount-25)
                minus_quarter_results = self.add_quarter(minus_quarter_results)
            if amount-10 >= 0:
                minus_dime_results = self.make_change_memoized(amount-10)
                minus_dime_results = self.add_dime(minus_dime_results)
            if amount-5 >= 0:
                minus_nickel_results = self.make_change_memoized(amount-5)
                minus_nickel_results = self.add_nickel(minus_nickel_results)
            if amount-1 >= 0:
                minus_penny_results = self.make_change_memoized(amount-1)
                minus_penny_results = self.add_penny(minus_penny_results)
            temp_solution = temp_solution.union(minus_quarter_results)
            temp_solution = temp_solution.union(minus_dime_results)
            temp_solution = temp_solution.union(minus_nickel_results)
            temp_solution = temp_solution.union(minus_penny_results)
            previous_solutions_dict[amount] = temp_solution
            return temp_solution

    def add_quarter(self, solution_set): #adds a quarter to each solution in the set
        temp_solution_set = set()
        for temp_solution in solution_set:
            temp_list = list(temp_solution)
            temp_list[0] +=1
            temp_solution_set.add(tuple(temp_list))
        return temp_solution_set
        
    def add_dime(self, solution_set): #adds a dime to each solution in the set
        temp_solution_set = set()
        for temp_solution in solution_set:
            temp_list = list(temp_solution)
            temp_list[1] +=1
            temp_solution_set.add(tuple(temp_list))
        return temp_solution_set

    def add_nickel(self, solution_set): #adds a nickel to each solution in the set
        temp_solution_set = set()
        for temp_solution in solution_set:
            temp_list = list(temp_solution)
            temp_list[2] +=1
            temp_solution_set.add(tuple(temp_list))
        return temp_solution_set

    def add_penny(self, solution_set): #adds a penny to each solution in the set
        temp_solution_set = set()
        for temp_solution in solution_set:
            temp_list = list(temp_solution)
            temp_list[3] +=1
            temp_solution_set.add(tuple(temp_list))
        return temp_solution_set

leaves = []
results_set = set()

print('Recursive tree approach')
datetime_object = datetime.datetime.now()
print(datetime_object)

start_node = node(40,None,None)
# recurrsive tree approach to solving the problem
print(start_node.amount)
start_node.make_children()
print(len(leaves))
#temp_list = list(results_set)
#temp_list.sort()
#print(temp_list)

leaves = []
results_set = set()

print('Brute-force method')
datetime_object = datetime.datetime.now()
print(datetime_object)

start_node = node(400,None,None)
#brute force approach to solving the problem
print(start_node.amount)
start_node.brute_force()
#temp_list = list(results_set)
#temp_list.sort()
#print(temp_list)

leaves = []
results_set = set()
previous_solutions_dict = {}

print('Memoized method')
datetime_object = datetime.datetime.now()
print(datetime_object)

start_node = node(400,None,None)
print(start_node.amount)
temp_set = start_node.make_change_memoized(start_node.amount)
#temp_list = list(temp_set)
#temp_list.sort()
#print(temp_list)

datetime_object = datetime.datetime.now()
print(datetime_object)