######################################################        IMPORTS          ========================================================================================================================================================================================================================================

import PySimpleGUI as ui
import math as m
import cmath as cm
import numpy as np  
import matplotlib.pyplot as plt  



#########################################################    DEFINATIONS     ====================================================================================================================================================================================================================================

def arith_calc(operand,operator,operand2):
    if operator == '+':
        operand += operand2
    elif operator == '-':
        operand -= operand2
    elif operator == 'x' or operator == '*':
        operand *= operand2
    elif operator == symbol['divide'] or operator == '/':
        operand /= operand2 
    elif operator == symbol['power'] or operator == '^':
        operand = operand**operand2
    elif operator == symbol['radical']:
        operand = operand**(1.0/operand2)
    
    return operand

def get_factors(number):
    facts = []
    for i in range(1,number+1):
        if number % i ==0:
            facts.append(i)
    return facts

def lowestterm(nume, den):
    hcf = m.gcd(nume, den)
    nume /= hcf
    den /= hcf
    if nume > den:
        len = m.ceil(m.log10(nume))
    else:
        len = m.ceil(m.log10(den))
    if len<=3:
        len = 3
    dec = float(nume)/den
    return nume, den, len, dec

def quadSolver(a,b,c):

    if a==b==0:
        if c!=0:
            message = 'Not a valid equation'
        else:
            message = ' 0=0 is not an interesting equation'

    if a==0:
        root1 = root2 = float(-c)/b
        message = 'Linear Equation'

    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + m.sqrt(discriminant))/ (2 * a)
        root2 = (-b - m.sqrt(discriminant))/ (2 * a)
        message = 'Two distinct real roots'
        
    elif discriminant == 0:
        root1 = root2 = float(-b + m.sqrt(discriminant))/ (2 * a)
        message = 'Equal roots'
        
    elif discriminant < 0:
        root1 = (-b + cm.sqrt(discriminant))/ (2 * a)
        root2 = (-b - cm.sqrt(discriminant))/ (2 * a)
        message = 'Two distinct complex roots'

    return str(root1), str(root2), message

def graph_func(function, range1, range2):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', 0.0))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    x = np.arange(float(range1), float(range2) , 0.1)  

    y = eval(function)

    plt.plot(x, y)  
    plt.show()
        

symbol = {
    'divide': chr(247),             # UNICODE EXPLAINATION
    'radical': u"n\u221ax",         # Check "/home/Pictures/unicode_chars.png" for table
    'power': u"x\u207F",
    'squared': u"\u00B2"            # Replace x with Hexadecimal digit
}                                   # String is: u"\u<unicode>"

############################################################     GUI  ===========================================================================================================================================================================================================================


# win ==> Main window
# win1 ==> Aritmetic Calculator Window
#
# layout ==> Main window Layout
# layout1 ==> Arithmetic Calcultor Layout


layout = [
    [ui.Text("Welcome to Calculator", font = 'Timesnewroman', justification = 'centre')],
    [ui.Text("Choose your Mode", font = 'Timesnewroman', justification = 'centre')],
    [ui.Text("1.", font = 'Timesnewroman'), ui.Button('Arithmetic Calculator', size=(50,1))],
    [ui.Text("2.", font = 'Timesnewroman'), ui.Button('Factors Calculator', size=(50,1))],
    [ui.Text("3.", font = 'Timesnewroman'), ui.Button('Lowest Term Calculator', size=(50,1))],
    [ui.Text("4.", font = 'Timesnewroman'), ui.Button('Quadratic Equation Solver', size=(50,1))],
    [ui.Text("5.", font = 'Timesnewroman'), ui.Button('Function Grapher', size=(50,1))],   
]

win = ui.Window("Calculator", layout = layout)

win1_active = False
win2_active = False
win3_active = False
win4_active = False

