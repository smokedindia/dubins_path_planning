import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection, LineCollection
from matplotlib.patches import Rectangle
import matplotlib.animation as animation
import numpy as np
import argparse

from dpp.env.grid import Grid
from dpp.env.car import SimpleCar
from dpp.env.environment import Environment
from dpp.test_cases.cases import TestCase, Hot6Case
from dpp.utils.utils import plot_a_car
from dpp.methods.hybrid_astar import HybridAstar

from time import time
import math


def main(parking_idx, heu=1, reverse=False, extra=False, grid_on=False, backward=False, save=False):
    # tc = TestCase()
    tc = Hot6Case(parking_idx=parking_idx, backward=backward)

    env = Environment(tc.obs)

    car = SimpleCar(env, tc.start_pos, tc.end_pos, l=0.5, max_phi=math.pi / 5)

    grid = Grid(env, cell_size=0.1)

    hastar = HybridAstar(car, grid, reverse, unit_theta=math.pi / 10)

    t = time()
    path, closed_ = hastar.search_path(heu, extra)
    end = time()
    print("Total time: {}s".format(round(end - t, 3)))

    if not path:
        print("No valid path!")
        return

    path = path[::5] + [path[-1]]

    branches = []
    bcolors = []
    for node in closed_:
        for b in node.branches:
            branches.append(b[1:])
            bcolors.append("y" if b[0] == 1 else "b")

    xl, yl = [], []
    carl = []
    for i in range(len(path)):
        xl.append(path[i].pos[0])
        yl.append(path[i].pos[1])
        carl.append(path[i].model[0])

    start_state = car.get_car_state(car.start_pos)
    end_state = car.get_car_state(car.end_pos)

    # plot and annimation
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, env.lx)
    ax.set_ylim(0, env.ly)
    ax.set_aspect("equal")

    if grid_on:
        ax.set_xticks(np.arange(0, env.lx, grid.cell_size))
        ax.set_yticks(np.arange(0, env.ly, grid.cell_size))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.tick_params(length=0)
        plt.grid(which="both")
    else:
        ax.set_xticks([])
        ax.set_yticks([])

    for ob in env.obs:
        ax.add_patch(Rectangle((ob.x, ob.y), ob.w, ob.h, fc="gray", ec="k"))

    ax.plot(car.start_pos[0], car.start_pos[1], "ro", markersize=6)
    plt.title(f'time: {round(end - t, 3)}s')
    ax = plot_a_car(ax, end_state.model)
    ax = plot_a_car(ax, start_state.model)

    # _branches = LineCollection(branches, color='b', alpha=0.8, linewidth=1)
    # ax.add_collection(_branches)

    # _carl = PatchCollection(carl[::20], color='m', alpha=0.1, zorder=3)
    # ax.add_collection(_carl)
    # ax.plot(xl, yl, color='whitesmoke', linewidth=2, zorder=3)
    # _car = PatchCollection(path[-1].model, match_original=True, zorder=4)
    # ax.add_collection(_car)

    _branches = LineCollection([], linewidth=1)
    ax.add_collection(_branches)

    (_path,) = ax.plot([], [], color="lime", linewidth=2)
    _carl = PatchCollection([])
    ax.add_collection(_carl)
    (_path1,) = ax.plot([], [], color="w", linewidth=2)
    _car = PatchCollection([])
    ax.add_collection(_car)

    frames = len(branches) + len(path) + 1

    def init():
        _branches.set_paths([])
        _path.set_data([], [])
        _carl.set_paths([])
        _path1.set_data([], [])
        _car.set_paths([])

        return _branches, _path, _carl, _path1, _car

    def animate(i):
        edgecolor = ["k"] * 5 + ["r"]
        facecolor = ["y"] + ["k"] * 4 + ["r"]

        if i < len(branches):
            _branches.set_paths(branches[: i + 1])
            _branches.set_color(bcolors)

        else:
            _branches.set_paths(branches)

            j = i - len(branches)

            _path.set_data(xl[min(j, len(path) - 1) :], yl[min(j, len(path) - 1) :])

            sub_carl = carl[: min(j + 1, len(path))]
            _carl.set_paths(sub_carl[::4])
            _carl.set_edgecolor("k")
            _carl.set_facecolor("m")
            _carl.set_alpha(0.1)
            _carl.set_zorder(3)

            _path1.set_data(xl[: min(j + 1, len(path))], yl[: min(j + 1, len(path))])
            _path1.set_zorder(3)

            _car.set_paths(path[min(j, len(path) - 1)].model)
            _car.set_edgecolor(edgecolor)
            _car.set_facecolor(facecolor)
            _car.set_zorder(3)

        return _branches, _path, _carl, _path1, _car

    ani = animation.FuncAnimation(
        fig, animate, init_func=init, frames=frames, interval=10, repeat=True, blit=True
    )
    # save animation
    fpath = f"hybrid_astar_{parking_idx}.mp4" if not backward else f"hybrid_astar_{parking_idx}_r.mp4"
    if save:
        ani.save(fpath, writer='ffmpeg', fps=30)
        np.save(fpath.replace('.mp4', '.npy'), np.array([p.pos for p in path]))

    plt.show()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("-heu", type=int, default=1, help="heuristic type")
    p.add_argument("-r", "--reverse", default=True, help="allow reverse or not")
    p.add_argument('-b', "--backward", action='store_true', help='backward parking')
    p.add_argument("-e", "--extra", action="store_true", help="add extra cost or not")
    p.add_argument("-g", "--grid_on", action="store_true", help="show grid or not")
    p.add_argument("--parking_idx", type=int, default=2, help="parking index")
    p.add_argument("-s", "--save", action="store_true", help="save animation")
    args = p.parse_args()

    main(**vars(args))
