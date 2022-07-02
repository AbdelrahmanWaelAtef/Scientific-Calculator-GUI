# We import the necessary libraries that we will use to do this project:
try:
    from tkinter import *  # This library provides us with functions that creates a GUI
    from math import *  # This library provides us with advanced mathematical for our calculator program
except:     # Checks if tkinter library is downloaded on the user's computer and installs it if not
    import pip
    pip.main(['install', 'tk'])
    import tkinter
# The main code:
cal_int = Tk()  # Create our interface window that will pack everything inside it
cal_int.title("Scientific Calculator")  # Giving our interface a name
cal_int.geometry("800x500")  # Giving the window a width and a height
cal_int.resizable(width=False, height=False)
cal_int.iconbitmap(default='calculator icon.ico')

# Here we create a widget called entry that displays a box where the user can type in or outputs get displayed on:
# Adjusting the width, and adjusting height using the font size function
screen = Entry(cal_int, borderwidth=1.5, font=('Helvetica', 12), bg='black', fg='white')
screen.grid(row=0, column=0, columnspan=7, sticky="nsew", rowspan=2)  # The grid method put our entry in our program

global answer_pushed    # A global variable that will help us later
answer_pushed = False
# Make functions for buttons to work:


# Function that takes in values of the coefficents of a quadratic function and returns the roots:
def quad(A, B, C):
    a = int(A)
    b = int(B)
    c = int(C)
    if a == 0:
        result = "This is not a function"
        return result
    elif (b**2-4*a*c) < 0:
        result = "This function does not have real roots"
        return result
    else:
        root1 = (-b + sqrt(b**2-4*a*c))/(2*a)
        root2 = (-b - sqrt(b**2-4*a*c))/(2*a)
        result = str(root1) + " , " +str(root2)
        return result

# Function for the quad.solver to work:
def button_solvequad(character):
    global answer_pushed
    answer_pushed = False
    perv = screen.get()
    screen.delete(0, END)
    screen.insert(0, "Enter in form of (a,b,c): " + str(character))
    return

# POL function that takes in Fx and Fy and returns the magnitude of resultant and angle:
def pol(x,y):
    r = sqrt(x**2+y**2)
    angle = atan(y/x)
    display = "magnitude: " + str(r)+ " , " + "angle: " + str(angle)
    return display

# Function for the pol function to work:
def button_pol_fun(character):
    global answer_pushed
    global prev
    answer_pushed = False
    perv = screen.get()
    screen.delete(0, END)
    screen.insert(0, "Enter in form of (Fx,Fy): " + str(character))
    return

# Function that displays something when buttons are pressed:
def button_click(character):
    global answer_pushed
    if answer_pushed:
        screen.delete(0, END)
        screen.insert(0, str(character))
        answer_pushed = False
    else:
        on_screen = screen.get()
        screen.delete(0, END)
        screen.insert(0, str(on_screen) + str(character))
    global prev
    prev = screen.get()

# Button equal function to calculate what is written on screen:
def button_eql():           # lines 68 to 73 are tweeks for other functions to work and for python to understand
    global prev
    prev = screen.get()
    while True:
        try:
            on_screen = str(screen.get())
            on_screen = on_screen.replace("Enter in form of (a,b,c): ","")
            on_screen = on_screen.replace("Enter in form of (Fx,Fy): ","")
            on_screen = on_screen.replace("^","**")
            on_screen = on_screen.replace("x","*")
            on_screen = on_screen.replace("÷","/")
            word = [char for char in on_screen]
            for w in range(len(word)):
                if str(word[w]).isalpha():
                    try:
                        if str(word[w-1]).isdigit():
                            word[w-1] = word[w-1] + '*'
                    except:
                        continue
                if str(word[w]) == '(':
                    try:
                        if str(word[w - 1]).isdigit():
                            word[w - 1] = word[w - 1] + '*'
                    except:
                        continue
            on_screen = ''
            for a in word:
                on_screen = on_screen + a
            on_screen = eval(on_screen)
            screen.delete(0, END)
            screen.insert(0,on_screen)

            break
        except:     # Error check
            screen.delete(0, END)
            screen.insert(0, "ERROR PRESS BACK TO RETURN")
            break
    global answer
    answer = on_screen
    global answer_pushed
    answer_pushed = True
    return

# Button exponential function to make powers:
def button_exp():
    on_screen = str(screen.get())
    counter = len(on_screen)-1
    on_screen1 = [char for char in on_screen]
    on_screen2 = ""
    done = False
    while counter != 0:             # While loop that makes some changes for more utility:
        pv = str(on_screen1[counter - 1])               # The purpose is to put the latest value in brackets
        if pv == "x" or pv == "÷" or pv == "+" or pv == "-":
            on_screen1[counter-1] = str(on_screen1[counter-1]) + "("
            for i in on_screen1:
                on_screen2 = on_screen2 + i
            done = True
            break
        elif pv == ")":
            on_screen1[counter-1] = ")x("
            for i in on_screen1:
                on_screen2 = on_screen2 + i
            done = True
            break
        counter = counter - 1
    if not done:
        on_screen2 = "(" + str(screen.get())
    screen.delete(0,END)
    screen.insert(0, str(on_screen2) + ")^(")

