print("Calculating triplets.....")

def pythagorean():
    for a in range(1, 50):
        for b in range(a + 1, 50):
            for c in range(b + 1, 50):
                if (a ** 2) + (b ** 2) == (c ** 2):
                    yield (a, b, c)

triplets = pythagorean() # creates a generator
for x in triplets:
	print(x)
