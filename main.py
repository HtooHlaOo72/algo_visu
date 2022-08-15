from email import message
from multiprocessing.dummy import Array
from pickle import TRUE
from threading import Condition, Thread, active_count, main_thread
import tkinter as tk
from tkinter import font
from tkinter import *
from tkinter import BOTH, ttk
from turtle import bgcolor
import random
from tkinter import messagebox
from matplotlib.ft2font import HORIZONTAL
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.selection_sort import selection_sort
from tkinter import Scale

algo_list = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort"]
speed_list = ["Slow", "Medium", "Fast"]

window_width = 700
window_height = 900
window_x = 50
window_y = 50
window = tk.Tk()
window.title("Algorithm Visualizer")

algorithm = tk.StringVar()
speed = tk.StringVar()
input_count = tk.IntVar()
step_count = tk.IntVar()
# speed_num = tk.DoubleVar()
# speed_num.set(0.0)
# control = {
#     "condition": Condition(),
#     "state": tk.BooleanVar()
# }
data_cache = []
data = [0] * input_count.get()

# for fonts;
font.families()
Desired_font = font.Font(family="Comic Sans MS", size=12, weight="bold")
Heading_font = font.Font(family="Comic Sans MS", size=20, weight="bold")


# main functions
def drawGraph(data, colors):
    global graph_canvas
    graph_canvas.delete("all")
    no_of_inputs = input_count.get()
    c_height = graph_canvas.winfo_height()
    c_width = graph_canvas.winfo_width()
    column_width = c_width/no_of_inputs
    one_unit_height = c_height/max(data)
    for i, v in enumerate(data):
        x1 = column_width*i
        x2 = x1+column_width
        y1 = c_height
        y2 = one_unit_height*(max(data)-v)

        graph_canvas.create_rectangle(
            x1, y1, x2, y2, fill=colors[i], outline="white")
        textX = x2-(column_width/2)
        textY = y2-10
        graph_canvas.create_text(
            textX, y1-12, text=str(data[i]), fill="white", font=("Roboto 8 bold"))
    window.update_idletasks()
# speed_box.grid(row=1,column=2,pady=5)
# speed_box.current(0)rectangle(x1,y1,x2,y2,fill=colors[i],outline="white")


def generateRandom(n=input_count):
    global data
    global data_cache
    step_count.set(0)
    data = []
    for i in range(0, n.get()):
        random_value = random.randint(1, 100)
        data.append(random_value)
    # cache
    data_cache = [x for x in data]
    drawGraph(data, ["#1D0B3B" for x in range(len(data))])


def increase_step():
    step_count.set(step_count.get()+1)


def notify(c):
    while (not control["state"].get()):
        c.acquire()
        c.notify()
        c.release()


def back_to_previous():
    global data
    data = [x for x in data_cache]
    step_count.set(0)
    drawGraph(data, ["#1D0B3B" for x in range(len(data))])


# def pause():
#     global control
#     control['state'].set(not control["state"].get())
#     print(control["state"].get())
#     if (not control["state"].get()):
#         pause_btn['text'] = "Pause"
#         print("pause thread", control["state"].get())
#         pause_thread = Thread(target=pause_control)
#         pause_thread.start()
#     else:
#         pause_btn['text'] = "Resume"


# def pause_control():
#     print("Pause Control")
#     global control
#     if (not control["state"].get()):
#         control["condition"].acquire()
#         control["condition"].notify_all()
#         control["condition"].release()
#     # global control
#     # noti = None
#     # if(not control["state"].get()):
#     #     noti = Thread(target=notify,args=(control["condition"]))
#     #     noti.start()
#     #     control["state"].set(True)
#     # else:
#     #     control["state"].set(False)
#     # noti = None

# command functions


def sort():
    global algorithm
    global speed
    global control
    
    if len(data) <= 0:
        messagebox.showwarning("Instruction", "Generate some numbers")
        return
    speedDict = {"Slow": 0.6, "Medium": 0.08, "Fast": 0.000000000008}
    algoDict = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
    }
    sort_fn = algoDict[algorithm.get()]
    
    if (algorithm.get() == "Merge Sort"):
        sort_fn(data, 0, len(data)-1,speedDict[speed.get()], drawGraph, increase_step)
    else:
        sort_fn(data, speedDict[speed.get()], drawGraph, increase_step)


