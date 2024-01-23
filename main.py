@namespace
class SpriteKind:
    Wire = SpriteKind.create()

def on_up_pressed():
    global cursorPos
    cursorPos += -1
    if cursorPos < 0:
        cursorPos = wireCount - 1
    UpdateCursor()
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def UpdateCursor():
    cursor.top = Math.floor(120 / Ratio) * (cursorPos + 1) - 2
def _5wire():
    if redcount > 1 and 0 % 2 == 1:
        if WireList[3] == 0:
            game.splash("cut wire 4")
        elif WireList[2] == 0:
            game.splash("cut wire 3")
        else:
            game.splash("cut wire 2")
def startPhase():
    global wireCount
    while wireCount < 3 or wireCount > 6:
        wireCount = game.ask_for_number("# of wires? (3-6)", 1)

def on_a_pressed():
    pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def InitSerial():
    global SerialNumber
    SerialNumber = game.ask_for_number("Last Digit of Serial Number", 1)
def InitWirePhase():
    InitColours()
    InitCursor()

def on_left_pressed():
    global sprite_list, mySprite2
    WireList[cursorPos] = WireList[cursorPos] - 1
    if WireList[cursorPos] < 0:
        WireList[cursorPos] = len(colourList) - 1
    WireSprites[cursorPos].fill(colourList[WireList[cursorPos]])
    WireSprites[cursorPos].draw_rect(0, 0, 160, 5, 15)
    sprite_list = sprites.all_of_kind(SpriteKind.Wire)
    for value in sprite_list:
        if value.top == Math.floor(120 / Ratio) * (cursorPos + 1):
            value.destroy()
    mySprite2 = sprites.create(WireSprites[cursorPos], SpriteKind.Wire)
    mySprite2.top = Math.floor(120 / Ratio) * (cursorPos + 1)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def InitCursor():
    global mySprite, cursor, cursorPos
    mySprite = img("""
        ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
    """)
    mySprite.draw_rect(0, 0, 160, 9, 10)
    mySprite.draw_rect(0, 1, 160, 7, 10)
    cursor = sprites.create(mySprite, SpriteKind.Wire)
    cursor.top = Math.floor(120 / Ratio) - 2
    cursorPos = 0
def InitColours():
    global colourList, WireList, Ratio, WireSprites, mySprite, mySprite2
    colourList = [2, 1, 8, 5, 15]
    WireList = []
    Ratio = wireCount + 1
    WireSprites = []
    index = 0
    while index <= wireCount - 1:
        WireList.append(0)
        mySprite = img("""
            ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
                        ................................................................................................................................................................
        """)
        mySprite.fill(colourList[WireList[index]])
        mySprite.draw_rect(0, 0, 160, 5, 15)
        WireSprites.append(mySprite)
        mySprite2 = sprites.create(mySprite, SpriteKind.Wire)
        mySprite2.top = Math.floor(120 / Ratio) * (index + 1)
        index += 1

def on_right_pressed():
    global sprite_list, mySprite2
    WireList[cursorPos] = (WireList[cursorPos] + 1) % len(colourList)
    WireSprites[cursorPos].fill(colourList[WireList[cursorPos]])
    WireSprites[cursorPos].draw_rect(0, 0, 160, 5, 15)
    sprite_list = sprites.all_of_kind(SpriteKind.Wire)
    for value2 in sprite_list:
        if value2.top == Math.floor(120 / Ratio) * (cursorPos + 1):
            value2.destroy()
    mySprite2 = sprites.create(WireSprites[cursorPos], SpriteKind.Wire)
    mySprite2.top = Math.floor(120 / Ratio) * (cursorPos + 1)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def _4wire():
    global redcount, whitecount
    for value3 in list2:
        if value3 == 0:
            redcount += 1
        elif value3 == 1:
            whitecount += 1
        else:
            pass
    if redcount > 1 and 0 % 2 == 1:
        if WireList[3] == 0:
            game.splash("cut wire 6")
        elif WireList[2] == 0:
            game.splash("cut wire 8")
        else:
            game.splash("cut wire 5")

def on_on_created(sprite):
    sprite.set_flag(SpriteFlag.GHOST, True)
sprites.on_created(SpriteKind.Wire, on_on_created)

def on_down_pressed():
    global cursorPos
    cursorPos += 1
    cursorPos = cursorPos % wireCount
    UpdateCursor()
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def _6wire():
    global redcount, whitecount
    for value4 in list2:
        if value4 == 0:
            redcount += 1
        elif value4 == 1:
            whitecount += 1
        else:
            pass
    if redcount > 1 and 0 % 2 == 1:
        if WireList[3] == 0:
            game.splash("cut wire 4")
        elif WireList[2] == 0:
            game.splash("cut wire 3")
        else:
            game.splash("cut wire 2")
def _3wires():
    global redcount
    redcount = 0
    if True:
        if WireList[3] == 0:
            game.splash("cut wire 4")
        else:
            game.splash("cut wire 3")
whitecount = 0
list2: List[number] = []
mySprite: Image = None
mySprite2: Sprite = None
sprite_list: List[Sprite] = []
WireSprites: List[Image] = []
colourList: List[number] = []
SerialNumber = 0
WireList: List[number] = []
redcount = 0
Ratio = 0
cursor: Sprite = None
cursorPos = 0
wireCount = 0
wireCount = 0
class phase(Enum):
    start = 0
    wire = 1
    solve = 2
state: phase = phase.start
startPhase()
if True:
    InitSerial()
state += 1
scene.set_background_color(1)
InitWirePhase()