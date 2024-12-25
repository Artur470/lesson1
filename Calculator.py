import tkinter as tk

operation = ""


def equal():
    global operation
    try:
        result = str(eval(operation))
        enter_d.set(result)
        operation = result
    except Exception:
        enter_d.set("Ошибка")
        operation = ""


def chickbtn(number):
    global operation
    operation += str(number)
    enter_d.set(operation)


def clear():
    global operation
    operation = ""
    enter_d.set("")


root = tk.Tk()
root.geometry("300x300")
root.title("Калькулятор")

enter_d = tk.StringVar()
enter = tk.Entry(root, width=20, font=40, textvariable=enter_d)


btn1 = tk.Button(root, width=5, height=2, text="1", command=lambda: chickbtn(1))
btn2 = tk.Button(root, width=5, height=2, text="2", command=lambda: chickbtn(2))
btn3 = tk.Button(root, width=5, height=2, text="3", command=lambda: chickbtn(3))
btn4 = tk.Button(root, width=5, height=2, text="4", command=lambda: chickbtn(4))
btn5 = tk.Button(root, width=5, height=2, text="5", command=lambda: chickbtn(5))
btn6 = tk.Button(root, width=5, height=2, text="6", command=lambda: chickbtn(6))
btn7 = tk.Button(root, width=5, height=2, text="7", command=lambda: chickbtn(7))
btn8 = tk.Button(root, width=5, height=2, text="8", command=lambda: chickbtn(8))
btn9 = tk.Button(root, width=5, height=2, text="9", command=lambda: chickbtn(9))
btn0 = tk.Button(root, width=5, height=2, text="0", command=lambda: chickbtn(0))


btnc = tk.Button(root, width=5, height=2, text="C", command=clear)
btnplus = tk.Button(root, width=5, height=2, text="+", command=lambda: chickbtn("+"))
btnmin = tk.Button(root, width=5, height=2, text="-", command=lambda: chickbtn("-"))
btnumn = tk.Button(root, width=5, height=2, text="*", command=lambda: chickbtn("*"))
btndel = tk.Button(root, width=5, height=2, text="/", command=lambda: chickbtn("/"))
btnequel = tk.Button(root, width=5, height=2, text="=", command=equal)


enter.place(x=20, y=10)
btn1.place(x=10, y=50)
btn2.place(x=65, y=50)
btn3.place(x=125, y=50)
btn4.place(x=180, y=50)
btn5.place(x=10, y=110)
btn6.place(x=65, y=110)
btn7.place(x=125, y=110)
btn8.place(x=180, y=110)
btn9.place(x=10, y=175)
btn0.place(x=65, y=175)

btnc.place(x=125, y=175)
btnplus.place(x=245, y=50)
btnmin.place(x=245, y=110)
btnumn.place(x=245, y=175)
btndel.place(x=245, y=230)
btnequel.place(x=180, y=175)

root.mainloop()
