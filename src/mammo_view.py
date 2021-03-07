import pandas as pd


path = ("data/mammographic/imputation.csv")

try: 
    df = pd.read_csv(path)
except:
    print("pandas did not find the dataset source")

path = "view/graph/mammo/age.pdf"
ax = ((df.iloc[:, 1]).plot.hist(bins=12, alpha=0.5))
ax.figure.savefig(path, dpi=300)

