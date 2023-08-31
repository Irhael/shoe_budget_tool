class Shoes:
    
    def __init__(self, name, price) -> None:
        # both public attributes
        self.name = name # name of the shoe 
        self.price = float(price) # price of the shoe
    
    def budget_check(self, budget):
        #isinstance() is a built-in function that returns True if the specified object is of the specified type, otherwise False.
        if not isinstance(budget, (int, float)): # Checking if the budget is an int or float
            print("Invalid budget type") 
            exit(1)

    def remaining_budget(self, budget):
        # This method returns the remaining budget after buying the shoe
        return budget - self.price 
    
    def buying(self, budget):

        self.budget_check(budget) # Checking if the budget is an int or float

        if budget >= self.price: 
            print(f"You cant buy this {self.name} with your budget of {budget}")
            
        if budget == self.price:
            print("Your budget is exactly the price of the shoe. If you buy this shoe, you will have no money left.")
        
        else:
            print(f"You can buy this {self.name} with your budget of {budget}")
            print(f"Your remaining budget is {self.remaining_budget(budget)}")

        exit('Thank you for shopping with us!')