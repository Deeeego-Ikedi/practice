#practice
qs = ["What is your name?",
      "What is your fav. color?",
      "What is your quest?"]

n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3


#section7-1
mv_title = ["ウォーキング・デッド",
           "アントラージュ",
           "ザ・ソプラノズ",
           "ヴァンパイア・ダイアリーズ"]

for mvtit in mv_title:
    print(mvtit)


#section7-2
for i in range(25, 61):
    print(i)


section7-3
mv_title = ["ウォーキング・デッド",
            "アントラージュ",
            "ザ・ソプラノズ",
            "ヴァンパイア・ダイアリーズ"]

x = 1

while x < len(mv_title) + 1:
    print(x, ":", mv_title[x-1])
    x += 1


#section7-4
number = 17
while True:
    a = input("Guess a number or type q to quit.")
    if a == "q":
        break
    try:
        a = int(a)
    except ValueError:
        print("please type a number or q to quit.")
    if a == number:
        print("You guessed correctly!")
        break
    else:
        print("You guessed incorrectly!")


#section7-5
a = [8, 19, 148, 4]
b = [9, 1, 33, 83]
c = []

for i in a:
    for j in b:
        c.append(i * j)

print(c)

        





