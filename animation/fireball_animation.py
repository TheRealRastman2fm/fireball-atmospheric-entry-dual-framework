import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------
# Physical parameters (simplified model)
# -----------------------------
g = 9.81                     # gravity (m/s^2)
Cd = 1.0                     # drag coefficient
A = 0.5                      # cross-sectional area (m^2)
m = 1000                    # meteoroid mass (kg)
rho0 = 1.2                  # sea level density
H = 8000                    # scale height (m)

# -----------------------------
# Initial conditions
# -----------------------------
v0 = 20000                 # initial velocity (m/s)
h0 = 100000               # initial altitude (m)

dt = 0.05
t_max = 60

# -----------------------------
# Storage arrays
# -----------------------------
t_vals = []
h_vals = []
v_vals = []
e_vals = []

# -----------------------------
# Initial state
# -----------------------------
h = h0
v = -v0   # downward
t = 0

# -----------------------------
# Time integration (Euler method)
# -----------------------------
while h > 0 and t < t_max:

    rho = rho0 * np.exp(-h / H)  # atmospheric density

    drag = 0.5 * Cd * rho * A * v**2 / m

    # equations of motion
    dv = g - drag * np.sign(v)
    dh = v

    v = v + dv * dt
    h = h + dh * dt

    # energy
    E = 0.5 * m * v**2

    t_vals.append(t)
    h_vals.append(max(h, 0))
    v_vals.append(abs(v))
    e_vals.append(E)

    t += dt

# -----------------------------
# Convert to arrays
# -----------------------------
t_vals = np.array(t_vals)
h_vals = np.array(h_vals)
v_vals = np.array(v_vals)
e_vals = np.array(e_vals)

# -----------------------------
# Figure setup
# -----------------------------
fig, ax = plt.subplots(1, 1, figsize=(7,5))

ax.set_xlim(0, t_vals[-1])
ax.set_ylim(0, h0)

line, = ax.plot([], [], lw=2, color='red')
dot, = ax.plot([], [], 'bo')

ax.set_xlabel("Time (s)")
ax.set_ylabel("Altitude (m)")
ax.set_title("Fireball Atmospheric Entry Simulation")

# -----------------------------
# Animation function
# -----------------------------
def update(i):
    line.set_data(t_vals[:i], h_vals[:i])
    dot.set_data(t_vals[i], h_vals[i])
    return line, dot

ani = FuncAnimation(fig, update, frames=len(t_vals), interval=20)

# -----------------------------
# Save animation (choose one)
# -----------------------------

# MP4 (best for journals)
ani.save("fireball_trajectory.mp4", fps=30, dpi=300)

# OR GIF (for GitHub/README)
# ani.save("fireball_trajectory.gif", writer='pillow', fps=30)

plt.show()