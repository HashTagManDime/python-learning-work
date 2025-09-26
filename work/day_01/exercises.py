# A small roster of lifters: (name, weight_lbs, grams_per_lb)
clients = [
    ("Tiny", 150, 1.2),
    ("Big Jacked Rabbit", 250, 1.3),
    ("You", 241, 1.25),
    ("Jack Ass", 400, 2.0)
]

def protein_goal(weight, grams_per_lb):
    raw = weight * grams_per_lb
    total_protein = min(raw, 350)
    return total_protein

for name, weight, gpl in clients:
    goal = protein_goal(weight, gpl)
    print(f"{name}: At {weight} lbs, your protein goal is {goal:.1f} grams")