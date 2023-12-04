from __future__ import annotations

from fractions import Fraction

import PySimpleGUI as sg

import computing
import linkedlist as ll

equationStack = ll.LinkedList()
currentNode: ll.ListNode | None = None

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

current_element: sg.Button = ctrl_button
current_element_color: tuple = ctrl_button.ButtonColor

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


def is_ctrl() -> bool:
    return not (ctrl_button.ButtonColor == shift_button_color)


def ctrl_pressed():
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


alias = {
    "BackSpace:8": "<-",
    "Delete:46": "<-",
    "Escape:27": "cls",
    "\r": "=",
}

ctrl_key_change = {
    "sin": "asin",
    "cos": "acos",
    "tan": "atan",
    "asin": "sin",
    "acos": "cos",
    "atan": "tan"
}

formular = {
    "pow": "pow(",
    "asin": "asin(",
    "acos": "acos(",
    "atan": "atan(",
    "sin": "sin(",
    "cos": "cos(",
    "tan": "tan(",
    "log": "log(",
    "^": "pow(",
    "ln": "ln(",
    "fac": "fac(",
    "fibonacci": "fibonacci(",
    "π": "pi",
    "!": "fac(",
    "√": "root(",
    "e": "e",
    "+": "+",
    ",": ",",
    ".": ".",
    "-": "-",
    "*": "*",
    "/": "/",
    ")": ")",
    "(": "(",

}

for i in range(10):
    formular[str(i)] = str(i)

temp_text = ""

computing.load_cache()

while True:
    event, values = window.read()
    print(f"event: {event} values: {values}")

    alias_button = alias.get(str(event))
    if alias_button is not None:
        event = alias_button

    ctrl_change = ctrl_key_change.get(event)
    if ctrl_change is not None and is_ctrl():
        event = ctrl_change

    if event is None or event == sg.WIN_CLOSED:
        print("Closing window...")
        break
    elif event == "ctrl" or str(event).startswith("Control_"):
        ctrl_pressed()
    elif event == "to fraction" and computing.is_float(calculation.get()):
        calculation.update(value=f"{computing.to_fraction(float(calculation.get()))}")
    elif str(calculation.get()).startswith("Error while calculating: "):
        calculation.update(value=temp_text)
        continue
    elif event == "Up:38":
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
    elif event == "=":
        if calculation.get() == "":
            continue
        try:
            result = computing.get_result(calculation.get())
            equationStack.append(result.calculation)
            equationStack.to_last()
            currentNode = equationStack.last
            calculation.update(value=f"{result.result}")
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
        f = formular.get(event)
        if f is None:
            continue
        calculation.update(value=str(calculation.get()) + f)

    element: sg.Button = window.find_element(event, True)

    if element is not None:
        try:
            current_element.update(button_color=current_element_color)
            current_element = element
            current_element_color = current_element.ButtonColor
            current_element.update(button_color=(current_element_color[0], "red"))
        except AttributeError:
            continue
