import matplotlib.pyplot as plt


PATH = 'matplotlib/view/graph/'
GRAPH = 'line'

x0 = [1, 3, 5, 7, 9]
y0 = [2, 3, 7, 1, 0]

x1 = [2, 4, 6, 8, 9]
y1 = [5, 1, 3, 7, 4]

''' matplotlib 
    color:
        'b' blue
        'g' green
        'r' red
        'c' cyan
        'm' magenta
        'y' yellow
        'k' black
        'w' white
        '#000000' black in hexadecimal
    label:
        "label name"
    linestyle: 
        '-' solid line style
        '--' dashed line style
        '-.' dash-dot line style
        ':' dotted line style
    linewidth:
        2
    marker: marcador
        '.' point marker
        ',' pixel marker
        'o' circle marker
        'v' triangle_down marker
        '^' triangle_up marker
        '<' triangle_left marker
        '>' triangle_right marker
        '1' tri_down marker
        '2' tri_up marker
        '3' tri_left marker
        '4' tri_right marker
        's' square marker
        'p' pentagon marker
        '*' star marker
        'h' hexagon1 marker
        'H' hexagon2 marker
        '+' plus marker
        'x' x marker
        'D' diamond marker
        'd' thin_diamond marker
        '|' vline marker
        '_' hline marker
    .
    Reference
        https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
'''
plt.plot(x0, y0, label = "red", color="#000000", linestyle=":", linewidth=3)
plt.plot(x1, y1, label = "blue", color="b", marker=".")

plt.title('Example: '+GRAPH+' graph')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()

plt.savefig(PATH+GRAPH+'.pdf', dpi=300)