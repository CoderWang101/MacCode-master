import numpy as np
from matplotlib import pyplot as plt

k = 1
m1 = 2
s1 = np.array((0, 0))
v1 = np.array((0, 1))
m2 = 2
s2 = np.array((1, 0))
v2 = np.array((0, -1))

def a(s1, s2):
    r2 = np.sum(np.square(s1 - s2))
    f = k * m1 * m2 / r2

    alpha = np.arctan2(s2[1] - s1[1], s2[0] - s1[0])
    fy = f * np.sin(alpha)
    fx = f * np.cos(alpha)
    # f = k * m1 * m2 / r**2 = mi * ai
    a1 = np.array([fx/m1, fy/m1])
    a2 = np.array([-fx/m2, -fy/m2])
    return a1, a2


def get_new(dt, s1, v1, a1, s2, v2, a2):
    new_s1 = s1 + v1 * dt
    new_s2 = s2 + v2 * dt
    new_v1 = v1 + a1 * dt
    new_v2 = v2 + a2 * dt
    new_a1, new_a2 = a(s1, s2)
    return new_s1, new_v1, new_a1, new_s2, new_v2, new_a2

def get_all_s(t, dt):
    global s1, v1, a1, s2, v2, a2, m1, m2, k
    a1, a2 = a(s1, s2)
    ss1, ss2 = [s1], [s2]
    for _ in np.arange(0, t, dt):
        s1, v1, a1, s2, v2, a2 = get_new(dt, s1, v1, a1, s2, v2, a2)
        ss1.append(s1)
        ss2.append(s2)
    return np.array(ss1), np.array(ss2)

if __name__ == '__main__':
    ss1, ss2 = get_all_s(200, 0.01)
    print(ss1)
    print(ss2)

    plt.plot(ss1[:, 0], ss1[:, 1], color='red', label='ball 1')
    plt.plot(ss2[:, 0], ss2[:, 1], color='blue', label='ball 2')
    plt.legend()
    plt.show()
