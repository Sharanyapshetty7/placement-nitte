n = int(input("Enter number of teams: "))
teams = [input(f"Enter team {i+1}: ") for i in range(n)]
meet = int(input("Enter number of meetings: "))
match = [[teams[i], teams[j]] for i in range(n-1) for j in range(i+1, n) for _ in range(meet)]
for m in match:
    print(f"{m[0]} vs {m[1]}")
