import matplotlib.pyplot as plt

fig = plt.figure()

rect = fig.patch
rect.set_facecolor("green")

x = [1, 3, 7, 9]
y = [23, 16, -10, 17]

# (1,1) 1 graph in height and 1 graph in width resp.
graph1 = fig.add_subplot(1,1,1, axisbg='black')
graph1.plot(x, y, "red", linewidth=4.0)

plt.show()