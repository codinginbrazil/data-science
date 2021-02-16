import matplotlib.pyplot as plt

''' Source
    https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
'''

PATH = 'view/graph/'
GRAPH = 'bar'

x0 = [1, 3, 5, 7, 9]
y0 = [2, 3, 7, 1, 0]

x1 = [2, 4, 6, 8, 9]
y1 = [5, 1, 3, 7, 4]

plt.bar(x0, y0, label = "red", color="r")
plt.bar(x1, y1, label = "blue", color="b")

plt.title('Example: '+GRAPH+' graph')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()

plt.savefig(PATH+GRAPH+'.pdf', dpi=300)
