import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Parameters
a = np.array([1.2, 1.0, 0.8])
b = np.array([
    [1.0, 0.8, 0.8],
    [0.8, 1.0, 0.8],
    [0.8, 0.8, 1.0]
])

dt = 0.05
T = 20
steps = int(T / dt)

x = np.array([0.33, 0.33, 0.34])
history = []

for _ in range(steps):
    history.append(x.copy())
    dx = x * (a - b.dot(x))
    x = x + dt * dx

history = np.array(history)

# Animation
fig, ax = plt.subplots()
ax.set_xlim(0, T)
ax.set_ylim(0, 1)
ax.set_xlabel("Time")
ax.set_ylabel("Market Share")

line1, = ax.plot([], [], label="Company A")
line2, = ax.plot([], [], label="Company B")
line3, = ax.plot([], [], label="Company C")
ax.legend()

def update(frame):
    t = np.linspace(0, frame*dt, frame)
    line1.set_data(t, history[:frame,0])
    line2.set_data(t, history[:frame,1])
    line3.set_data(t, history[:frame,2])
    return line1, line2, line3

ani = FuncAnimation(fig, update, frames=len(history), interval=50)

writer = PillowWriter(fps=20)
ani.save("market_simulation.gif", writer=writer)

print("BITTI")
