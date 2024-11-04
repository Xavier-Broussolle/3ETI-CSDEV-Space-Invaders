import tkinter as tk

SI = tk.Tk()
SI.title("Space Invaders")
SI.geometry('1190x780')
Titre = tk.Label(SI, text="Space Invaders", fg = 'black')
Titre.pack(pady= 10)
button_options = tk.Button(SI, text ="Options", fg='black')
button_options.pack(pady =100)
buttonquit = tk.Button(SI, text="Quitter", fg='red', command=SI.destroy)
buttonquit.pack(pady=50)
SI.mainloop()