# Button delete function to delete the last character entered:
def button_delete():
    global prev
    prev =  screen.get()
    on_screen = screen.get()
    on_screen = len(on_screen)
    screen.delete(on_screen-1)  # Deletes the last index on screen
    return

# Button clear function to clear everything on screen:
def button_clear():
    global prev
    prev = screen.get()
    screen.delete(0, END)
    return

# Button answer function to put the answer of the previous process:
def button_ans():
    on_screen = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(on_screen) + str(answer))

# Button prev function to return to previous state on screen:
def button_prev():
    screen.delete(0, END)
    screen.insert(0, str(prev))

def button_rec():
    on_screen = str(screen.get())
    counter = len(on_screen)-1
    on_screen1 = [char for char in on_screen]
    on_screen2 = ""
    done = False
    while counter != 0:             # While loop that makes some changes for more utility:
        pv = str(on_screen1[counter - 1])               # The purpose is to put the latest value in brackets
        if pv == "x" or pv == "÷" or pv == "+" or pv == "-":
            on_screen1[counter-1] = str(on_screen1[counter-1]) + "("
            for i in on_screen1:
                on_screen2 = on_screen2 + i
            done = True
            break
        elif pv == ")":
            on_screen1[counter-1] = ")x("
            for i in on_screen1:
                on_screen2 = on_screen2 + i
            done = True
            break
        counter = counter - 1
    if not done:
        on_screen2 = "(" + str(screen.get())
    screen.delete(0,END)
    screen.insert(0, str(on_screen2) + ")^(-1)")
# Define buttons and put buttons on screen:

# Row 1:
button_7 = Button(cal_int,  text="7", command=lambda: button_click(7), borderwidth=0.5,bg='#505050',fg='white').grid(row=2, column=0, padx=0, pady=0, sticky = "nsew")
button_8 = Button(cal_int,  text="8", command=lambda: button_click(8), borderwidth=0.5,bg='#505050',fg='white').grid(row=2, column=1, padx=0, pady=0, sticky = "nsew")
button_9 = Button(cal_int,  text="9", command=lambda: button_click(9), borderwidth=0.5,bg='#505050',fg='white').grid(row=2, column=2, padx=0, pady=0, sticky = "nsew")
button_AC = Button(cal_int,  text="AC", command=button_clear, borderwidth=0.5, bg='#D4D4D2',fg='black').grid(row=2, column=3, padx=0, pady=0, sticky = "nsew")
button_DEL = Button(cal_int,  text="DEL", command=button_delete, borderwidth=0.5, bg='#D4D4D2',fg='black').grid(row=2, column=4, padx=0, pady=0, sticky = "nsew")
button_answer = Button(cal_int,  text="Ans", command=button_ans, borderwidth=0.5, bg='#D4D4D2',fg='black').grid(row=2, column=5, padx=0, pady=0, sticky = "nsew")

