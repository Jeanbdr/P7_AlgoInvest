"""LA Y'AURA DES TRUCS POUR BRUTALISER DE FORCE 
à base de for in range  addition tout ca si ca depasse 500 ca compte pas
on append le tout dans une liste on tri et hop magie la force est brutaliser"""

import csv
import itertools
import time

# PRIX DE L'ACTION - (PRIX DE L'ACTION * ROI)
# MAXIMUM COST POSSIBLE : 822
# MAXIMUM COMBINATION POSSIBLE : 1.048.575
stocks = []
possible_combination = []
alors_peut_etre = []


def search_csv():
    with open("Action.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            stock = [row[0], float(row[1]), float(row[2])]
            stocks.append(stock)


search_csv()


def create_combination():
    target = 500
    start = time.time()
    for i in range(len(stocks), 0, -1):
        for j in itertools.combinations([x[1] for x in stocks], i):
            if sum(j) <= target:
                possible_combination.append(j)
    end = time.time()
    print("Execution time :", (end - start) * 10**3, "ms")


create_combination()
# print(stocks[1][1:3])
print(stocks)
print(possible_combination)
