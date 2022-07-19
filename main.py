import tkinter as tk
from tkinter import BOTH, ttk
from turtle import bgcolor

algo_list = ["Bubble Sort","Insertion Sort","Selection Sort"]
speed_list = ["Slow","Medium","Fast"]

window_width = 900
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
    frm_w=form_frame.winfo_width()
    frm_h=form_frame.winfo_height()
    column_w=frm_w/input_count.get()
    print("Frame width:height",frm_w,frm_h,column_w)

#command functions
def sort(algo=algorithm,spd=speed):
    drawGraph()
    print("Sort",algo.get()," / Speed",spd.get(),input_count.get())
# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

window.resizable(True,True)


form_frame = tk.Frame(window,width=700,background="Red")
form_frame.grid(row=0,column=0,sticky="ew")
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


#graph frame
graph_frame = tk.Frame(window,background="blue")
graph_frame.grid(row=1,sticky="ew")
graph_label = tk.Label(graph_frame,text="Graph")
graph_label.pack()
# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# run the window
window.mainloop()


