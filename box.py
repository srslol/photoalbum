import tkinter as tk

window = tk.Tk()

output = tk.Text(bg='green')

output.grid(row=1, column=0, sticky="nsew")

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure((0,1), weight=1, uniform=1)

window.mainloop()