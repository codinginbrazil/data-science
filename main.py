import matplotlib.pyplot as plt


PATH = 'graph/'

x0 = [1, 3, 5, 7, 9]
y0 = [2, 3, 7, 1, 0]

x1 = [2, 4, 6, 8, 9]
y1 = [5, 1, 3, 7, 4]

if __name__ == '__main__':
    graph = 'scatterplot'

    plt.scatter(x0, y0, label = "red", color="r")
    plt.scatter(x1, y1, label = "blue", color="b")

    plt.title('Example: '+ graph +' graph')
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.legend()

    plt.savefig(PATH + graph +'.pdf')
