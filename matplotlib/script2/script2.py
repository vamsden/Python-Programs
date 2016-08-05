import matplotlib.pyplot as plt

x = []
y = []

read_file = open("data.txt", "r")
data = read_file.read().split("\n")

for i in data:
	val = i.split(",")
	x.append([val[0]])
	y.append([val[1]])

print(data)
print(x)
print(y)

plt.plot(x, y)
plt.show()
