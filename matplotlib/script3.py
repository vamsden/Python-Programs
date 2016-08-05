import matplotlib.pyplot as plt

fig = plt.figure()

rect = fig.patch

# Colors the outer background
rect.set_facecolor("green")

x = [1, 3, 7, 9]
y = [23, 16, -10, 17]

# (1,1) 1 graph in height and 1 graph in width resp.
# (1,1,1) the last number specifies the graph number we are talking about.
graph1 = fig.add_subplot(1,1,1, axisbg='black')

# Function to plot the graph with x and y values and the color specifies the line color
# linewidth describes the thickness of the line
graph1.plot(x, y, "red", linewidth=4.0)

plt.show()