from pickle import TRUE
import tkinter as tk
from tkinter import BOTH, ttk
from turtle import bgcolor
import random

from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.selection_sort import selection_sort

algo_list = ["Bubble Sort","Insertion Sort","Selection Sort","Merge Sort"]
speed_list = ["Slow","Medium","Fast"]

window_width = 700
window_height = 900
window_x = 50
window_y = 50
window = tk.Tk()
window.title("Algorithm Visualizer")


algorithm = tk.StringVar()
speed = tk.StringVar()
input_count =tk.IntVar()
step_count = tk.IntVar()
data=[0]* input_count.get()


#main functions
def drawGraph(data,colors):
    global graph_canvas
    graph_canvas.delete("all")
    no_of_inputs= input_count.get()
    c_height=graph_canvas.winfo_height()
    c_width =graph_canvas.winfo_width()
    column_width = c_width/no_of_inputs
    one_unit_height = c_height/max(data)
    for i,v in enumerate(data):
        x1=column_width*i
        x2=x1+column_width
        y1=c_height
        y2=one_unit_height*(max(data)-v)

        graph_canvas.create_rectangle(x1,y1,x2,y2,fill=colors[i],outline="yellow")
        textX = x2-(column_width/2)
        textY=y2-10
        graph_canvas.create_text(textX,y1-12,text=str(data[i]),fill="blue",font=("Roboto 8 bold"))
    window.update_idletasks()


def generateRandom(n=input_count):
    global data
    step_count.set(0)
    data=[]
    for i in range(0,n.get()):
        random_value = random.randint(1,100)
        data.append(random_value)
    #test data
    data=[1,2,3,4,5,10,9,8,7,6,5]
    drawGraph(data,["black" for x in range(len(data))])
def increase_step():
    step_count.set(step_count.get()+1)
#command functions
def sort(algo=algorithm,spd=speed):
    speedDict = {"Slow":1.3,"Medium":0.8,"Fast":0.08}
    algoDict = {
                "Bubble Sort":bubble_sort,
                "Selection Sort":selection_sort,
                "Insertion Sort":insertion_sort,
                "Merge Sort":merge_sort,
                }
    sort_fn = algoDict[algorithm.get()]
    if(algorithm.get() == "Merge Sort") :
        merge_result = sort_fn(data,0,len(data)-1,speedDict[spd.get()],drawGraph)
        print("Merge Result",merge_result)
    else :
        sort_fn(data,speedDict[spd.get()],drawGraph,increase_step)
    #print("Sort",algo.get()," / Speed",spd.get(),input_count.get())

def resizeCanvas(e):
    global graph_canvas
    g_width = graph_canvas.winfo_width()
    g_height = graph_canvas.winfo_height()
    print("Resize canvas",window.winfo_width(),g_width,g_height)
    if(e.type != 22 and g_width == window.winfo_width() and len(data)>0):
        drawGraph()
    graph_canvas.config(width=window.winfo_width(),height=e.height)

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

step_label = tk.Label(form_frame,text="Steps")
step_label.grid(row=4,column=0,sticky="w",pady=5)
step_value = tk.Label(form_frame,textvariable=step_count)
step_value.grid(row=4,column=2,sticky="w",pady=5)

algo_box = ttk.Combobox(form_frame,textvariable=algorithm,values=algo_list,state="readonly")
algo_box.grid(row=0,column=2,pady=5)
algo_box.current(0)
#speed choice box
speed_label = tk.Label(form_frame,text="Speed")
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
graph_frame = tk.Frame(window,background="gray",height=500)
#graph_frame.grid(row=1,sticky="ew")
graph_frame.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)

#graph canvas
graph_canvas = tk.Canvas(graph_frame,height=450,width=550,bg="white")
graph_canvas.bind('<Configure>',resizeCanvas)
graph_canvas.pack()
# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# run the window
window.mainloop()


