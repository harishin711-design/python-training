votes = {
    "A": 0,
    "B": 0,
    "C": 0
}

n = int(input("Enter number of voters: "))

for i in range(n):
    candidate = input("Vote for candidate (A/B/C): ").upper()
    if candidate in votes:
        votes[candidate] += 1
    else:
        print("Invalid vote")

print("\nVote Results")
for candidate, count in votes.items():
    print(candidate, "=", count)

winner = max(votes, key=votes.get)
print("Winner is:", winner)