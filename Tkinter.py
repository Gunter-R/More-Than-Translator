from tkinter import *
import os


def main():
    def ecs(event):
        root.destroy()
        main()

    def up(event):
        text = maintext.get('1.0', END).upper().strip('\n')
        maintext.delete('1.0', END)
        maintext.insert('1.0', text)

    def down(event):
        text = maintext.get('1.0', END)[:-1].lower()
        maintext.delete('1.0', END)
        maintext.insert('1.0', text)

    def enter1(event):
        maintext.delete('1.0', END)
        maintext.insert('1.0', root.selection_get(selection="CLIPBOARD"))

    def copy(event):
        command = 'echo ' + maintext.get('1.0', END).strip() + '| clip'
        os.system(command)

    def RuEng(event, a):
        a = a.rstrip()
        Rd = dict()
        Ed = dict()
        R1 = 'абвгдеёжзийклмнопрстуфхцшщьъыэюяЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
        E1 = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        R = r'''йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ бю1234567890!-+=*()%,."№;:\/?_'''
        E = r'''qwertyuiop[]asdfghjkl;'zxcvbnm,.`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>~ ,.1234567890!-+=*()%?/@#$^\|&_'''
        for i in range(len(R)):
            Rd[R[i]] = E[i]
            Ed[E[i]] = R[i]
        text2 = ''
        text = maintext.get('1.0', END)[:-1].replace('\n', '')  # ввод

        flag = True
        if a == 'Ru':
            for i in range(len(text)):
                if text[i] in E1:
                    enterlabel = Label(root, text='Wrong language!', font='Fixedsys 20', bg='gainsboro', fg='brown')
                    enterlabel.place(x=207, y=25)
                    flag = False
        if a == 'Eng':
            for i in range(len(text)):
                if text[i] in R1:
                    enterlabel = Label(root, text='Wrong language!', font='Fixedsys 20', bg='gainsboro', fg='brown')
                    enterlabel.place(x=207, y=25)
                    flag = False
        if flag:
            enterlabel = Label(root, text='Enter your text', font='Fixedsys 20', bg='gainsboro', fg='brown')
            enterlabel.place(x=207, y=25)
            if a == 'Ru':
                for i in range(len(text)):
                    text2 += Rd[text[i]]
            elif a == 'Eng':
                for i in range(len(text)):
                    text2 += Ed[text[i]]
            maintext.delete('1.0', END)
            maintext.insert('1.0', text2)

    root = Tk()
    root.title('Сorrect your text')
    root.geometry('800x500+400+200')
    root.configure(background='gainsboro')

    escbutt = Button(root, text='Rest', width=4, heigh=1, font='Fixedsys 11', bg='brown', fg='white')
    escbutt.place(x=10, y=10)
    escbutt.bind('<Button-1>', ecs)

    enterlabel = Label(root, text='Enter your text', font='Fixedsys 20', bg='gainsboro', fg='brown')
    enterlabel.place(x=207, y=25)

    label2 = Label(root, text='''*Press Ctrl+V to enter copied text
*Press Ctrl+C to copy text''', font='Fixedsys 14', bg='gainsboro', justify=LEFT)
    label2.place(x=80, y=420)

    buttRuEng = Button(root, text='Ru->Eng', font='Fixedsys 25', fg='gainsboro', width=8, heigh=1, bg='brown')
    buttRuEng.bind("<Button-1>", lambda event, f='Ru': RuEng(event, f))
    buttRuEng.place(x=600, y=60)

    buttEngRu = Button(root, text='Eng->Ru', font='Fixedsys 25', fg='gainsboro', width=8, heigh=1, bg='brown')
    buttEngRu.bind("<Button-1>", lambda event, f='Eng': RuEng(event, f))
    buttEngRu.place(x=600, y=160)

    buttCaps = Button(root, text='CapsLock', font='Fixedsys 25', fg='gainsboro', width=8, heigh=1, bg='brown')
    buttCaps.bind("<Button-1>", up)
    buttCaps.place(x=600, y=260)

    buttACaps = Button(root, text='AntiCaps', font='Fixedsys 25', fg='gainsboro', width=8, heigh=1, bg='brown')
    buttACaps.bind("<Button-1>", down)
    buttACaps.place(x=600, y=360)

    maintext = Text(root, height=17, width=50, font='Fixedsys 14', wrap=WORD)
    maintext.place(x=80, y=70)

    root.bind('<Control-c>', copy)
    root.bind('<Control-v>', enter1)
    root.mainloop()


main()
