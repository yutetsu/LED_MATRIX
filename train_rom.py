import os
from PIL import Image, ImageDraw, ImageFilter
from display import show, clear

# Init variable for sys option

# Create const
EXT = ".png"
LEDS_SIZE = 128, 32

# Create variable
output = {}


def train(cmd, train, special, type, dest, line, full_type):
    output.clear()
    led1 = Image.new("RGB", (LEDS_SIZE), (0, 0, 0))
    led2 = Image.new("RGB", (LEDS_SIZE), (0, 0, 0))
    led3 = Image.new("RGB", (LEDS_SIZE), (0, 0, 0))
    led4 = Image.new("RGB", (LEDS_SIZE), (0, 0, 0))

    if cmd == "CLEAR":
        output[f'CMD'] = 'CLEAR'
        clear()

    elif cmd == "UPDATE":
        os.system("update-git")

    elif cmd == "SHOW":
        output[f'CMD'] = 'SHOW'

        if train.startswith("E233"):
            output[f'{train} ROM VER'] = '2.3 [TEST]'
            if special != "" and type == "":
                output[f'SPECIAL'] = special
                ledframe = 1
                try:
                    special_frame = Image.open(train + "/SPECIAL/" + special + EXT)
                except IOError:
                    return f"[{train}] /SPECIA/{special}{EXT} not found"
                led1.paste(special_frame, (0, 0))
            else:
                if dest != "" and type == "":
                    output[f'FULL_DEST'] = dest
                    ledframe = 1
                    full_dest_frame = Image.open(
                    try:
                        train + "/FULL_DEST/" + dest + EXT)
                    except IOError:
                        return f"[{train}] /FULL_DEST/{dest}{EXT} not found"
                    led1.paste(full_dest_frame, (0, 0))
                if line != "" and type == "":
                    output[f'FULL_LINE'] = line
                    ledframe = 1
                    try:
                        line_frame = Image.open(train + "/FULL_LINE/" + line + EXT)
                    except IOError:
                        return f"[{train}] /FULL_LINE/{line}{EXT} not found"
                    led1.paste(line_frame, (0, 0))
                if type != "" and dest == "":
                    output[f'FULL_TYPE'] = type
                    ledframe = 1
                    try:
                        full_type_frame = Image.open(train + "/FULL_TYPE/" + type + EXT)
                    except IOError:
                        return f"[{train}] /FULL_TYPE/{type}{EXT} not found"
                    led1.paste(full_type_frame, (0, 0))
                if type != "" and dest != "":
                    output[f'TYPE'] = type
                    ledframe = 2
                    try:
                        type_jp_frame = Image.open(train + "/TYPE/" + type + "_JP" + EXT)
                        type_en_frame = Image.open(train + "/TYPE/" + type + "_EN" + EXT)
                    except IOError:
                        return f"[{train}] /TYPE/{type}{EXT} not found"
                    led1.paste(type_jp_frame, (0, 0))
                    led2.paste(type_en_frame, (0, 0))
                    output[f'DEST'] = dest
                    try:
                        dest_frame = Image.open(train + "/DEST/" + dest + EXT)
                    except IOError:
                        return f"[{train}] /DEST/{dest}{EXT} not found"
                    led1.paste(dest_frame, (48, 0))
                    led2.paste(dest_frame, (48, 0))
                    if line != "":
                        output[f'LINE'] = line
                        ledframe = 3
                        try:
                            line_frame = Image.open(train + "/LINE/" + line + EXT)
                        except IOError:
                            return f"[{train}] /LINE/{line}{EXT} not found"
                        led3.paste(type_jp_frame, (0, 0))
                        led3.paste(line_frame, (48, 0))
                        if full_type == "TRUE":
                            output[f'FULL_TYPE'] = full_type
                            ledframe = 4
                            try:
                                full_type_frame = Image.open(train + "/FULL_TYPE/" + type + EXT)
                            except IOError:
                                return f"[{train}] /FULL_TYPE/{type}{EXT} not found"
                            led4.paste(full_type_frame, (0, 0))
                    if full_type == "TRUE":
                        output[f'FULL_TYPE'] = full_type
                        ledframe = 3
                        try:
                            full_type_frame = Image.open(train + "/FULL_TYPE/" + type + EXT)
                        except IOError:
                            return f"[{train}] /FULL_TYPE/{type}{EXT} not found"
                        led3.paste(full_type_frame, (0, 0))

        elif train == "RM1000":
            output[f'{train} ROM VER'] = '1.1 [FINAL]'
            if special != "":
                output[f'SPECIAL'] = special
                ledframe = 1
                try:
                    special_frame  = Image.open(train + "/SPECIAL/" + special + EXT)
                except IOError:
                    return f"[{train}] /SPECIA/{special}{EXT} not found"
                led1.paste(special_frame, (0,0))
            else:
                if type != "":
                    output[f'TYPE'] = type
                    ledframe = 1
                    try:
                        type_frame = Image.open(train + "/TYPE/" + type + EXT)
                    except IOError:
                        return f"[{train}] /TYPE/{type}{EXT} not found"
                    led1.paste(type_frame, (0,0))
                if dest != "":
                    output[f'DEST'] = dest
                    ledframe = 1
                    try:
                        dest_frame = Image.open(train + "/DEST/" + dest + EXT)
                    except IOError:
                        return f"[{train}] /DEST/{dest}{EXT} not found"
                    led1.paste(dest_frame, (48,0))

        elif train == "JR305":
            output[f'{train} ROM VER'] = '1.1 [FINAL]'
            if special != "":
                output[f'SPECIAL'] = special
                ledframe = 1
                try:
                    special_frame  = Image.open(train + "/SPECIAL/" + special + EXT)
                except IOError:
                    return f"[{train}] /SPECIA/{special}{EXT} not found"
                led1.paste(special_frame, (0,0))
            else:
                if type != "":
                    output[f'TYPE'] = type
                    ledframe = 1
                    try:
                        type_frame = Image.open(train + "/TYPE/" + type + EXT)
                    except IOError:
                        return f"[{train}] /TYPE/{type}{EXT} not found"
                    led1.paste(type_frame, (0,0))
                if dest != "":
                    output[f'DEST'] = dest
                    ledframe = 1
                    try:
                        dest_frame = Image.open(train + "/DEST/" + dest + EXT)
                    except IOError:
                        return f"[{train}] /DEST/{dest}{EXT} not found"
                    led1.paste(dest_frame, (52,0))

        elif train == "SR01":
            output[f'{train} ROM VER'] = '1.1 [FINAL]'
            if special != "":
                output[f'SPECIAL'] = special
                ledframe = 1
                try:
                    special_frame  = Image.open(train + "/SPECIAL/" + special + EXT)
                except IOError:
                    return f"[{train}] /SPECIA/{special}{EXT} not found"
                led1.paste(special_frame, (0,0))
            else:
                if type != "":
                    output[f'TYPE'] = type
                    ledframe = 1
                    try:
                        type_frame = Image.open(train + "/TYPE/" + type + EXT)
                    except IOError:
                        return f"[{train}] /TYPE/{type}{EXT} not found"
                    led1.paste(type_frame, (0,0))
                if dest != "":
                    output[f'DEST'] = dest
                    ledframe = 1
                    try:
                        dest_frame = Image.open(train + "/DEST/" + dest + EXT)
                    except IOError:
                        return f"[{train}] /DEST/{dest}{EXT} not found"
                    led1.paste(dest_frame, (48,0))

        elif train == "TX3000":
            output[f'{train} ROM VER'] = '1.1 [FINAL]'
            if special != "":
                output[f'SPECIAL'] = special
                ledframe = 1
                try:
                    special_frame  = Image.open(train + "/SPECIAL/" + special + EXT)
                except IOError:
                    return f"[{train}] /SPECIA/{special}{EXT} not found"
                led1.paste(special_frame, (0,0))
            else:
                if type != "":
                    output[f'TYPE'] = type
                    ledframe = 1
                    try:
                        type_frame = Image.open(train + "/TYPE/" + type + EXT)
                    except IOError:
                        return f"[{train}] /TYPE/{type}{EXT} not found"
                    led1.paste(type_frame, (0,0))
                if dest != "":
                    output[f'DEST'] = dest
                    ledframe = 1
                    try:
                        dest_frame = Image.open(train + "/DEST/" + dest + EXT)
                    except IOError:
                        return f"[{train}] /DEST/{dest}{EXT} not found"
                    led1.paste(dest_frame, (48,0))

        elif train == "JR110":
            output[f'{train} ROM VER'] = '1.0 [TEST]'
            if special != "":
                output[f'SPECIAL'] = special
                ledframe = 1
                try:
                    special_frame  = Image.open(train + "/SPECIAL/" + special + EXT)
                except IOError:
                    return f"[{train}] /SPECIA/{special}{EXT} not found"
                led1.paste(special_frame, (0,0))
            else:
                if type != "":
                    output[f'TYPE'] = type
                    ledframe = 2
                    try:
                        type_frame_jp = Image.open(train + "/TYPE/" + type + "_JP"  + EXT)
                        type_frame_en = Image.open(train + "/TYPE/" + type + "_EN" + EXT)
                    except IOError:
                        return f"[{train}] /TYPE/{type}{EXT} not found"
                    led1.paste(type_frame_jp, (0,0))
                    led2.paste(type_frame_en, (0,0))
                if dest != "":
                    output[f'DEST'] = dest
                    ledframe = 2
                    try:
                        dest_frame_jp = Image.open(train + "/DEST/" + dest + "_JP" + EXT)
                        dest_frame_en = Image.open(train + "/DEST/" + dest + "_EN" + EXT)
                    except IOError:
                        return f"[{train}] /DEST/{dest}{EXT} not found"
                    led1.paste(dest_frame_jp, (35,0))
                    led2.paste(dest_frame_en, (35,0))


        else:
            return "[ERROR] ROM NOT FOUND"
    
        show(ledframe, led1, led2, led3, led4)

    print(str(output))
    return str(output)
