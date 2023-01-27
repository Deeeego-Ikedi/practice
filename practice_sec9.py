###section9-1
##import os
##
##path = os.path.join("C:", "\\Users", "Daigo", "Documents", "Python Scripts", "practice_sec9.txt")
##ans = input("Where are you from?")
##
##with open(path, "w") as f:
##    f.write("Hi from Python!\n")
##    f.write("Hi from Hamamatsu!\n")
##
##
###section9-2
##    f.write(ans)
##    f.write("\n")
##
##
###section9-3
##list_1 = ["Top Gun", "Risky Business", "Monority Report"]
##list_2 = ["Titanic", "The Revenant", "Inception"]
##list_3 = ["Training Day", "Man on Fire", "Flight"]
##
##list_data = [list_1, list_2, list_3]
##
##import csv
##
##with open("sec9-3.csv", "w", newline="") as f:
##    w = csv.writer(f, delimiter=",")
##    w.writerow(list_1)
##    w.writerow(list_2)
##    w.writerow(list_3)
##
##
#section9-4
list_1 = ["トップガン", "リスキービジネス", "マイノリティレポート"]
list_2 = ["タイタニック", "ザ・レベナント", "インセプション"]
list_3 = ["トレーニング・デイ", "マン・オン・ファイア", "フライト"]

list_data = [list_1, list_2, list_3]

import csv

with open("sec9-4.csv", "w", newline="", encoding="cp932") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(list_1)
    w.writerow(list_2)
    w.writerow(list_3)



