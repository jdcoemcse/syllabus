import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
u, v = np.meshgrid(np.linspace(0, 2*np.pi, 100), np.linspace(-0.3, 0.3, 20))
x, y, z = (1 + v*np.cos(u/2)) * np.cos(u), (1 + v*np.cos(u/2)) * np.sin(u), v*np.sin(u/2)
def update(frame):
    ax.clear()
    angle = np.radians(frame)
    rot = np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
    x_rot, y_rot, z_rot = np.dot(rot, [x.flatten(), y.flatten(), z.flatten()]).reshape(3, *x.shape)
    ax.set(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), zlim=(-0.5, 0.5))
    return ax.plot_surface(x_rot, y_rot, z_rot, color='red', edgecolor='k', alpha=0.6),
ani = animation.FuncAnimation(fig, update, frames=range(0, 360, 2), blit=False)
plt.show()