import csv
import itertools
import time

# To obtain the maximum number of possible combinations
# you have to do the following calculation 2**n
# (n being the number of actions)
# Which will give us 2**20 or 1,048,575
# While using this script we consume approximatly 30Mo of memory


def search_csv():
    stocks = []
    with open("Action.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            stock = (
                row[0],
                float(row[1]),
                float(row[2]),
                float(row[1]) * float(row[2]) / 100,
            )
            stocks.append(stock)
    return stocks


def create_combination():
    possible_combinations = []
    best_action = None
    best_roi = 0
    for actions_number in range(1, len(stocks) + 1):
        for combination in itertools.combinations(stocks, actions_number):
            possible_combinations.append(combination)
    for combination in possible_combinations:
        budget = sum(action[1] for action in combination)
        roi = sum(action[3] for action in combination)
        if budget < 500 and roi > best_roi:
            best_action = combination
            best_roi = roi
    result = print(
        f"\nFYI : Each action contain : name, coast, benefits (in %) and calculated roi \n"
    )
    print(f"Here is the best buying option to maximize your profit : {best_action}\n")
    print(f"This combination will bring you a profit of : {best_roi}€\n\n")
    return result


start = time.time()
stocks = search_csv()
create_combination()
# time.sleep(20)
end = time.time()
print("This script took :", (end - start) * 10**3, "ms to give you this result.")
