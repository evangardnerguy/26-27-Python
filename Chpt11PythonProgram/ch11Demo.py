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