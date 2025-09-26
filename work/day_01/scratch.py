#function = protein goals
def protein_goal(weight, grams_per_lb):
    return f"At {weight} lbs, your protein goal is {grams_per_lb}"

#variables
#Tiny little fella =
weight = 150
grams_per_lb = 1.2 # to maximize hypertrophy
#call = How much do we need coach?
print(protein_goal(weight, weight * grams_per_lb))

#Big Jacked Rabbit =
weight = 250
grams_per_lb = 1.3 # cause John Jewett said so
#call = How much do we need coach?
print(protein_goal(weight, weight * grams_per_lb))