def resizeCanvas(e):
    global graph_canvas
    global data
    g_width = graph_canvas.winfo_width()
    g_height = graph_canvas.winfo_height()
    if (e.type != 22 and g_width == window.winfo_width() and len(data) > 0):
        drawGraph(data, ["#1D0B3B" for x in range(len(data))])
    graph_canvas.config(width=window.winfo_width(), height=e.height)


# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

window.resizable(True, True)

form_frame = tk.Frame(window, height=400, background="#280B56")
# form_frame.grid(row=0,column=0,sticky="ew")
form_frame.pack(side=tk.TOP, fill=tk.BOTH)

# styles
style = ttk.Style()
style.configure("style.TCombobox", padding=6, foreground="#280B56")
style.configure("style.TButton", padding=6,
                relief="flat", foreground="#280B56")
style.configure("style.TSpinbox", padding=6,
                relief="flat", foreground="#280B56")
style.configure("style.TScale",padding = 6)

# heading
algo_label = tk.Label(form_frame, text="Algo Visu Project",
                      font=Heading_font, fg="white", bg="#280B56")
algo_label.grid(row=0, column=0, sticky="w", pady=5)

# algorithm choice box
algo_label = tk.Label(form_frame, text="Algorithm",
                      font=Desired_font, fg="white", bg="#280B56")
algo_label.grid(row=1, column=0, sticky="w", pady=5)
algo_box = ttk.Combobox(form_frame, textvariable=algorithm,
                        values=algo_list, state="readonly", style="style.TCombobox")
algo_box.grid(row=1, column=2, pady=5)
algo_box.current(0)

# speed choice box
speed_label = tk.Label(form_frame, text="Speed",
                       font=Desired_font, fg="white", bg="#280B56")
speed_label.grid(row=2, column=0, sticky="w", pady=5)
# speed_slide = Scale(form_frame, from_=0, to=100,
#                     orient="horizontal", variable=speed_num, activebackground="#280B56", bg="white", bd=1, length=145)
# speed_slide.grid(row=2, column=2)
# speed_slide.set(10)
speed_box = ttk.Combobox(form_frame, textvariable=speed,
                        values=speed_list, state="readonly", style="style.TCombobox")
speed_box.grid(row=1, column=2, pady=5)
speed_box.current(0)
speed_box.grid(row=2, column=2,pady=5)
# no of input box
ninput_label = tk.Label(form_frame, text="No of inputs",
                        font=Desired_font, fg="white", bg="#280B56")
ninput_label.grid(row=3, column=0, sticky="w", pady=5)
ninput_box = ttk.Spinbox(form_frame, from_=1, to=30,
                        textvariable=input_count, style="style.TSpinbox")
input_count.set(20)
ninput_box.grid(row=3, column=2, sticky='w', pady=5)

# buttons
generate_btn = ttk.Button(form_frame, text="Generate", command=generateRandom)
generate_btn.grid(row=4, column=2, sticky="w", pady=5)

# pause_btn = ttk.Button(form_frame, text="Pause", command=pause)
# pause_btn.grid(row=4, column=3, sticky="w", pady=5)

sort_btn = ttk.Button(form_frame, text="Sort", command=sort)
sort_btn.grid(row=5, column=2, sticky="w", pady=5)

reset_btn = ttk.Button(form_frame, text="Reset", command=back_to_previous)
reset_btn.grid(row=5, column=3, sticky="w", pady=5)

# steps display
step_label = tk.Label(form_frame, text="Steps: ",
                      font=Desired_font, fg="white", bg="#280B56")
step_label.grid(row=6, column=0, sticky="w", pady=5)
step_value = tk.Label(form_frame, textvariable=step_count,
                      font=Desired_font, fg="white", bg="#280B56")
step_value.grid(row=6, column=2, sticky="w", pady=5)

# graph frame
graph_frame = tk.Frame(window, background="gray", height=500)
# graph_frame.grid(row=1,sticky="ew")
graph_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# graph canvas
graph_canvas = tk.Canvas(graph_frame, height=450, width=550, bg="grey")
graph_canvas.bind('<Configure>', resizeCanvas)
graph_canvas.pack()
# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# run the window
window.mainloop()
