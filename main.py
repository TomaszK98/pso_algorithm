from tkinter import *
from backend_part import *

def plot_command():

    best_cost_pos = pso(float(c1_text.get()), float(c2_text.get()), float(w_text.get()), int(particles_text.get()), int(iter_text.get()), func_text.get())
    best_cost = best_cost_pos[0]
    best_pos = best_cost_pos[1]

    cost_value = Label(root, text=best_cost)
    cost_value.place(relx=0.2, rely=0.2, relheight=0.08, relwidth=0.2)

    pos_value = Label(root, text=best_pos)
    pos_value.place(relx=0.5, rely=0.2, relheight=0.08, relwidth=0.2)

    plot_show(func_text.get())

root = Tk()
root.wm_title("PSO ALGORITHM")

canvas = Canvas(root, height = 400, width = 800)
canvas.grid()

start_button = Button(root, text = "Start",width = 10, command = plot_command, bg = "light blue")
start_button.place(relx = 0.05, rely = 0.1,relheight = 0.08, relwidth = 0.05)

particles_label = Label(root, text = "Particles: ")
particles_label.place(relx = 0.1, rely = 0.1,relheight = 0.08, relwidth = 0.1)

particles_text = StringVar()
particles_text.set("50")
particles_entry = Entry(root, textvariable = particles_text)
particles_entry.place(relx = 0.2, rely = 0.1,relheight = 0.08, relwidth = 0.1)

c1_label = Label(root, text = "C1: ")
c1_label.place(relx = 0.3, rely = 0.1,relheight = 0.08, relwidth = 0.05)

c1_text = StringVar()
c1_text.set("0.5")
c1_entry = Entry(root, textvariable = c1_text)
c1_entry.place(relx = 0.35, rely = 0.1,relheight = 0.08, relwidth = 0.1)

c2_label = Label(root, text = "C2: ")
c2_label.place(relx = 0.45, rely = 0.1,relheight = 0.08, relwidth = 0.05)

c2_text = StringVar()
c2_text.set("0.3")
c2_entry = Entry(root, textvariable = c2_text)
c2_entry.place(relx = 0.5, rely = 0.1,relheight = 0.08, relwidth = 0.1)

w_label = Label(root, text = "W: ")
w_label.place(relx = 0.6, rely = 0.1,relheight = 0.08, relwidth = 0.05)

w_text = StringVar()
w_text.set("0.9")
w_entry = Entry(root, textvariable = w_text)
w_entry.place(relx = 0.65, rely = 0.1,relheight = 0.08, relwidth = 0.1)

iter_label = Label(root, text = "Iterations: ")
iter_label.place(relx = 0.75, rely = 0.1,relheight = 0.08, relwidth = 0.1)

iter_text = StringVar()
iter_text.set("50")
iter_entry = Entry(root, textvariable = iter_text)
iter_entry.place(relx = 0.85, rely = 0.1,relheight = 0.08, relwidth = 0.1)

func_text = StringVar(root)
func_text.set("Sphere")

w = OptionMenu(root, func_text, "Sphere", "Ackley's")
w.place(relx = 0.85, rely = 0.2,relheight = 0.08, relwidth = 0.1)

cost_label = Label(root, text="Best cost: ")
cost_label.place(relx=0.1, rely=0.2, relheight=0.08, relwidth=0.1)

pos_label = Label(root, text="Best pos: ")
pos_label.place(relx=0.4, rely=0.2, relheight=0.08, relwidth=0.1)

root.mainloop()


