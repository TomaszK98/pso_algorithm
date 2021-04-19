import pyswarms as ps
import matplotlib.pyplot as plt
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history, plot_contour, plot_surface
from pyswarms.utils.plotters.formatters import Mesher, Designer
import random

def plot_show(func):

    if func == "Sphere":

        m = Mesher(func=fx.sphere,
                   limits=[(-1, 1), (-1, 1)])
    elif func == "Ackley's":

        m = Mesher(func=fx.ackley,
                   limits=[(-1.5, 1.5), (-1.5, 1.5)])

    d = Designer(limits=[(-1, 1), (-1, 1), (-0.1, 1)],
                 label=['x-axis', 'y-axis', 'z-axis'])

    pos_history_3d = m.compute_history_3d(optimizer.pos_history)  # preprocessing
    animation3d = plot_surface(pos_history=pos_history_3d,
                               mesher=m, designer=d,
                               mark=(0, 0, 0))
    plt.show()

def pso(c1,c2,w,particles,iters,func):

    options = {'c1':c1,
               'c2':c2,
               'w':w}

    center = random.randint(-32,32)

    global optimizer
    optimizer = ps.single.GlobalBestPSO(n_particles=particles,
                                        dimensions=2,
                                        options=options,
                                        center=center,
                                        init_pos=None)

    if func == "Sphere":

        optimizer_value = optimizer.optimize(fx.sphere, iters=iters)

    elif func =="Ackley's":

        optimizer_value = optimizer.optimize(fx.ackley, iters=iters)

    return optimizer_value

