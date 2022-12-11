import customtkinter
import tkinter
from typing import Union, Callable

class CTkSpinbox(customtkinter.CTkFrame):
         
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: int = 1,
                 min_value: int = 0,
                 max_value: int = 1000,
                 command: Callable = None,
                 **kwargs):
        
        super().__init__(*args, width=width, height=height, **kwargs)
        
        self.step_size = step_size
        self.max_value = max_value
        self.min_value = min_value
        self.command = command
        self.validation = self.register(self.only_numbers)
        
        self.grid_columnconfigure((0, 2), weight=0) 
        self.grid_columnconfigure(1, weight=1)

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)
    
        self.text = tkinter.StringVar()
        self.text.set(self.min_value)

        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, textvariable=self.text,
                                            placeholder_text=str(self.min_value), justify="right", validate='key',
                                            validatecommand=(self.validation, '%P'))       
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = customtkinter.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

    def add_button_callback(self):
        if self.entry.get()=="":
            self.text.set(0)
        try:
            if int(self.entry.get())<self.max_value:
                self.text.set(int(self.entry.get()) + self.step_size)
        except ValueError:
            return
        if self.command is not None:
            self.command()
            
    def configure(self, state):
        if state=="disabled":
            self.entry.configure(state="disabled")
            self.add_button.configure(state="disabled")
            self.subtract_button.configure(state="disabled")
        else:
            self.entry.configure(state="normal")
            self.add_button.configure(state="normal")
            self.subtract_button.configure(state="normal")
            
    def subtract_button_callback(self):
        if self.entry.get()=="":
            self.text.set(0)
        try:
            if int(self.entry.get())<self.max_value+1 and int(self.entry.get())>self.min_value:
                self.text.set(int(self.entry.get()) - self.step_size)
        except ValueError:
            return
        if self.command is not None:
            self.command()
        
    def only_numbers(self, char):
        if (char.isdigit() or (char=="")) and (len(char)<=len(str(self.max_value))):
            return True
        else:
            return False
        
    def get(self) -> Union[int, None]:
        if self.entry.get()=="":
            return 0
        try:
            return int(self.text.get())
        except ValueError:
            return None

    def set(self, value: int):
        if str(value).isdigit():
            self.text.set(int(value))
