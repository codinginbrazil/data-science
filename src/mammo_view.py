import pandas as pd


if __name__ == "__main__" :
    path = ("data/mammographic/imputation.csv")
    try: 
        df = pd.read_csv(path)
    except:
        print("pandas did not find the dataset source")

    path = "view/graph/mammo/age_boxplot.pdf"
    ax = df.boxplot(column=['AGE'])
    ax.figure.savefig(path, dpi=300)
    ax.cla()   # Clear axis
    
    path = "view/graph/mammo/age_histogram.pdf"
    ax = ((df.iloc[:, 1]).plot.hist(bins=16, alpha=.9))
    ax.figure.savefig(path, dpi=300)
    