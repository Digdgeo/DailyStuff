
import matplotlib
import matplotlib.lines as mlines
matplotlib.rcParams['axes.formatter.useoffset'] = False

season = {0.5: {'Siembra': 5, 'Recogida': 10},
          1.5: {'Siembra': 1, 'Recogida': 7},
          2.5: {'Siembra': 3, 'Recogida': 8},
          3.5: {'Siembra': 4, 'Recogida': 7}}

df = pd.DataFrame.from_dict(season).T


# Func to draw line segment
def newline(p1, p2, color='black'):
    ax = plt.gca()
    l = mlines.Line2D([p1[0],p2[0]], [p1[1],p2[1]], color='green', lw=3)
    ax.add_line(l)
    return l

# Figure and Axes
fig, ax = plt.subplots(1,1,figsize=(14,7), facecolor='#f7f7f7', dpi= 80)

# Vertical Lines
for i in range(1,12):
    
    ax.vlines(x=i, ymin=0, ymax=4, color='black', alpha=1, linewidth=1, linestyles='dotted')

# Points
ax.scatter(y=df.index, x=df['Siembra'], s=50, color='olive', alpha=0.7)
ax.scatter(y=df.index, x=df['Recogida'], s=50, color='olive', alpha=0.7)

# Line Segments
for i, p1, p2 in zip(df.index, df['Siembra'], df['Recogida']):
    newline([p1, i], [p2, i])
    
# Decoration
ax.set_facecolor('#f7f7f7')
ax.set_title("Dumbell Chart: Cultivos 2002", fontdict={'size':22})
ax.set(xlim=(0,12), ylim=(0, 4), ylabel='Cultivos')
ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])
ax.set_xticklabels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])


ax.set_yticks([0.5, 1.5, 2.5, 3.5])

ax.set_yticklabels(['Algodon', 'Cereal', 'Girasol', 'Remolacha'])

#ax.plot(data)

plt.show()

