basketball_team = {"Jack", "Jess", "Jane", "Jen", "Juliet", "Jap"}
baseball_team = {"Jack", "Jane", "Juliet", "Jacob", "Jax", "Justice"}

print("Students who play both sports:", basketball_team.intersection(baseball_team))
print("Students who play either sport:", basketball_team.union(baseball_team))
print("Students who play baseball but not basketball:", baseball_team.difference(basketball_team))
print("Students who play basketball but not baseball:", basketball_team.difference(baseball_team))
print("Students who play one sport but not both:", basketball_team.symmetric_difference(baseball_team))