import matplotlib.pyplot as plt


PATH = 'view/graph/'
GRAPH = 'scatterplot'

x0 = [1, 3, 5, 7, 9]
y0 = [2, 3, 7, 1, 0]

x1 = [2, 4, 6, 8, 9]
y1 = [5, 1, 3, 7, 4]

# plt.plot(x0, y0, label = "red", color="#000000", linestyle=":", linewidth=5)
plt.scatter(x0, y0, label = "red", color="r", marker="*",s=x0)
plt.scatter(x1, y1, label = "blue", color="b", marker=".")

plt.title('Example: '+GRAPH+' graph')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()

plt.savefig(PATH+GRAPH+'.pdf', dpi=300)
