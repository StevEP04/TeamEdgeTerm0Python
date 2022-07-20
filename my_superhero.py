
import random
print("\n\t-My super hero_\n")

class My_superhero:
    def __init__(self, name, hit_superpower, defense, health, attacks, hero_alive):
        self.name = name
        self.hit_superpower = hit_superpower
        self.defense = defense
        self.health = health
        self.attacks = attacks
        self.alive = True

    def __repr__(self):
        return f"Superhero: {self.name}"
    
    def is_alive(self):
        return self.health > 0 

    def attack(self, villian):
        style_attack = input(f"Which attack will you use? {self.attacks}")
        villian.health = villian.health - self.attacks[style_attack]
        print(f"{self.name} attacks {villian.name}!\n{villian.name} health = {villian.health}")



thor = My_superhero("Thor", 150, 200, 1000, {"god blast": 210, "hammer": 110, "The odinforce": 180, "ultimate" : 400}, True)
thanos = My_superhero("Thanos", 150, 200, 1000, {"power gem": 250, "reality gem": 150, "space gem": 120, "ultimate": 400}, True)

while thor.is_alive and thanos.is_alive:
    thor.attack(thanos)
    thanos.attack(thor)

if thor.is_alive():
    print("The God of thunder wins! ...")
else:
    print("Thanos destroyed the god of thunder! ...")
