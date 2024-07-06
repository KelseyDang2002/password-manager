import tkinter as tk

window = tk.Tk()

window.geometry("500x500")
window.title("Password Manager")

label = tk.Label(window, text="Menu", font=('Arial', 18))
label.pack()

textbox = tk.Text(window, height=3, font=('Arial', 18))
textbox.pack(padx=10, pady=10)

buttonframe = tk.Frame()
buttonframe.columnconfigure(0, width=1)
buttonframe.columnconfigure(1, width=1)
buttonframe.columnconfigure(2, width=1)

btn1 = tk.Button(buttonframe, text="Submit", font=('Arial', 18))

window.mainloop()