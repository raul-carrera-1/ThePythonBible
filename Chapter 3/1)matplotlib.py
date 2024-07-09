## Matplot is a imprt that allows you to plot things in a 2D graph

# Import matplotlib.pyplot as plot
import matplotlib.pyplot as plot

print("Running")

# Value of the x cord
x = [-30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
# Value of the y cord is absolute value of x
y = []
for nums in range(len(x)):
    y.append(abs(x[nums]))

# Plot the x and y in the graph, calls this equation as "By 5", and colors the equations as "darkgreen"
plot.plot(x,y,label="By 5",color="darkgreen")
# Plot the x sides name as "x"
plot.xlabel('x')
# Plot the y sides name as "y"
plot.ylabel('y')
# The title of the 2D graph
plot.title('multiples in the Positive direction')
# Show the grid
plot.grid(True)
# To Show the graph
plot.legend()
plot.show()