import matplotlib.pyplot as plt
from matplotlib import animation
from orbit import AU, xelist, yelist, xslist, yslist

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
ax.grid()

line_e, = ax.plot([], [], '-g', lw=0, c='blue')
point_e, = ax.plot([AU], [0], marker='o',
                   markersize=4,
                   markeredgecolor='blue',
                   markerfacecolor='blue')
text_e = ax.text(AU, 0, 'Earth')
point_s, = ax.plot([0], [0], marker='o',
                   markersize=7,
                   markeredgecolor='yellow',
                   markerfacecolor='yellow')
text_s = ax.text(0, 0, 'Sun')

# earth track
exdata, eydata = [], []

# sun track
sxdata, sydata = [], []

print(len(xelist))


def update(i):
    exdata.append(xelist[i])
    eydata.append(yelist[i])

    line_e.set_data(exdata, eydata)
    point_e.set_data(xelist[i], yelist[i])
    text_e.set_position((xelist[i], yelist[i]))

    point_s.set_data(xslist[i], yslist[i])
    text_s.set_position((xslist[i], yslist[i]))

    ax.axis('equal')
    ax.set_xlim(-3 * AU, 3 * AU)
    ax.set_ylim(-3 * AU, 3 * AU)

    return line_e, point_s, point_e, text_e, text_s


anim = animation.FuncAnimation(
    fig,
    func=update,
    frames=len(xelist),
    interval=1,
    blit=True
)
plt.show()
