import random
import matplotlib.pyplot as plt

PATH = 'graph/'

dt = [1,2,4,6,8,12,512,12,2]

for i in range(1000):
    random_number = random.randint(0,1000)
    dt.append(random_number)

plt.boxplot(dt)

plt.title("boxplot")

plt.savefig(PATH+"boxplot.pdf")