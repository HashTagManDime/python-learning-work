# Day 1 - Variables, Functions, Strings

# variable = your shaker bottle
name = "Stephen"
sets = 4
reps = 10

# function = define an exercise
def summary(person, sets, reps):
    total = sets * reps
    pr_today = True
    return f"{person} completed {total} reps. PR today? {pr_today}"

# call the function (do the set)
print(summary(name, sets, reps))