# Row 2:
button_4 = Button(cal_int,  text="4", command=lambda: button_click(4), borderwidth=0.5,bg='#505050',fg='white').grid(row=3, column=0, padx=0, pady=0, sticky = "nsew")
button_5 = Button(cal_int,  text="5", command=lambda: button_click(5), borderwidth=0.5,bg='#505050',fg='white').grid(row=3, column=1, padx=0, pady=0, sticky = "nsew")
button_6 = Button(cal_int,  text="6", command=lambda: button_click(6), borderwidth=0.5,bg='#505050',fg='white').grid(row=3, column=2, padx=0, pady=0, sticky = "nsew")
button_leftbracket = Button(cal_int,  text="(", command= lambda: button_click("("), borderwidth=0.5, bg='#505050',fg='white').grid(row=3, column=3, padx=0, pady=0, sticky = "nsew")
button_rightbracket = Button(cal_int,  text=")", command= lambda: button_click(")"), borderwidth=0.5, bg='#505050',fg='white').grid(row=3, column=4, padx=0, pady=0, sticky = "nsew")
button_sqr = Button(cal_int,  text="Root", command= lambda: button_click("sqrt("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=3, column=5, padx=0, pady=0, sticky = "nsew")

# Row 3:
button_1 = Button(cal_int,  text="1", command= lambda: button_click(1), borderwidth=0.5,bg='#505050',fg='white').grid(row=4, column=0, padx=0, pady=0, sticky = "nsew")
button_2 = Button(cal_int,  text="2", command=lambda: button_click(2), borderwidth=0.5,bg='#505050',fg='white').grid(row=4, column=1, padx=0, pady=0, sticky = "nsew")
button_3 = Button(cal_int,  text="3", command=lambda: button_click(3), borderwidth=0.5,bg='#505050',fg='white').grid(row=4, column=2, padx=0, pady=0, sticky = "nsew")
button_plus = Button(cal_int,  text="+", command=lambda: button_click("+"), borderwidth=0.5, bg='#FF9500',fg='white').grid(row=4, column=3, padx=0, pady=0, sticky = "nsew")
button_minus = Button(cal_int,  text="-", command=lambda: button_click("-"), borderwidth=0.5, bg='#FF9500',fg='white').grid(row=4, column=4, padx=0, pady=0, sticky = "nsew")
button_previous= Button(cal_int,  text="Prev.", command= button_prev, borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=4, column=5, padx=0, pady=0, sticky = "nsew")

# Row 4:
button_0 = Button(cal_int,  text="0", command=lambda: button_click(0), borderwidth=0.5,bg='#505050',fg='white').grid(row=5, column=0, padx=0, pady=0, sticky = "nsew")
button_dot = Button(cal_int,  text=".", command= lambda: button_click("."), borderwidth=0.5, bg='#505050',fg='white').grid(row=5, column=1, padx=0, pady=0, sticky = "nsew")
button_comma = Button(cal_int,  text=",", command= lambda: button_click(","), borderwidth=0.5, bg='#505050',fg='white').grid(row=5, column=2, padx=0, pady=0, sticky = "nsew")
button_multiply = Button(cal_int,  text="x", command=lambda: button_click("x"), borderwidth=0.5, bg='#FF9500',fg='white').grid(row=5, column=3, padx=0, pady=0, sticky = "nsew")
button_divide = Button(cal_int,  text="÷", command=lambda: button_click("÷"), borderwidth=0.5, bg='#FF9500',fg='white').grid(row=5, column=4, padx=0, pady=0, sticky = "nsew")
button_power = Button(cal_int,  text="Power", command= button_exp, borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=5, column=5, padx=0, pady=0, sticky = "nsew")

# Row 5:
button_sine = Button(cal_int,  text="sin", command= lambda: button_click("sin("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=6, column=0, padx=0, pady=0, sticky = "nsew")
button_cosine = Button(cal_int,  text="cos", command= lambda: button_click("cos("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=6, column=1, padx=0, pady=0, sticky = "nsew")
button_tan = Button(cal_int,  text="tan", command= lambda: button_click("tan("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=6, column=2, padx=0, pady=0, sticky = "nsew")
button_arcsine = Button(cal_int,  text="arcsin", command= lambda: button_click("asin("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=6, column=3, padx=0, pady=0, sticky = "nsew")
button_arccos = Button(cal_int,  text="arccos", command= lambda: button_click("acos("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=6, column=4, padx=0, pady=0, sticky = "nsew")
button_arctan = Button(cal_int,  text="arctan", command= lambda: button_click("atan("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=6, column=5, padx=0, pady=0, sticky = "nsew")

# Row 6:
button_sinh = Button(cal_int,  text="sinh", command= lambda: button_click("sinh("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=7, column=0, padx=0, pady=0, sticky = "nsew")
button_cosh = Button(cal_int,  text="cosh", command= lambda: button_click("cosh("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=7, column=1, padx=0, pady=0, sticky = "nsew")
button_tanh = Button(cal_int,  text="tanh", command= lambda: button_click("tanh("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=7, column=2, padx=0, pady=0, sticky = "nsew")
button_arcsinh = Button(cal_int,  text="arcsinh", command= lambda: button_click("asinh("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=7, column=3, padx=0, pady=0, sticky = "nsew")
button_arccosh = Button(cal_int,  text="arccosh", command= lambda: button_click("acosh("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=7, column=4, padx=0, pady=0, sticky = "nsew")
button_arctanh = Button(cal_int,  text="arctanh", command= lambda: button_click("atanh("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=7, column=5, padx=0, pady=0, sticky = "nsew")

# Row 7:
button_radian = Button(cal_int,  text="RAD", command= lambda: button_click("radians("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=8, column=0, padx=0, pady=0, sticky = "nsew")
button_degree = Button(cal_int,  text="DEG", command= lambda: button_click("degrees("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=8, column=1, padx=0, pady=0, sticky = "nsew")
button_quad = Button(cal_int,  text="solve quad.", command= lambda: button_solvequad("quad("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=8, column=2, padx=0, pady=0, sticky = "nsew")
button_pol = Button(cal_int,  text="pol", command= lambda: button_pol_fun("pol("), borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=8, column=3, padx=0, pady=0, sticky = "nsew")
button_recp = Button(cal_int,  text="(-1)", command= button_rec, borderwidth=0.5, bg='#1C1C1C',fg='white').grid(row=8, column=4, padx=0, pady=0, sticky = "nsew")
button_equal = Button(cal_int,  text="=", command=button_eql, borderwidth=0.5, bg='#FF9500',fg='white').grid(row=8, column=5, padx=0, pady=0, sticky = "nsew")

# Scaling buttons to fit any size of window:
for r in range(1,9):
    Grid.rowconfigure(cal_int, r, weight = 1)
for c in range(6):
    Grid.columnconfigure(cal_int, c, weight = 1)

cal_int.mainloop()  # This creates a loop that keeps our interface running until we exit