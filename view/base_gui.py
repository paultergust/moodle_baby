import PySimpleGUI as sg


def blank_frame():
    return sg.Frame(
        "",
        [[]],
        pad=(5, 3),
        expand_x=True,
        expand_y=True,
        background_color="#404040",
        border_width=0,
    )


sg.theme("DarkGrey15")

layout_frame1 = [
    [blank_frame(), blank_frame()],
    [
        sg.Frame(
            "Frame 3",
            [[blank_frame()]],
            # pad=(5, 3),
            expand_x=True,
            expand_y=True,
            title_location=sg.TITLE_LOCATION_TOP,
        )
    ],
]

# layout_frame2 = [[blank_frame()]]

layout = [
    [
        sg.Listbox(
            values=['test', 'test1', 'test2'],
            size=(20, 25),
            expand_x=False,
            expand_y=True,
        ),
        sg.Frame(
            "Frame 1", layout_frame1, size=(800, 30), expand_x=True, expand_y=True
        ),
    ]
]

window = sg.Window("Title", layout, margins=(2, 2), finalize=True, resizable=True)

while True:

    event, values = window.read()
    print(event, values)
    if event == sg.WINDOW_CLOSED:
        break

window.close()