while True:                             
    event, values = win.read(timeout = 10000)  
          
    if event in (None, 'Exit'):
        win.close()     
        break

    if event == 'Arithmetic Calculator':
        win1_active = True
        win.Hide()

        display_nos = ''
        operands = []
        operators = []
        result = 0.0
        clearlist = True
        initval_entered = False

        layout1 = [
            [ui.Input(font='Helvetica 28', size=(15,1), key = 'box')],
            [ui.Text(key = '-keys1-', visible = False)],
            [ui.Button('1', size = (2,1), font='Ariel 30'), ui.Button('2', size = (2,1), font='Ariel 30'), ui.Button('3', size = (2,1), font='Ariel 30'), ui.Button('+', size = (2,1), font='Ariel 30')],
            [ui.Button('4', size = (2,1), font='Ariel 30'), ui.Button('5', size = (2,1), font='Ariel 30'), ui.Button('6', size = (2,1), font='Ariel 30'), ui.Button('-', size = (2,1), font='Ariel 30')],
            [ui.Button('7', size = (2,1), font='Ariel 30'), ui.Button('8', size = (2,1), font='Ariel 30'), ui.Button('9', size = (2,1), font='Ariel 30'), ui.Button('x', size = (2,1), font='Ariel 30')],
            [ui.Button(symbol['radical'], size = (3,1), font='Ariel 20'), ui.Button('0', size = (3,1), font='Ariel 20'), ui.Button(symbol['power'], size = (3,1), font='Ariel 20'), ui.Button(symbol['divide'], size = (3,1), font='Ariel 20')],
            [ui.Button('C', size = (3,1), font='Ariel 20'), ui.Button('AC', size = (3,1), font='Ariel 20'),ui.Button('.', size = (3,1), font='Ariel 20'), ui.Button('=', size = (3,1), font='Ariel 20')]
        ]

        win1 = ui.Window("Arithmetic Calculator", layout = layout1)

        
        
        while True:
            event1, values1 = win1.read(timeout = 10000)
            if event1 in (None, 'Exit') :
                win1.close()
                win1_active = False
                win.UnHide()
                initval_entered = False
                break
            
            elif event1 in '1234567890.':
                initval_entered = True
                display_nos = values1['box']
                display_nos += event1

            elif event1 == '-' and not initval_entered:
                display_nos = values1['box']
                display_nos += event1

            elif event1 == 'C':
                display_nos = display_nos[:-1]

            elif event1 in '+-x*/' or event1 == symbol['divide'] or event1 == symbol['power'] or event1 == symbol['radical'] and initval_entered==True:
                if not clearlist:
                    operands = [result]
                    operators = []
                else:
                    try:
                        operands.append(float(display_nos))
                    except ValueError:
                        pass
                operators.append(event1)
                display_nos = ''
            
            elif event1 == 'AC':
                display_nos = ''
                operands = []
                operators = []
                result = 0.0
                clearlist = True
                initval_entered = False

            try:
                if event1 == '=' and initval_entered:
                    operands.append(float(display_nos))
                    for n in range(0,len(operands)-1):
                        if n == 0:
                            result = arith_calc(operands[0],operators[0],operands[1])
                        else:
                            result = arith_calc(result,operators[n],operands[n+1])
                    display_nos = str(result)
                    clearlist = False
                else:
                    pass
            except ValueError:
                display_nos = "Error"      
                        
            win1['box'].update(display_nos)

    if event == 'Factors Calculator':
        win2_active = True
        win.Hide()
        
        num = ''

        layout2 = [
            [ui.Text('Enter the number for which you would like \nto find all integer factors', font='Timesnewroman 20')],
            [ui.Input(font='Helvetica 30', size = (20,1), key = 'number', enable_events=True)],
            [ui.Text('The factors are:', font='Timesnewroman 20')],
            [ui.Multiline(font='Helvetica 20', size = (30,5), key = '-ML-', do_not_clear=False, disabled=True)],
            [ui.Button('Ok', size = (7,2), disabled = False), ui.Text('                                                                           '), ui.Exit(size = (7,2))]
        ]
        win2 = ui.Window("Factors Calculator", layout = layout2)
        
        
        while True:
            event2, values2 = win2.read(timeout = 10000)
            if event2 in (None, 'Exit'):
                win2.close()
                win2_active = False
                win.UnHide()
                break

                

            if event2 == 'Ok':
                
                try:  
                    num = abs(int(values2['number']))
                
                except ValueError:
                    win2['-ML-'].print('Please Enter A Valid Number')
                
                else:
                    factors = get_factors(num)

                    if len(factors) == 2:
                        win2['-ML-'].print(*factors, sep = "\n")
                        win2['-ML-'].print("\n")
                        win2['-ML-'].print(num, "is a prime number")

                    else:
                        win2['-ML-'].print(*factors, sep = "\n")
                        win2['-ML-'].print("\n")
                        win2['-ML-'].print(num, "is a composite number")
    
    if event == 'Lowest Term Calculator':
        win3_active = True
        win.Hide()

        font3 = "ComicsansMS 20"

        layout3 = [
            [ui.Text('Enter Numerator of Fraction:    ', font = font3), ui.Input(key = '-numer-', font = font3, justification='centre', size = (15,1))],
            [ui.Text(" "*50, font = font3), ui.Text("-"*28, font = font3)],
            [ui.Text('Enter Denominator of Fraction: ', font = font3), ui.Input(key = '-denom-', font = font3, justification='centre', size = (15,1))],
            [ui.Text(" ")],
            [ui.Text("The Lowest term is:                    ", font = font3), ui.Multiline(size = (15,4), font = font3, key = '-LowT-', do_not_clear=False, disabled = True)],
            [ui.Text(" ")],
            [ui.Text("The Decimal form is:                  ", font = font3), ui.Input(key = '-decimal-', font = font3, size = (15,1), disabled = True)],
            [ui.Button('Ok', size = (7,2)), ui.Text('                                                                                 '), ui.Exit(size = (7,2))]
        ]

        win3 = ui.Window("Lowest Term Calculator", layout = layout3, return_keyboard_events=True)

        while True:
            event3, values3 = win3.read(timeout = 10000)

            if event3 in (None, 'Exit'):
                win3.close()
                win3_active = False
                win.UnHide()
                break

            if event3 == 'Ok':
                
                try:  
                    numerator = int(values3['-numer-'])
                    denominator = int(values3['-denom-'])

                except ValueError:
                    win3['-LowT-'].print('Please Enter A Valid Number:')
                    
                
                else:
                    win3['-LowT-'].update('')
                    numerator, denominator, bar, decimalvalue = lowestterm(numerator, denominator)
                    win3['-LowT-'].print(int(numerator))
                    win3['-LowT-'].print('-'*bar)
                    win3['-LowT-'].print(int(denominator))
                    win3['-decimal-'].update(decimalvalue)
                
    if event == 'Quadratic Equation Solver':
        win4_active = True
        win.Hide()
        
        font4 = 'Georgia 20'

        layout4 = [
            [ui.Text('Enter your equation in standard Form:', font = font4)],
            [ui.Input(size = (4,1), key = '-a-', font = font4), ui.Text('x' + symbol['squared'] + ' +', font = font4), ui.Input(size = (4,1), key = '-b-', font = font4), ui.Text('x +', font = font4), ui.Input(size = (4,1), key = '-c-', font = font4),  ui.Text(' = 0', font = font4)],
            [ui.Text('')],
            [ui.Text('Roots are:', font = font4)],
            [ui.Text('x = ', font = font4), ui.Input(font = font4, size = (30,1), key = '-X1-', disabled=True)],
            [ui.Text('x = ', font = font4), ui.Input(font = font4, size = (30,1), key = '-X2-', disabled = True)],
            [ui.Text('')],
            [ui.Input(font = font4, size = (45,1), key = '-message-', disabled = True)],
            [ui.Button('Find Roots', size = (8,1), font = font4), ui.Text('                         '), ui.Button('Graph', size = (8,1), font = font4), ui.Text('                        '), ui.Exit(size = (8,1), font = font4)],
        ]

        win4 = ui.Window('Quadratic Equation Solver', layout4)

        while True:
            event4, values4 = win4.read(timeout = 10000)

            if event4 in (None, 'Exit'):
                win4.close()
                win4_active = False
                win.UnHide()
                break

            try:
                a = float(values4['-a-'])
                b = float(values4['-b-'])
                c = float(values4['-c-'])
            
            except ValueError:
                win4['-message-'].update('Enter Numerical Values of a, b and c.')
            
            else:

                if event4 == 'Find Roots':
                    try:
                        a = float(values4['-a-'])
                        b = float(values4['-b-'])
                        c = float(values4['-c-'])
                    
                    except ValueError:
                        win4['-message-'].update('Please enter appropriate value.')
                    
                    else:               
                        x1, x2, message = quadSolver(a, b, c)
                        win4['-X1-'].update(x1)
                        win4['-X2-'].update(x2)
                        win4['-message-'].update(message)
                
                if event4 == 'Graph':

                    dialogboxlayout4 = [
                        [ui.Text('Enter the range of your function:', font = font4)],
                        [ui.Text("")],
                        [ui.Text('x =', font = font4), ui.Input(size = (5,1), font = font4, key = '-xmin-'), ui.Text(' ------->', font = font4), ui.Text('x =', font = font4), ui.Input(size = (5,1), font = font4, key = '-xmax-', default_size = '100')],
                        [ui.Text("")],
                        [ui.Button('Ok', size = (7,1), font = font4)],
                        [ui.Text('', font = font4, size = (30,1), key = '-dmessage-')],
                    ]

                    dialogbox4 = ui.Window('Specify range of function', dialogboxlayout4)

                    while True:
                        event41, values41 = dialogbox4.read(timeout = 10000)

                        if event41 in (None, 'Exit'):
                            dialogbox4.close()
                            break

                        if event41 == 'Ok':
                            try:
                                xmin = float(values41['-xmin-'])
                                xmax = float(values41['-xmax-'])
                            
                            except ValueError:
                                win4['-dmessage-'].update('Please enter appropriate value.')
                            
                            else:
                                dialogbox4.close()
                                break

                    function = '(' + str(a) + ')*' + 'x' + '**2' + ' +' + '(' + str(b) + ')*' + 'x' + ' +' + '(' + str(c) + ')'
                    graph_func(function, xmin, xmax)

    if event == 'Function Grapher':
        win5_active = True
        win.Hide()

        font5 = 'calibri 15'

        layout5 = [
            [ui.Text('Enter a Function in Python syntax:'), ui.Input(key = '-func-')],
            [ui.Text('', key = '-out-', size = (30,1))],
            [ui.Button('Graph', size = (7,1), disabled = False), ui.Text('                                                                                                                      '), ui.Exit(size = (7,1))],
            
        ]

        win5 = ui.Window('Quadratic Equation Solver', layout5, font = font5 )

        while True:
            event5, values5 = win5.read(timeout = 10000)

            if event5 in (None, 'Exit'):
                win5.close()
                win5_active = False
                win.UnHide()
                break

            if event5 == 'Graph':

                dialogboxlayout5 = [
                        [ui.Text('Enter the range of your function:', font = font5)],
                        [ui.Text("")],
                        [ui.Text('x =', font = font5), ui.Input(size = (5,1), font = font5, key = '-xmin-', default_text='-100'), ui.Text(' ------->', font = font5), ui.Text('x =', font = font5), ui.Input(size = (5,1), font = font5, key = '-xmax-', default_text='100')],
                        [ui.Text("")],
                        [ui.Button('Ok', size = (7,1), font = font5)],
                        [ui.Text('', font = font5, size = (30,1), key = '-dmessage-')],
                    ]

                dialogbox5 = ui.Window('Specify range of function', dialogboxlayout5)

                while True:
                    event51, values51 = dialogbox5.read(timeout = 10000)

                    if event51 in (None, 'Exit'):
                        dialogbox5.close()
                        break

                    if event51 == 'Ok':
                        try:
                            xmin = float(values51['-xmin-'])
                            xmax = float(values51['-xmax-'])
                        
                        except ValueError:
                            win5['-dmessage-'].update('Please enter appropriate value.')
                        
                        else:
                            dialogbox5.close()
                            break
                try:
                    function = str(values5['-func-'])
                    graph_func(function,xmin,xmax)

                except (ValueError, SyntaxError,NameError) as e:
                    win5['-out-'].update('Enter valid Python expression')

                 







                        





