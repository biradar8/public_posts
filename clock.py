from ttkbootstrap import Window, Label
from datetime import datetime

time = lambda:datetime.now().strftime('Time : %I:%M:%S %p')
date = lambda:datetime.today().strftime('Date : %d-%b-%Y')
def update_time():
    time_label.configure(text=f'{time()}\n{date()}')
    root.after(100, update_time)

if __name__ == '__main__':
    root = Window(title='Clock', themename='vapor', size=(275, 80), resizable=(False, False))
    time_label = Label(root, text='', font=('calibri', 20, 'bold'))
    time_label.grid(column=0, row=0)
    update_time()
    root.mainloop()
