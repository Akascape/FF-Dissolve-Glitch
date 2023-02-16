"""
MIT License

Copyright (c) 2023 Akash Bora

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import tkinter
import customtkinter
from tkdial import Meter
from PIL import Image, ImageTk
import os
import subprocess
from Assets.spinbox import CTkSpinbox
import threading
import random

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme(random.choice(['blue','green','dark-blue']))

if customtkinter.get_appearance_mode()=="Dark":
    o = 1
else:
    o = 0
    
def set_fps(value):
    label_4.configure(text="FPS: "+str(int(value)))

def set_speed(value):
    label_5.configure(text="Speed: "+str(round(value,1))+"x Slower")

def set_preset():
    global preset
    if meter.get()<20:
        meter.configure(text="Slow")
        preset = "slow"
    elif meter.get()<40:
        meter.configure(text="Medium")
        preset = "medium"
    elif meter.get()<60:
        meter.configure(text="Fast")
        preset = "fast"
    elif meter.get()<80:
        meter.configure(text="Faster")
        preset = "faster"
    elif meter.get()<90:
        meter.configure(text="Superfast")
        preset = "superfast"
    elif meter.get()<=100:
        meter.configure(text="Ultrafast")
        preset = "ultrafast"
       
def open_video():
    global file
    file = tkinter.filedialog.askopenfilename(filetypes=[('Video', ['*.mp4','*.avi','*.mov','*.mkv']),('All Files', '*.*')])
    if file:
        open_button.configure(fg_color=customtkinter.ThemeManager.theme["CTkButton"]["hover_color"][o], text=file)
        outpng = os.path.join(DIRPATH,"Assets","thumbnail_cache","vid_thumbnail.jpg")
        if os.path.exists(os.path.join(DIRPATH,"Assets","thumbnail_cache","vid_thumbnail.jpg")):
                os.remove(os.path.join(DIRPATH,"Assets","thumbnail_cache","vid_thumbnail.jpg"))
        subprocess.call(f'ffmpeg -loglevel quiet -ss 00:00:01 -t 00:00:01 -i "{file}" -qscale:v 2 -r 10.0 "{outpng}"', shell=True)
        if os.path.exists(os.path.join(DIRPATH,"Assets","thumbnail_cache","vid_thumbnail.jpg")):
            vid_image2 = customtkinter.CTkImage(Image.open(outpng), size=(300,150))
            video_frame.configure(image=vid_image2, text="")
    else:
        open_button.configure(fg_color=customtkinter.ThemeManager.theme["CTkButton"]["fg_color"][o], text="OPEN VIDEO")
        video_frame.configure(image=icon, text="FF-DISSOLVE GLITCH")

def conversion():
    if file=="":
        return
    outfile = tkinter.filedialog.asksaveasfilename(initialfile="Untitled.mp4", filetypes=[('Video', ['*.mp4','*.avi','*.mov','*.mkv']),('All Files', '*.*')])
    if not outfile:
        return
    
    fp = str(int(fps_slider.get()))
    mod = str((mode_box.get()).lower())
    m = str((type_box.get()).lower())
    sp = str(round(speed_slider.get(),1))
    mc = str((mc_box.get()).lower())
    export_button.configure(state="disabled")
    cmd = f'ffmpeg -i "{file}" -c:v libx264 -preset "{preset}" -s "{reso_box_x.get()}x{reso_box_y.get()}" -filter:v setpts="{sp}"*PTS,minterpolate="fps="{fp}":mb_size=16:search_param=400:vsbmc=0:scd=none:mc_mode="{mc}":me_mode="{mod}":me="{m}"" "{outfile}"'
    subprocess.call(cmd, shell=False)

    if os.path.exists(outfile):
        tkinter.messagebox.showinfo("DONE","Exported the file: "+outfile)
    else:
        tkinter.messagebox.showinfo("ERROR","Something went wrong!")
    export_button.configure(state="normal")

def info():
    tkinter.messagebox.showinfo("About",
    "This program make some weird but cool dissolving glitch with FFmpeg. \nHow To Use?"
    "\n➤ Click the OPEN button and choose your video file"
    "\n➤ Then choose the desired modes and parameters"
    "\n➤ Then simply click the Export button and wait for the video to get baked"
    "\n➤ After baking, you can view the video and see the results"
    "\nNote: You can press 'q' on your keyboard to end any ffmpeg process safely"
    "\n\nDeveloper: Akash Bora (a.k.a. Akascape)\nIf you have any issue then contact me on Github."
    "\nVersion-0.4")
    
HEIGHT = 800
WIDTH = 500
DIRPATH = os.path.dirname(os.path.realpath(__file__))

if not os.path.exists(os.path.join(DIRPATH,"Assets","thumbnail_cache")):
    os.mkdir(os.path.join(DIRPATH,"Assets","thumbnail_cache"))
               
app = customtkinter.CTk()
app.title("FF Dissolve Glitch")
app.geometry((f"{WIDTH}x{HEIGHT}"))
app.minsize(450,600)
app.bind("<1>", lambda event: event.widget.focus_set())

try:
    app.wm_iconbitmap()
    icopath = ImageTk.PhotoImage(Image.open(os.path.join(DIRPATH,"Assets","Programicon.png")))
    app.iconphoto(False, icopath)
except:
    pass

file = ""
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.grid(padx=20, pady=20, sticky="nswe")

frame_1.grid_columnconfigure(0, weight=1)
frame_1.grid_rowconfigure(0, weight=1)

icon = customtkinter.CTkImage(Image.open(os.path.join(DIRPATH,"Assets","Programicon.png")), size=(150,150))

video_frame = customtkinter.CTkLabel(master=frame_1, image=icon, height=200, font=customtkinter.CTkFont("",30),text="FF-DISSOLVE GLITCH",
                                     fg_color=customtkinter.ThemeManager.theme["CTkFrame"]["top_fg_color"][o])
video_frame.grid(row=0, rowspan=2, sticky="nswe", padx=10, pady=10)

open_button = customtkinter.CTkButton(master=frame_1, text="OPEN VIDEO", height=40, command=open_video)
open_button.grid(padx=10, sticky="we")

label_1 = customtkinter.CTkLabel(master=frame_1, text="Motion Estimation Mode:")
label_1.grid(pady=(10,0))

mode_values = ['BILAT','BIDIR']
mode_box = customtkinter.CTkOptionMenu(master=frame_1, height=40, values=mode_values)
mode_box.grid(padx=10, sticky="we")

label_2 = customtkinter.CTkLabel(master=frame_1, text="Algorithm Type:")
label_2.grid(pady=0)

type_values = ["TSS","ESA","TDLS","NTSS","FSS","DS","HEXBS","EPZS","UMH"]
type_box = customtkinter.CTkOptionMenu(master=frame_1, height=40, values=type_values)
type_box.grid(padx=10, sticky="we", pady=0)

label_3 = customtkinter.CTkLabel(master=frame_1, text="Motion Compression:")
label_3.grid()

mc_values = ["AOBMC","OBMC"]
mc_box = customtkinter.CTkOptionMenu(master=frame_1, height=40, values=mc_values)
mc_box.grid(padx=10, sticky="we", pady=0)

label_4 = customtkinter.CTkLabel(master=frame_1, text="FPS: 30")
label_4.grid(pady=0)

fps_slider = customtkinter.CTkSlider(master=frame_1, from_=20, to=60, command=set_fps)
fps_slider.set(30)
fps_slider.grid(sticky="we", pady=0, padx=10)

label_5 = customtkinter.CTkLabel(master=frame_1, text="Speed: 1x Slower")
label_5.grid(row=11, pady=0)

speed_slider = customtkinter.CTkSlider(master=frame_1, from_=0.1, to=50, command=set_speed)
speed_slider.set(1)
speed_slider.grid(sticky="nwe", pady=0, padx=10)

label_6 = customtkinter.CTkLabel(master=frame_1, text="Resolution")
label_6.grid(pady=12)

reso_box_x = CTkSpinbox(master=frame_1, max_value=5000, min_value=240, width=150)
reso_box_x.grid(row=13, sticky="w", padx=10)
reso_box_x.set(1280)

reso_box_y = CTkSpinbox(master=frame_1, max_value=5000, min_value=240, width=150)
reso_box_y.grid(row=13, sticky="e", padx=10)
reso_box_y.set(720)

export_button = customtkinter.CTkButton(master=frame_1, height=40, text="EXPORT", command=lambda: threading.Thread(target=conversion).start())
export_button.grid(row=15, sticky="we", pady=(0,0), padx=(200,20))

export_values = ["mp4","avi","mov","mkv","wmv"]
export_box = customtkinter.CTkOptionMenu(master=frame_1, height=40, width=100, values=export_values)
export_box.grid(row=14, sticky="we", pady=(0,10), padx=(200,20))

preset = "medium"

meter = Meter(frame_1, bg=customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][o], radius=150, start=0, end=100, border_width=5,
               fg="black", text_color="white", start_angle=270, end_angle=-360, text="", scale_color="black", axis_color="white",
               needle_color="white", command=set_preset, scroll_steps=0.5)
meter.set_mark(80, 100, "green")
meter.set_mark(50, 80, "#92d050")
meter.set_mark(20, 50, "yellow")
meter.set_mark(0, 20, "orange")
meter.set(40)
meter.configure(text="Medium")

label_7 = customtkinter.CTkLabel(master=frame_1, text="Export Format")
label_7.grid(row=14, pady=(80,0), padx=(200,0), sticky="w")

meter.grid(row=14, rowspan=2, sticky="w", padx=10, pady=5)

i_button = customtkinter.CTkButton(master=frame_1, text="i", fg_color=customtkinter.ThemeManager.theme["CTkFrame"]["top_fg_color"][o],
                                   corner_radius=0, width=20, command=info)
i_button.grid(row=0, sticky="ne", padx=10, pady=10)

app.mainloop()                   
