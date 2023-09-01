class Shoes:
    
    def __init__(self, name: object, price) -> None:
        # both public attributes
        self.name = name # name of the shoe 
        self.price = float(price) # price of the shoe

    def budget_check(self, budget):
        # isinstance() is a built-in function that returns True if the specified object is of the specified type, otherwise False.
        if not isinstance(budget, (int, float)): # Checking if the budget is an int or float
            print("Invalid budget type")
            exit(1)

    def remaining_budget(self, budget):
        # This method returns the remaining budget after buying the shoe
        return budget - self.price
    
    def buy(self, budget):

        self.budget_check(budget) # Checking if the budget is an int or float

        if budget >= self.price:
            print(f"You can afford some {self.name}.")
            
            if budget == self.price:
                print("Your budget is exactly this price of the shoe. You can buy it!")
            else:
                print(f"You can buy this {self.name} with your budget of R${budget:.2f}")
                print(f"Your will be remaining R${self.remaining_budget(budget):.2f}")
            print('Thank you for shopping with us!')
        else:
            print(f"You can't afford any {self.name}. Your budget is too low")



