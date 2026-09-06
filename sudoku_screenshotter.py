import easyocr
import pyautogui as pag
import keyboard
import numpy as np
import cv2
from sudoku_solver import solve

reader = easyocr.Reader(['en'])

box_pos = []
for x in range(9):
    for y in range(9):
        box_pos.append([54+82*y,310+82*x,114,114])
#450+55*y,240+55*x,75,75
print("Ready")
keyboard.wait('insert')

grid = [[],[],[],[],[],[],[],[],[]]

for i, x in enumerate(box_pos):
    image = np.array(pag.screenshot('folk.png', region=x))
    img = cv2.imread('folk.png')
    img = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2)))
    result = reader.readtext(img, detail=0, allowlist=['1','2','3','4','5','6','7','8','9'], text_threshold=0.4, low_text=0.3, link_threshold=0.4, mag_ratio=1, x_ths=.7, y_ths=.7)
    grid[i//9].append(0 if not result else int(str(result)[2:3]))


copmpleteGrid = solve(grid)

for x in copmpleteGrid:
    #print(x)
    for y in x:
        pag.press(str(y))
        pag.press('right')
    pag.press('left')
    pag.press('left')
    pag.press('left')
    pag.press('left')
    pag.press('left')
    pag.press('left')
    pag.press('left')
    pag.press('left')
    pag.press('left')
    pag.press('down')