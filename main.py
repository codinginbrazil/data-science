import matplotlib.pyplot as plt


PATH = 'graph/'

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 3]

if __name__ == '__main__':

    plt.bar(x, y)

    plt.title("Example: Bar graph")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")

    plt.savefig(PATH+'bar.pdf')
