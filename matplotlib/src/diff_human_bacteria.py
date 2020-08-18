import matplotlib.pyplot as plt


PATH_DATA = 'matplotlib/data/ncbi/'
PATH_OUTPUT = 'matplotlib/view/html/'

DICT_NUCLEOBASE = ['A', 'T', 'C', 'G']

""" Source: NCBI
    * Human 18S rRNA gene:
        https://www.ncbi.nlm.nih.gov/nuccore/M10098.1?report=fasta
    * Escherichia coli strain U 5/41 16S ribosomal RNA:
        https://www.ncbi.nlm.nih.gov/nuccore/NR_024570.1?report=fasta
"""
def histogram(path_of_data, dictionary):
    count = {}
    data = open(path_of_data).read()
    data = data.replace("\n", "")

    for i in dictionary:
        for j in dictionary:
            count[i+j] = 0

    for k in range(len(data)-1):
        count[data[k]+data[k+1]] += 1
    return count


def export_html(histogram):
    i = 1
    html_nucleobase = open(PATH_OUTPUT+NUCLEOBASE+".html", "w")

    for k in histogram:
        normalization = histogram[k] / max(histogram.values())
        html_nucleobase.write(
            "<div "
            +"style='width:100px; "
            +"border:1px solid #111; "
            +"height:100px; "
            +"float: left; "
            +"background-color: rgba(0,0,0,"
            + str(normalization) 
            +"'></div>"
        )
        if i%4 == 0:
            html_nucleobase.write(
                "<div style ='clear:both'><div>"
            )
        i += 1
    html_nucleobase.close()


if __name__ == '__main__':
    NUCLEOBASE = "human" #or "bacteria"

    hist = histogram((PATH_DATA+NUCLEOBASE+".fasta"), DICT_NUCLEOBASE)
    export_html(hist)