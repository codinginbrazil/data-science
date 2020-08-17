import matplotlib.pyplot as plt


PATH = 'graph/'

x = [1, 2, 5]
y = [2, 3, 7]

if __name__ == '__main__':

    plt.title("Example: Line graph")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")

    plt.plot(x, y)

    # plt.show()
    plt.savefig(PATH+'line.pdf')
