import matplotlib.pyplot as plt


PATH_DATA = 'data/ncbi/'
PATH_OUTPUT = 'view/html/'

""" Source: NCBI
    * Human 18S rRNA gene:
        https://www.ncbi.nlm.nih.gov/nuccore/M10098.1?report=fasta
    * Escherichia coli strain U 5/41 16S ribosomal RNA:
        https://www.ncbi.nlm.nih.gov/nuccore/NR_024570.1?report=fasta
"""
dt_human = open(PATH_DATA+"human.fasta").read()
dt_bacteria = open(PATH_DATA+"bacteria.fasta").read()

html_human = open(PATH_OUTPUT+"human.html", "w")
html_bacteria = open(PATH_OUTPUT+"bacteria.html", "w")

dict_nucleobase = ['A', 'T', 'C', 'G']

count = {}

for i in dict_nucleobase:
    for j in dict_nucleobase:
        count[i+j] = 0

dt_bacteria = dt_bacteria.replace("\n", "")

for k in range(len(dt_bacteria)-1):
    count[dt_bacteria[k]+dt_bacteria[k+1]] += 1

print(count)

# HTML
i = 1
for k in count:
    info = count[k] / max(count.values())
    html_bacteria.write(
        "<div "
        +"style='width:100px; "
        +"border:1px solid #111; "
        +"height:100px; "
        +"float: left; "
        +"background-color: rgba(0,0,0,"
        + str(info) 
        +"'></div>"
    )

    if i%4 == 0:
        html_bacteria.write(
            "<div style ='clear:both'><div>"
        )
    i += 1
    
html_bacteria.close()
