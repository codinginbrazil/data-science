import pandas as pd


if __name__ == "__main__" :
    path = ("dataset/forest_fires/source.csv")
    try: 
        df = pd.read_csv(path)
    except:
        print("pandas did not find the dataset source")

    path = "view/graph/forest_fires/temp_boxplot.pdf"
    ax = df.boxplot(column=['temp'])
    ax.figure.savefig(path, dpi=300)
    ax.cla()   # Clear axis
    
    path = "view/graph/forest_fires/temp_histogram.pdf"
    ax = ((df.iloc[:, 8]).plot.hist(bins=6, alpha=.9))
    ax.figure.savefig(path, dpi=300)
    ax.cla()   # Clear axis
    
    
    path = "view/graph/forest_fires/DC_boxplot.pdf"
    ax = df.boxplot(column=['DC'])
    ax.figure.savefig(path, dpi=300)
    ax.cla()   # Clear axis
    
    path = "view/graph/forest_fires/DC_histogram.pdf"
    ax = ((df.iloc[:, 6]).plot.hist(bins=10, alpha=.9))
    ax.figure.savefig(path, dpi=300)
    ax.cla()   # Clear axis
    
    
    path = "view/graph/forest_fires/DMC_boxplot.pdf"
    ax = df.boxplot(column=['DMC'])
    ax.figure.savefig(path, dpi=300)
    ax.cla()   # Clear axis
    
    path = "view/graph/forest_fires/DMC_histogram.pdf"
    ax = ((df.iloc[:, 5]).plot.hist(bins=10, alpha=.9))
    ax.figure.savefig(path, dpi=300)
    ax.cla()   # Clear axis