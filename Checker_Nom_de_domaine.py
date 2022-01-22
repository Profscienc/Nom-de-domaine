from tkinter import *
from tkinter import messagebox
import whois 
import sys
root = Tk()
root.title("Profscience Checkeur")
root.geometry("470x180")
root.resizable(False, False)
label = Label(root, text="Entrer un nom de domaine:", font=("ariel 15 bold"))
label.grid(row=0, column=0, padx=12, pady=30)
name = StringVar()
domain_name = Entry(root, textvariable=name, font=("ariel 15 bold"), relief=GROOVE, bd=2)
domain_name.grid(row=0, column=1, padx=5, pady=30)
domain_name.focus()
def check():
    if name.get() != '':
        try: 
            domain = whois.whois(name.get()) 
            if domain.domain_name == None: 
                sys.exit(1) 
              
        except :
            messagebox.showinfo("Checkeur de Nom de Domaine",
                                "Ce nom de domaine est disponible à l'achat")
        else:
            messagebox.showinfo("Checkeur de Nom de Domaine",
                                "Désolé, ce nom de domaine n'est pas disponible")
    else:
        messagebox.showerror("Checkeur de Nom de Domaine",
                             "Veuillez entrer un nom de domaine et checker encore")
    
check_button = Button(root, text="Check", width=10, bg='black', fg='gold', font=("ariel 15 bold"), relief=GROOVE, command=check)
check_button.place(x=175, y=100)
root.mainloop()
