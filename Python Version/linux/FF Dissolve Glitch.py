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
font_name="cambria" #change the font if you are facing some UI issues
resource="ffmpeg"
subprocess.call(f'"{resource}" -version', shell=True) #check ffmpeg
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
    Log.place(x=150,y=225)
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
    modebox['state']=NORMAL
    exportbox['state']=NORMAL
    fpsbox['state']=NORMAL
    mebox['state']=NORMAL
    spedbox['state']=NORMAL
    mcbox['state']=NORMAL
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
try:
	icopath=PhotoImage(file=resource_path0("Programicon.png"))
	root.iconphoto(False, icopath)
except:
	pass
root.geometry("400x300")
root.configure(bg='#FFFFFF')
Label(root, text="FF DISSOLVE GLITCH", font=(font_name,17),bd=1, fg="#f86604", bg="#FFFFFF").grid()
flabel=Label(root, text="Choose Video", font=(font_name,8), fg="#f86604", bg="#FFFFFF")
flabel.grid()
Vdo=Button(root, width=42,bg="#82CC6C",fg="white",highlightthickness=1,borderwidth=0.2,text="OPEN",relief="groove", command=openfile)
Vdo.grid()
Label(root, text="Choose Mode", font=(font_name,9), bg="#FFFFFF").place(x=40,y=85)
Label(root, text="Choose Type", font=(font_name,9), bg="#FFFFFF").place(x=160,y=85)
Label(root, text="Slow Speed", font=(font_name,9), bg="#FFFFFF").place(x=275,y=130)
Label(root, text="Choose FPS", font=(font_name,9), bg="#FFFFFF").place(x=45,y=130)
Label(root, text="Export Format", font=(font_name,9), bg="#FFFFFF").place(x=155,y=130)
Label(root, text="MC Mode", font=(font_name,9), bg="#FFFFFF").place(x=280,y=85)
modes=["BILAT","BIDIR"]
modebox=ttk.Combobox(root,values=modes, font=(font_name,10) , width=8, state="readonly")
modebox.current(0)
modebox.place(x=40,y=105)
me=["TSS","ESA","TDLS","NTSS","FSS","DS","HEXBS","EPZS","UMH"]
mebox=ttk.Combobox(root,values=sorted(me), font=(font_name,10) , width=8, state="readonly")
mebox.current(7)
mebox.place(x=160,y=105)
speed=["0.5","1","2","10","20","50"]
spedbox=ttk.Combobox(root,values=speed, font=(font_name,10) , width=8)
spedbox.current(1)
spedbox.place(x=270,y=150)
fps=["25", "30", "60"]
fpsbox=ttk.Combobox(root,values=fps, font=(font_name,10) , width=8)
fpsbox.current(0)
fpsbox.place(x=40,y=150)
export=["mp4","avi","mov","mkv","wmv"]
exportbox=ttk.Combobox(root,values=export, font=(font_name,10) , width=8, state="readonly")
exportbox.current(0)
exportbox.place(x=160,y=150)
mc=["AOBMC","OBMC"]
mcbox=ttk.Combobox(root,values=mc, font=(font_name,10) , width=8, state="readonly")
mcbox.current(0)
mcbox.place(x=270,y=105)
btn=Button(width=25, height=2,text="GLITCH",font=(font_name,10) ,bg="#f86604",fg="#FFFFFF",borderwidth=0,highlightthickness=2,padx=0,pady=0,command=prestep)
btn.place(x=108,y=180)
Log=Label(root,text="", font=(font_name,10) , bg="#FFFFFF")
infobtn= Button(root, width=2,bg="#FFFFFF",fg="black", text="ⓘ",relief="sunken",cursor='hand2', highlightthickness=0,borderwidth=0,padx=0,pady=0,command=info)
infobtn.place(x=377,y=275)
dev=Label(root, text='Developed by Akascape | ',bg='#FFFFFF',fg="#6D76CD", font=(font_name,10) )
dev.place(x=5,y=280)
link=Label(root, text="Github Link",font=(font_name,10) ,bg='#FFFFFF',fg="#6D76CD", cursor="hand2")
link.place(x=175,y=280)
link.bind("<Button-1>", lambda e:
callback("https://github.com/Akascape/FF-Dissolve-Glitch"))
root.mainloop()
#Developer: Akash Bora (a.k.a Akascape)
#version 0.1
