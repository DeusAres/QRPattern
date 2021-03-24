import qrcode
import PySimpleGUI as sg
from PIL import Image, ImageDraw

layout = [
    [sg.Input("URL", key = '-URL-')],
    [sg.Button("Generate", bind_return_key = True)]
]

mainWindow = sg.Window("QR to A4", layout)

while True:
    event, values = mainWindow.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    QR_code = qrcode.make(values['-URL-']).convert("RGBA")
    QR_code_outline = ImageDraw.Draw(QR_code)
    width = 5
    QR_code_outline.rectangle([(0,0), (QR_code.width, QR_code.height)], outline = "#000000", width = width)
    W, H = 2480, 3508

    QR_code.show()
    canvas = Image.new("RGBA", (W, H), "#FFFFFF")
    line_QR_code = Image.new("RGBA", (W, QR_code.height), "#FFFFFF")

    for x in range(0, W, QR_code.width):
        if x + QR_code.width > W:
            break
        line_QR_code.paste(QR_code, (x, 0), QR_code)
        #line_QR_code =
    line_QR_code.show()
    
    for y in range(0, H, QR_code.height):
        canvas.paste(line_QR_code, (0, y), line_QR_code)
        if y + QR_code.height > H:
            break

    canvas.show()
        
    

