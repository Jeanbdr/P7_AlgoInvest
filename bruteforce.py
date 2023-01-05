"""LA Y'AURA DES TRUCS POUR BRUTALISER DE FORCE 
à base de for in range  addition tout ca si ca depasse 500 ca compte pas
on append le tout dans une liste on tri et hop magie la force est brutaliser"""

import csv
import itertools
import time

# MAXIMUM COST POSSIBLE : 822
# MAXIMUM COMBINATION POSSIBLE : 1.048.575


def search_csv():
    stocks = []
    with open("Action.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            stock = (
                row[0],
                float(row[1]),
                float(row[2]),
                float(row[1]) * float(row[2]),
            )
            stocks.append(stock)
    return stocks


stocks = search_csv()


def create_combination(budget):
    start = time.time()
    possible_combinations = []
    for actions_number in range(1, len(stocks) + 1):
        for combination in itertools.combinations(stocks, actions_number):
            combination_costs = [action[1] for action in combination]
            if sum(combination_costs) <= budget:
                possible_combinations.append(combination)
    end = time.time()
    print("Execution time :", (end - start) * 10**3, "ms")
    return possible_combinations


possible_combinations = create_combination(budget=500)
print(len(possible_combinations))


def find_best_option():
    for combination in possible_combinations:
        benefits = sum(action[3] for action in combination)


find_best_option()
