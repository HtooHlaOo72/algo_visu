from pickle import TRUE
import tkinter as tk
from tkinter import BOTH, ttk
from turtle import bgcolor
import random

algo_list = ["Bubble Sort","Insertion Sort","Selection Sort"]
speed_list = ["Slow","Medium","Fast"]

window_width = 700
window_height = 900
window_x = 50
window_y = 50
window = tk.Tk()
window.title("Algorithm Visualizer")

data=[]
algorithm = tk.StringVar()
speed = tk.StringVar()
input_count =tk.IntVar()

#main functions
def drawGraph():

    no_of_inputs= input_count.get()
    global graph_canvas
    graph_canvas.delete("all")
    c_height=graph_canvas.winfo_height()
    c_width =graph_canvas.winfo_width()
    offset=4
    column_width = c_width/no_of_inputs
    one_unit_height = c_height/max(data)
    data_for_graph = [i/max(data) for i in data]
    print(data_for_graph,one_unit_height)
    for i,v in enumerate(data):
        x1=column_width*i
        x2=x1+column_width
        y1=c_height
        y2=one_unit_height*v

        graph_canvas.create_rectangle(x1,y1,x2,y2,fill="black",outline="yellow")
    window.update_idletasks()


def generateRandom(n=input_count):

    global data
    for i in range(0,n.get()):
        random_value = random.randint(1,100)
        data.append(random_value)
    drawGraph()
    print(data)
#command functions
def sort(algo=algorithm,spd=speed):
    drawGraph()
    #print("Sort",algo.get()," / Speed",spd.get(),input_count.get())

def resizeCanvas(e):
    global graph_canvas
    print("Resize canvas",e.width,e.height)
    graph_canvas.config(width=e.width,height=e.height)
# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

window.resizable(True,True)


form_frame = tk.Frame(window,height=400,background="Red")
#form_frame.grid(row=0,column=0,sticky="ew")
form_frame.pack(side=tk.TOP,fill=tk.BOTH)
# combobox

#algorithm choice box
algo_label = tk.Label(form_frame,text="Algorithm")
algo_label.grid(row=0,column=0,sticky="w",pady=5)
algo_box = ttk.Combobox(form_frame,textvariable=algorithm,values=algo_list,state="readonly")
algo_box.grid(row=0,column=2,pady=5)
algo_box.current(0)
#speed choice box
speed_label = tk.Label(form_frame,text="Algorithm")
speed_label.grid(row=1,column=0,sticky="w",pady=5)
speed_box = ttk.Combobox(form_frame,textvariable=speed,values=speed_list,state="readonly")
speed_box.grid(row=1,column=2,pady=5)
speed_box.current(0)

#no of input box
ninput_label = tk.Label(form_frame,text="No of inputs")
ninput_label.grid(row=2,column=0,sticky="w",pady=5)
ninput_box = ttk.Spinbox(form_frame,from_=1,to=30,textvariable=input_count)
input_count.set(30)
ninput_box.grid(row=2,column=2,sticky='w',pady=5)

sort_btn = ttk.Button(form_frame,text="Sort",command=sort)
sort_btn.grid(row=3,column=2,sticky="w",pady=5)

generate_btn = ttk.Button(form_frame,text="Generate",command=generateRandom)
generate_btn.grid(row=3,column=1,sticky="w",pady=5)

#graph frame
graph_frame = tk.Frame(window,background="blue",height=500)
#graph_frame.grid(row=1,sticky="ew")
graph_frame.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
graph_label = tk.Label(graph_frame,text="Graph")
graph_label.pack()
#graph canvas
graph_canvas = tk.Canvas(graph_frame,height=450,width=550,bg="white")
graph_canvas.bind('<Configure>',resizeCanvas)
graph_canvas.pack()
# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# run the window
window.mainloop()


