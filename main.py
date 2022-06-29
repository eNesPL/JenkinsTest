#read values from specific places on screen
import pyautogui
import time

#read text between coordinates
#(804, 352) (935, 378)
import pytesseract as pytesseract
from PIL import Image

a = {'x1':804, 'y1':352, 'x2':905, 'y2':378}
#(805, 527)(932, 554)
b = {'x1':804, 'y1':527, 'x2':905, 'y2':554}
#(804, 699)(933, 726)
c = {'x1':804, 'y1':699, 'x2':905, 'y2':726}
#(806, 876)(935, 900)
d = {'x1':804, 'y1':876, 'x2':905, 'y2':900}
def read_text(a, b, c, d):
    #read text from screen
    text_a = pyautogui.screenshot(region=(a['x1'], a['y1'], a['x2']-a['x1'], a['y2']-a['y1']))
    text_a = text_a.resize((900, 300))
    text_a.save('a.png')
    text_b = pyautogui.screenshot(region=(b['x1'], b['y1'], b['x2']-b['x1'], b['y2']-b['y1']))
    text_b = text_b.resize((900, 300))
    text_b.save('b.png')
    text_c = pyautogui.screenshot(region=(c['x1'], c['y1'], c['x2']-c['x1'], c['y2']-c['y1']))
    text_c = text_c.resize((900, 300))
    text_c.save('c.png')
    text_d = pyautogui.screenshot(region=(d['x1'], d['y1'], d['x2']-d['x1'], d['y2']-d['y1']))
    text_d = text_d.resize((900, 300))
    text_d.save('d.png')

    #read text from image
    text_a = pytesseract.image_to_string(text_a)
    text_b = pytesseract.image_to_string(text_b)
    text_c = pytesseract.image_to_string(text_c)
    text_d = pytesseract.image_to_string(text_d)
    #print text
    #return text replace non-numeric characters with empty string .replace(",","").replace(".","").replace("\n","").replace(":","")
    return text_a.replace(",","").replace(".","").replace("\n","").replace(":",""), text_b.replace(",","").replace(".","").replace("\n","").replace(":",""), text_c.replace(",","").replace(".","").replace("\n","").replace(":",""), text_d.replace(",","").replace(".","").replace("\n","").replace(":","")

# get smallest value read_text(a,b,c,d) < 2000000 and click on it
def get_smallest_value(a,b,c,d):
    readed_a, readed_b, readed_c, readed_d= read_text(a,b,c,d)
    try:
        readed_a = int(readed_a)
    except:
        readed_a = 2000000
    try:
        readed_b = int(readed_b)
    except:
        readed_b = 2000000
    try:
        readed_c = int(readed_c)
    except:
        readed_c = 2000000
    try:
        readed_d = int(readed_d)
    except:
        readed_d = 2000000

    if readed_a < readed_d and readed_a < readed_c and readed_a < readed_b:
        if readed_a < 2000000:
            return a
    elif readed_b < readed_d and readed_b < readed_c and readed_b < readed_a:
        if readed_b < 2000000:
            return b
    elif readed_c < readed_d and readed_c < readed_b and readed_c < readed_a:
        if readed_c < 2000000:
            return c
    elif readed_d < readed_c and readed_d < readed_b and readed_d < readed_a:
        if readed_d < 2000000:
            return d
    else:
        return None
while True:
    g = get_smallest_value(a,b,c,d)
    if (g!=None):
        #click on g
        pyautogui.click(g['x1'], g['y1'])
        time.sleep(2)
        #send arrow down
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
    else:
        #send arrow down
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
    time.sleep(1)

