import random


def flipping_simulation(how_many):

    heads_count = 0
    tails_count = 0

    for i in range(how_many):

        flip = random.randint(0, 1)

        if flip == 0:
            heads_count += 1
        else:
            tails_count += 1

    return heads_count, tails_count


how_many = int(input("How many times should I flip a coin?: "))

head = 0
tail = 1

result = flipping_simulation(how_many)

heads_count = result[0]
tails_count = result[1]

print(f"Head of coin appears {heads_count} times.")
print(f"Tail of coin appears {tails_count} times.")

if heads_count > tails_count:
    print(f"The Heads appears {round(heads_count / tails_count, 2)} times more often than the Tails.")

else:
    print(f"The Tails appears {round(tails_count / heads_count, 2)} times more often than the Heads.")
