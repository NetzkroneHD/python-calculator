from __future__ import annotations

import PySimpleGUI as sg
import linkedlist as ll

from fractions import Fraction
import math

equationStack = ll.LinkedList()
currentNode: ll.ListNode | None = None

pi = math.pi
e = math.e

fib_cache = {
    0: 0,
    1: 1
}

fac_cache = {
    0: 1,
    1: 1
}


def root(x, y):
    return math.pow(x, 1 / y)


def pow(x, y):
    return math.pow(x, y)


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def tan(x):
    return math.tan(x)


def asin(x):
    return math.asin(x)


def acos(x):
    return math.acos(x)


def atan(x):
    return math.atan(x)


def ln(x):
    return math.log(x, e)


def log(x, base):
    return math.log(x, base)


def fac(x):
    fc = 1
    for i in range(x + 1):
        if i in fac_cache:
            fc = fac_cache[i]
        else:
            fc *= i
            fac_cache[i] = fc
    return fc


def is_ctrl() -> bool:
    return not (ctrl_button.ButtonColor == shift_button_color)


def is_float(x: str) -> bool:
    try:
        float(x)
        return True
    except ValueError:
        return False


def fibonacci(n):
    if n in fib_cache:
        return fib_cache.get(n)
    n1 = fibonacci(n - 1)
    n2 = fibonacci(n - 2)

    fib_cache[n - 1] = n1
    fib_cache[n - 2] = n2

    return n1 + n2


fibonacci(99)

space = " "
calculation: sg.InputText = sg.InputText("", background_color="GREY", justification="CENTER",
                                         expand_y=True, expand_x=True, disabled=True,
                                         use_readonly_for_disable=True)

ctrl_button = sg.Button("ctrl", expand_x=True)

cls_button = sg.Button("cls", expand_x=True, tooltip="Clears the screen")
to_fraction_button = sg.Button("to fraction", expand_x=True, tooltip="Converts the calculation to a fraction")

log_button = sg.Button("log", expand_x=True, tooltip="Usage: log(x, base)")
ln_button = sg.Button("ln", expand_x=True, tooltip="Description: Represents the natural log\nUsage: ln(x)")
fibonacci_button = sg.Button("fibonacci", expand_x=True, tooltip="Usage: fibonacci(n)")

sin_button = sg.Button("sin", expand_x=True, tooltip="Usage: sin(x)")
cos_button = sg.Button("cos", expand_x=True, tooltip="Usage: cos(x)")
tan_button = sg.Button("tan", expand_x=True, tooltip="Usage: tan(x)")

pi_button = sg.Button("π", expand_x=True)
e_button = sg.Button("e", expand_x=True)
pow_button = sg.Button("^", expand_x=True, tooltip="Usage: pow(base, exponent)")
root_button = sg.Button("√", expand_x=True, tooltip="Usage: root(radicand, exponent)")
fac_button = sg.Button("!", expand_x=True, tooltip="Usage: fac(x)")

comma_button = sg.Button(",", expand_x=True)
bracket_o_button = sg.Button("(", expand_x=True)
bracket_c_button = sg.Button(")", expand_x=True)
del_button = sg.Button("<-", expand_x=True)

shift_button_color = ctrl_button.ButtonColor

layout = [
    [sg.Text(f"{space:100}", expand_x=True)],
    [calculation],
    # cls
    [ctrl_button, to_fraction_button, cls_button],
    # log ln <-
    [log_button, ln_button, del_button],
    # sin cos tan fibonacci
    [sin_button, cos_button, tan_button, fibonacci_button],
    # π e ^ √
    [pi_button, e_button, pow_button, root_button],
    # , ( ) !
    [comma_button, bracket_o_button, bracket_c_button, fac_button],
    # 1 2 3 +
    [sg.Button("1", expand_x=True, button_color="darkblue"),
     sg.Button("2", expand_x=True, button_color="darkblue"),
     sg.Button("3", expand_x=True, button_color="darkblue"),
     sg.Button("+", expand_x=True)],
    # 4 5 6 -
    [sg.Button("4", expand_x=True, button_color="darkblue"),
     sg.Button("5", expand_x=True, button_color="darkblue"),
     sg.Button("6", expand_x=True, button_color="darkblue"),
     sg.Button("-", expand_x=True)],
    # 7 8 9 *
    [sg.Button("7", expand_x=True, button_color="darkblue"),
     sg.Button("8", expand_x=True, button_color="darkblue"),
     sg.Button("9", expand_x=True, button_color="darkblue"),
     sg.Button("*", expand_x=True)],
    # . 0 = /
    [sg.Button(".", expand_x=True, button_color="darkblue"),
     sg.Button("0", expand_x=True, button_color="darkblue"),
     sg.Button("=", expand_x=True, button_color="darkblue"),
     sg.Button("/", expand_x=True)]]

window = sg.Window("Simple Calculator", layout, auto_size_text=True, return_keyboard_events=True)

