import pyswarms as ps
import matplotlib.pyplot as plt
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history, plot_contour, plot_surface
from pyswarms.utils.plotters.formatters import Mesher, Designer

def pso(c1,c2,w,particles,iters,func):
    options = {'c1':c1,
               'c2':c2,
               'w':w}

    optimizer = ps.single.GlobalBestPSO(n_particles=particles,
                                        dimensions=2,
                                        options=options)

    if func == "Sphere":

        x = optimizer.optimize(fx.ackley, iters=iters)

        m = Mesher(func=fx.sphere,
                   limits=[(-1, 1), (-1, 1)])

    elif func =="Ackley's":

        optimizer.optimize(fx.ackley, iters=iters)

        m = Mesher(func=fx.ackley,
                   limits=[(-1.5, 1.5), (-1.5, 1.5)])


    # Plot the cost
    # plot_cost_history(optimizer.cost_history)

    # Adjust figure limits
    d = Designer(limits=[(-1,1), (-1,1), (-0.1,1)],
                 label=['x-axis', 'y-axis', 'z-axis'])

    # animation2d = plot_contour(pos_history=optimizer.pos_history,
    #                            mesher=m, designer=d,
    #                            mark=(0,0))

    pos_history_3d = m.compute_history_3d(optimizer.pos_history) # preprocessing
    animation3d = plot_surface(pos_history=pos_history_3d,
                               mesher=m, designer=d,
                               mark=(0,0,0))

    plt.show()
    return x
