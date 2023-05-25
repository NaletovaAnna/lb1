from tkinter import *
import requests
import messagebox

def z1():
    root = Tk()

    def btn_click():
        pass1 = loginInput.get()
        password = passField.get()
        info_str = f'данные: {str(pass1)}, {str(password)}'
        messagebox.showinfo(title='Название', message=info_str)
        if password in pass1:
            otvet_str = 'Пароль верный'
            messagebox.showinfo(title='Название', message=otvet_str)
        else:
            messagebox.showerror(title='', message='Error always!')

    root['bg'] = '#fafafa'
    root.title('Время мира')
    root.wm_attributes('-alpha', 0.7)
    root.geometry('300x250')

    canvas = Canvas(root, height=300, width=250)
    canvas.pack()

    frame = Frame(root, bg='pink')
    frame.place(relheight=1, relwidth=1)

    title = Label(frame, text='проверка пароля', bg='pink', font=40)
    title.pack()
    btn = Button(frame, text='next', bg='red', command=btn_click)
    btn.pack()

    loginInput = Entry(frame, bg='white',)
    loginInput.pack()

    passField = Entry(frame, bg='white', show='*')
    passField.pack()

    root.mainloop()

def z2():
    root = Tk()

    root['bg'] = '#fafafa'
    root.title('Время мира')
    root.wm_attributes('-alpha', 0.7)
    root.geometry('300x250')

    canvas = Canvas(root, height=300, width=250)
    canvas.pack()

z2()