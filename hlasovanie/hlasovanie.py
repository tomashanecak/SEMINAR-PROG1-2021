import os

from matplotlib.pyplot import get
path = os.path.dirname(__file__)

votes = []
out_of_game = []

with open(os.path.join(path, "hlasovanie_1.txt"), "r") as fvotes:
	for vote in fvotes:
		votes.append(vote.strip())

with open(os.path.join(path, "hlasovanie_2.txt"), "r") as fout:
	for out in fout:
		out_of_game.append(out.strip())

for i, vote in enumerate(votes):
    if vote in out_of_game:
        votes.pop(i)
        
votes_count = {}
for vote in votes:
	if vote in votes_count:
		votes_count[vote] += 1
	else:
		votes_count[vote] = 1


print(f"Celkovy pocet hlasov je -> {len(votes)}")
for vote in votes_count:
    print(f"Sutaziaci s cislom {vote} ma pocet hlasov -> {votes_count[vote]}")

key_min = min(votes_count.keys(), key=(lambda k: votes_count[k]))
minimal_value = votes_count[key_min]
not_passing = []
for person in votes_count:
    if votes_count[person] == minimal_value:
        not_passing.append(person)

for person in not_passing: print(f"Do dalsieho kola nepostupuje sutaziaci s cislom -> {person} s poctom hlasov {minimal_value}")



