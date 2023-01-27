#print("Hello, World!")
#print("Hello, Japan!")
 
#for i in range(100):
#   print("Hello, World!")

# section3-1
print("Japan")
print("Shizuoka")
print("Hamamatsu")

# section3-2
x = 15
if x < 10:
    print("xは10未満です。")
else:
    print("xは10以上です。")

# section3-3
x = 30
if x <= 10:
    print("x is smaller than 10 or 10.")
elif x > 10 and x <= 25:
    print("x is larger than 10 and smaller than 25 or 25.")
else:
    print("x is larger than 25.")

# section3-4
x = 10
y = 3
z = x % y
print(z)
    
# section3-5
x = 10
y = 2
z = x / y
print(z)

# section3-6
age = 10
if age <= 1:
    print("You're baby.")
elif age > 1 and age <= 3:
    print("You're toddler.")
elif age > 3 and age <= 5:
    print("You're preschool.")
elif age > 5 and age <= 12:
    print("You're gradeschooler.")
elif age > 12 and age <= 18:
    print("You're teen.")
elif age > 18 and age <= 21:
    print("You're young adult.")
elif age > 21 and age < 65:
    print("You're adult.")
elif age >= 65 and age < 75:
    print("You're early elderly.")
else:
    print("You're late elderly.")


