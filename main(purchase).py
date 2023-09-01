
from shoes import Shoes

low: Shoes = Shoes("Redleys", 250)
medium: Shoes = Shoes("Air force 1s", 600)
high: Shoes = Shoes("Jordan 1s", 2000)

try:
    shoe_budget = float(input("Please, enter your budget: "))
except ValueError:
    print("Invalid budget type")
    exit(1)

for shoes in [high, medium, low]:
    shoes.buy(shoe_budget)




# Calling the buying method on each shoe object
# OBS: The order of the shoes in the list is from the most expensive to the least expensive. The most expensive shoe
# have to be the first to be checked, because if the budget is less than the price of the most expensive shoe,
# then the budget is not enough to buy any of the shoes.


