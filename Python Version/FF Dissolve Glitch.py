import tkinter
from tkinter import *
from tkinter import Tk, Button, Label, ttk, messagebox, filedialog
import os
import sys
import webbrowser
import subprocess
def resource_path0(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
global resource
try:
    resource="ffmpeg" #ffmpeg path
    subprocess.Popen(f'"{resource}" -version', shell=True) #check ffmpeg
except:
    messagebox.showerror("No FFMPEG found!","Please download ffmpeg!")
    sys.exit()
def openfile():
    global file
    file=tkinter.filedialog.askopenfilename(filetypes =[('MP4', '*.mp4'),('All Files', '*.*')])
    if(len(file)>=1):
        flabel.config(text=file, fg="#2da86e")
        Vdo['text']='OPEN AGAIN'
        Vdo['bg']='#D0CECE'
    else:
        flabel.config(text="Choose Video", fg="#f86604")
        Vdo['text']='OPEN'
        Vdo['bg']="#82CC6C"
def prestep():
    if Vdo['text']=='OPEN AGAIN':
        pass
    else:
        messagebox.showinfo("","Please input a video file!")
        return
    Disabled()
    outfile=file[:-4]+"_dissolve_glitched_"+str(modebox.get())+"_"+str(mebox.get())+"_"+str(mcbox.get())+"."+exportbox.get()
    if os.path.exists(outfile):
        warn=messagebox.askquestion("Warning","Do you want to replace the old file?")
        if warn=='yes':
            os.remove(outfile)
        elif warn=='no':
            Enabled()
            return
    try:
        Convert(outfile)
        Enabled()
    except:
        Enabled()
        messagebox.showerror("OOPS!","Something went wrong!")
def Convert(outfile):
    Log.place(x=110,y=225)
    Log.config(text="Applying the Glitch...")
    root.update_idletasks()
    fp=int(fpsbox.get())
    mod=(modebox.get()).lower()
    m=(mebox.get()).lower()
    sp=float(spedbox.get())
    mc=(mcbox.get()).lower()
    subprocess.call(f'"{resource}" -i "{file}" -filter:v setpts="{sp}"*PTS,minterpolate="fps="{fp}":mb_size=16:search_param=400:vsbmc=0:scd=none:mc_mode="{mc}":me_mode="{mod}":me="{m}"" "{outfile}"', shell=True)
    Log.place_forget()
    root.update_idletasks()
    messagebox.showinfo("Done!","Your video is baked!")
def Disabled():
    Vdo['state']=DISABLED
    modebox['state']=DISABLED
    exportbox['state']=DISABLED
    fpsbox['state']=DISABLED
    mebox['state']=DISABLED
    spedbox['state']=DISABLED
    mcbox['state']=DISABLED
    btn['state']=DISABLED
def Enabled():
    Log.place_forget()
    root.update_idletasks()
    Vdo['state']=NORMAL
    modebox['state']="readonly"
    exportbox['state']="readonly"
    fpsbox['state']=NORMAL
    mebox['state']="readonly"
    spedbox['state']=NORMAL
    mcbox['state']="readonly"
    btn['state']=NORMAL
def info():
    messagebox.showinfo("Help",
    "This program make some weird but cool dissolving glitch with FFmpeg. \nHow To Use?"
    "\n➤Click the OPEN button and choose your video file"
    "\n➤Then choose the desired modes and parameters"
    "\n➤Then simply click the GLITCH button and wait for the video to get baked"
    "\n➤After baking, you can view the video which will be saved in the same directory"
    "\n\nDeveloper: Akash Bora (a.k.a. Akascape)\nIf you have any issue then contact me on Github."
    "\nVersion-0.1")
def callback(url):
    webbrowser.open_new_tab("https://github.com/Akascape/FF-Dissolve-Glitch")
root= Tk()
root.title("FF Dissolve Glitch")
root.resizable(width=False, height=False)
root.columnconfigure(0,weight=1)
path=resource_path0("Programicon.ico")
root.wm_iconbitmap(path)
root.geometry("400x300")
root.configure(bg='#FFFFFF')
Label(root, text="FF DISSOLVE GLITCH", font=("Impact",17),bd=1, fg="#f86604", bg="#FFFFFF").grid()
flabel=Label(root, text="Choose Video", font=("Calibri",10), fg="#f86604", bg="#FFFFFF")
flabel.grid()
Vdo=Button(root, width=50,bg="#82CC6C",fg="white",highlightthickness=1,borderwidth=0.2,text="OPEN",relief="groove", command=openfile)
Vdo.grid()
Label(root, text="Choose Mode", font=("Calibri",10), bg="#FFFFFF").place(x=42,y=75)
Label(root, text="Choose Type", font=("Calibri",10), bg="#FFFFFF").place(x=165,y=75)
Label(root, text="Slow Speed", font=("Calibri",10), bg="#FFFFFF").place(x=277,y=120)
Label(root, text="Choose FPS", font=("Calibri",10), bg="#FFFFFF").place(x=45,y=120)
Label(root, text="Export Format", font=("Calibri",10), bg="#FFFFFF").place(x=160,y=120)
Label(root, text="MC Mode", font=("Calibri",10), bg="#FFFFFF").place(x=283,y=75)
modes=["BILAT","BIDIR"]
modebox=ttk.Combobox(root,values=modes, font="Verdana 10", width=8, state="readonly")
modebox.current(0)
modebox.place(x=40,y=95)
me=["TSS","ESA","TDLS","NTSS","FSS","DS","HEXBS","EPZS","UMH"]
mebox=ttk.Combobox(root,values=sorted(me), font="Verdana 10", width=8, state="readonly")
mebox.current(7)
mebox.place(x=160,y=95)
speed=["0.5","1","2","10","20","50"]
spedbox=ttk.Combobox(root,values=speed, font="Verdana 10", width=8)
spedbox.current(1)
spedbox.place(x=270,y=140)
fps=["25", "30", "60"]
fpsbox=ttk.Combobox(root,values=fps, font="Verdana 10", width=8)
fpsbox.current(0)
fpsbox.place(x=40,y=140)
export=["mp4","avi","mov","mkv","wmv"]
exportbox=ttk.Combobox(root,values=export, font="Verdana 10", width=8, state="readonly")
exportbox.current(0)
exportbox.place(x=160,y=140)
mc=["AOBMC","OBMC"]
mcbox=ttk.Combobox(root,values=mc, font="Verdana 10", width=8, state="readonly")
mcbox.current(0)
mcbox.place(x=270,y=95)
btn=Button(width=25, height=2,text="GLITCH",font=("Cambria", 10),bg="#f86604",fg="#FFFFFF",borderwidth=0,highlightthickness=2,padx=0,pady=0,command=prestep)
btn.place(x=108,y=180)
Log=Label(root,text="", font=("Calibri",16), bg="#FFFFFF")
infobtn= Button(root, width=2,bg="#FFFFFF",fg="black", text="ⓘ",font=(10),relief="sunken",cursor='hand2', highlightthickness=0,borderwidth=0,padx=0,pady=0,command=info)
infobtn.place(x=377,y=275)
dev=Label(root, text='Developed by Akascape | ',bg='#FFFFFF',fg="#6D76CD", font=("Impact",10))
dev.place(x=5,y=280)
link=Label(root, text="Github Link",font=('Impact',10),bg='#FFFFFF',fg="#6D76CD", cursor="hand2")
link.place(x=140,y=281)
link.bind("<Button-1>", lambda e:
callback("https://github.com/Akascape/FF-Dissolve-Glitch"))
root.mainloop()
#Developer: Akash Bora (a.k.a Akascape)
#version 0.1
