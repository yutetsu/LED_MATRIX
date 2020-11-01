import os
from PIL import Image, ImageDraw, ImageFilter

rows = "32"
cols = "64"
chain_length = "2"
brightness = "100"
mapping = "regular-pi1"
rgb_sequence = "RBG"
led_slowdown_gpio = "3"

def show(LEDFRAME, led1 , led2, led3, led4):
    grid = Image.open("BIN/grid.png").convert("RGBA")
    x, y = grid.size
    
    if LEDFRAME == 1:
        temp = led1.convert('RGBA')
        temp.save("BIN/temp1.png") 
        temp_big = led1.resize((385, 97), Image.NEAREST).convert('RGBA')
        temp_big.paste(grid, (0, 0, x, y), grid)
        temp_big.save("BIN/temp1_big.png") 
        
    if LEDFRAME == 2:
        temp = led1.convert('RGBA')
        temp.save("BIN/temp1.png")
        temp = led2.convert('RGBA')
        temp.save("BIN/temp2.png")
        temp_big = led1.resize((385, 97), Image.NEAREST).convert('RGBA')
        temp_big.paste(grid, (0, 0, x, y), grid)
        temp_big.save("BIN/temp1_big.png") 
        temp_big = led2.resize((385, 97), Image.NEAREST).convert('RGBA')
        temp_big.paste(grid, (0, 0, x, y), grid)
        temp_big.save("BIN/temp2_big.png") 
    
    if LEDFRAME == 3:
        temp = led1.convert('RGBA')
        temp.save("BIN/temp1.png")
        temp = led2.convert('RGBA')
        temp.save("BIN/temp2.png")
        temp = led3.convert('RGBA')
        temp.save("BIN/temp3.png")
        temp_big = led1.resize((385, 97), Image.NEAREST).convert('RGBA')
        temp_big.paste(grid, (0, 0, x, y), grid)
        temp_big.save("BIN/temp1_big.png") 
        temp_big = led2.resize((385, 97), Image.NEAREST).convert('RGBA')
        temp_big.paste(grid, (0, 0, x, y), grid)
        temp_big.save("BIN/temp2_big.png")
        temp_big = led3.resize((385, 97), Image.NEAREST).convert('RGBA')
        temp_big.paste(grid, (0, 0, x, y), grid)
        temp_big.save("BIN/temp3_big.png") 
    
    if LEDFRAME == 4:
        temp = led1.convert('RGBA')
        temp.save("BIN/temp1.png")
        temp = led2.convert('RGBA')
        temp.save("BIN/temp2.png")
        temp = led3.convert('RGBA')
        temp.save("BIN/temp3.png")
        temp = led4.convert('RGBA')
        temp.save("BIN/temp4.png")
        temp_big = led1.resize((385, 97), Image.NEAREST).convert('RGBA')
        temp_big.paste(grid, (0, 0, x, y), grid)
        temp_big.save("BIN/temp1_big.png") 
        temp_big = led2.resize((385, 97), Image.NEAREST).convert('RGBA')
        temp_big.paste(grid, (0, 0, x, y), grid)
        temp_big.save("BIN/temp2_big.png")
        temp_big = led3.resize((385, 97), Image.NEAREST).convert('RGBA')
        temp_big.paste(grid, (0, 0, x, y), grid)
        temp_big.save("BIN/temp3_big.png") 
        temp_big = led4.resize((385, 97), Image.NEAREST).convert('RGBA')
        temp_big.paste(grid, (0, 0, x, y), grid)
        temp_big.save("BIN/temp4_big.png") 
    
    #os.system("sudo pkill -u daemon")
    #os.system("sudo led-image-viewer -f -w 3 BIN/temp1.png BIN/temp2.png BIN/temp3.png BIN/temp4.png --led-rows="+rows+" --led-cols="+cols+" --led-chain="+chain_length+" --led-brightness="+brightness+" --led-gpio-mapping="+mapping+" --led-rgb-sequence="+rgb_sequence+" --led-slowdown-gpio="+led_slowdown_gpio+" --led-daemon")
    return

def demo():
    #os.system("sudo pkill -u daemon")
    #os.system("sudo led-image-viewer -f -w 3 BIN/アドレス1.gif --led-rows="+rows+" --led-cols="+cols+" --led-chain="+chain_length+" --led-brightness="+brightness+" --led-gpio-mapping="+mapping+" --led-rgb-sequence="+rgb_sequence+" --led-slowdown-gpio="+led_slowdown_gpio+" --led-daemon")
    return

def clear():
    #os.system("sudo pkill -u daemon")
    return