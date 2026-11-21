# variables, arithmetic, importing modules
# demo 1 variable & assignment

def demo1_variables():
    CAN_VOLUME = 0.355
    BOTTLE_VOLUME = 2.0

    cansPerPack = 6
    packVolume = cansPerPack * CAN_VOLUME
    print("6-pack volume:", packVolume, "liters")
    print("2-liter bottle:", BOTTLE_VOLUME, "liters")

demo1_variables()

# = means is set to or gets
lives = 3
print("Lives at start:", lives)
lives = lives + 2
print("After a power-up:", lives)

print("\n\noperators and precidence:")
def demo3_operators():
    a = 10
    b = 4
    print("a + b / 2 =", a + b / 2) #12.0
    print("(a + b) / 2 =", (a + b) / 2) #7.0
    print("10 - 2 - 3 =", 10 - 2 - 3) #5
    print("7 + 4.0 =", 7 + 4.0) #11.0

    print("10 * 2 ** 3 =", 10 * 2 ** 3) #80
    print ("2 ** 3 ** 2 =", 2 ** 3 ** 2) #512

    balance = 1000.0
    rate = 5.0
    years = 10
    future = balance * (1 + rate / 100) ** 10
    print("future value: ", future)

demo3_operators()

print("\n\nFloor division & modulus")
def demo4_floor_and_mod():
    print("17 / 5 =", 17 / 5)
    print("17 // 5 =", 17 // 5)
    print("17 % 5 =", 17 % 5)

demo4_floor_and_mod()

screentime = 437
hours = screentime // 60
minutes = screentime % 60
print(hours, "hours and", minutes, "minutes")


from math import sqrt, pi

radius = sqrt(60)
print(round(pi * radius ** 2, 2))