allowed_keys = ["π", "e", "^", ",", "(", ")", "<-", "+", "-", "*", "/", ".", ",", "BackSpace:8", "Delete:46",
                "Escape:27", "\r", "=", "cls", "root(", "√", "sin", "cos", "tan", "asin", "acos", "atan", "log", "ln",
                "fac", "!", "Control_L:17", "fibonacci", "f", "Up:38", "Down:40"]

ctrl_key_change = {
    "sin": "asin",
    "cos": "acos",
    "tan": "atan",
    "asin": "sin",
    "acos": "cos",
    "atan": "tan"
}

# Dieses Dictionary wird verwendet, um Tastaturevents, die von PySimpleGUI generiert werden, auf andere Befehle umzuleiten.
button_alias = {
    "\r": "=",
    "BackSpace:8": "<-",
    "Escape:27": "cls",
    "r": "√",
    "p": "π",
    "f": "fibonacci",
}

# Ähnlich wie button_alias, wird dieses Dictionary verwendet, um Symbole oder Tastaturereignisse auf andere Symbole oder Befehle umzuleiten
symbol_alias = {
    "π": "pi",
    "BackSpace:8": "<-",
    "Delete:46": "<-",
    "\r": "=",
    "Escape:27": "cls",
    "p": "pi",
    "r": "root("
}

symbol_commands = {
    "BackSpace:8": "<-",
    "Delete:46": "<-",
    "\r": "=",
    "Escape:27": "cls",
    "p": "pi",
    "π": "pi",
    "fibonacci": "fibonacci(",
    "f": "fibonacci(",
    "!": "fac(",
    "√": "root(",
    "r": "root(",
    "root": "root(",
    "^": "pow(",
    "pow": "pow(",
    "asin": "asin(",
    "acos": "acos(",
    "atan": "atan(",
    "sin": "sin(",
    "cos": "cos(",
    "tan": "tan(",
    "log": "log(",
    "ln": "ln(",
    "fac": "fac("
}

for i in range(10):
    allowed_keys.append(str(i))

temp_text = ""

current_element: sg.Button = ctrl_button
current_element_color: tuple = ctrl_button.ButtonColor

while True:
    event, values = window.read()

    if event is None or event == sg.WIN_CLOSED:
        print("Closing window...")
        break
    elif event == "ctrl" or event == "Control_L:17":
        if not is_ctrl():
            sin_button.update(text="asin")
            cos_button.update(text="acos")
            tan_button.update(text="atan")
            ctrl_button.update(button_color=(shift_button_color[0], "blue"))
        else:
            sin_button.update(text="sin")
            cos_button.update(text="cos")
            tan_button.update(text="tan")
            ctrl_button.update(button_color=shift_button_color)

        continue
    elif event == "to fraction" and is_float(str(calculation.get())):
        calculation.update(value=f"{str(Fraction(float(calculation.get())).limit_denominator())}")
        continue

    elif event not in allowed_keys and event not in symbol_alias:
        continue
    elif str(calculation.get()).startswith("Error while calculating: "):
        calculation.update(value=temp_text)
        continue

    if event == "Up:38":
        if currentNode is not None:
            if currentNode.previous is not None:
                calculation.update(value=f"{currentNode.previous.value}")
                currentNode = currentNode.previous
            else:
                calculation.update(value=f"{currentNode.value}")
        continue
    elif event == "Down:40":
        if currentNode is not None:
            if currentNode.next is not None:
                calculation.update(value=f"{currentNode.next.value}")
                currentNode = currentNode.next
            else:
                calculation.update(value=f"{currentNode.value}")
        continue

    element: sg.Button = window.find_element(event, True)

    if element is not None:
        try:
            alias = button_alias.get(event)
            if alias is not None:
                element = window.find_element(alias, True)

            current_element.update(button_color=current_element_color)
            current_element = element
            current_element_color = current_element.ButtonColor
            current_element.update(button_color=(current_element_color[0], "red"))
        except AttributeError:
            continue

    event_alias = symbol_alias.get(event)

    if event_alias is not None:
        event = event_alias
    if is_ctrl() and event in ctrl_key_change:
        event = ctrl_key_change[event]

    cmd = symbol_commands.get(event)

    if cmd is not None:
        calculation.update(value=str(calculation.get()) + cmd)
    elif event == "=":
        if calculation.get() == "":
            continue
        try:
            code = eval(compile(str(calculation.get()), "<string>", "eval"))
            equationStack.append(calculation.get())
            equationStack.to_last()
            currentNode = equationStack.last
            print(f"EquationStack: {equationStack}")
            calculation.update(value=f"{code}")
        except Exception as ex:

            temp_text = str(calculation.get())
            calculation.update(value=f"Error while calculating: {ex}")

    elif event == "cls":
        calculation.update(value="")
        equationStack.to_last()
        currentNode = equationStack.last

    elif event == "<-":
        calculation.update(value=str(calculation.get())[0:len(str(calculation.get())) - 1])

    else:
        calculation.update(value=str(calculation.get()) + event)
window.close()
exit(1)
