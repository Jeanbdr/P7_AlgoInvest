import csv
import itertools
import time

# To obtain the maximum number of possible combinations
# you have to do the following calculation 2**n
# (n being the number of actions)
# Which will give us 2**20 or 1,048,575


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


def create_combination(budget):
    possible_combinations = []
    for actions_number in range(1, len(stocks) + 1):
        for combination in itertools.combinations(stocks, actions_number):
            combination_costs = [action[1] for action in combination]
            if sum(combination_costs) <= budget:
                possible_combinations.append(combination)
    return possible_combinations


def find_best_option():
    combinations_benefits = []
    final_result = []
    for combination in possible_combinations:
        benefits = sum(action[3] for action in combination)
        combinations_benefits.append(benefits)
    for total_roi, action_package in zip(combinations_benefits, possible_combinations):
        final_result.append((total_roi, action_package))
    final_result.sort(reverse=True)
    print(
        f"\nFYI : Each action contain : name, coast, benefits (in %) and calculated roi \n"
    )
    print(
        f"Here is the best buying option to maximize your profit : {final_result[0][1]}\n"
    )
    print(f"This combination will bring you a profit of : {final_result[0][0]}€\n\n")


start = time.time()
stocks = search_csv()
possible_combinations = create_combination(budget=500)
find_best_option()
end = time.time()
print("This script took :", (end - start) * 10**3, "ms to give you this result.")
