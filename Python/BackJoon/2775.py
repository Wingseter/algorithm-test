T = int(input())

for _ in range(T):
    people = [a for a in range(1, 15)]
    flore = int(input())
    room = int(input())
    for f in range(flore):
        for r in range(1, room):
            people[r] = people[r] + people[r -1]
    print(people[room - 1])
