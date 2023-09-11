def makejuice(fruit):
    return f"{fruit}+🧃"
def add_ice(juice):
    return f"{juice}+🧊"
def add_sugar(iced_juice):
    return f"{iced_juice}+🍬"


juice =makejuice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)