# Written by DougDoug (DougDoug on Youtube, DougDougW on Twitch)

# Hello!
# This file contains the main logic to process Twitch chat and convert it to game commands.
# All sections that you need to update are labeled with a "TODO" comment.
# The source code primarily comes from:
    # Wituz's "Twitch Plays" tutorial: http://www.wituz.com/make-your-own-twitch-plays-stream.html
    # PythonProgramming's "Python Plays GTA V" tutorial: https://pythonprogramming.net/direct-input-game-python-plays-gta-v/

# There are 2 other files needed to run this code:
    # TwitchPlays_AccountInfo.py is where you put your Twitch username and OAuth token. This is to keep your account details separated from the main source code.
    # TwitchPlays_Connection.py is the code that actually connects to Twitch. You should not modify this file.

# Disclaimer:
    # This code is NOT optimized or well-organized. I am not a Python programmer.
    # I created a simple version that works quickly, and I'm sharing it for educational purposes.

###############################################
# Import and define our functions / key codes to send key commands

# General imports
import time
import subprocess
import ctypes
import random
import string

# Twitch imports
import TwitchPlays_Connection
from TwitchPlays_AccountInfo import TWITCH_USERNAME, TWITCH_OAUTH_TOKEN

# Controller imports
import pyautogui
import pynput
from pynput.mouse import Button, Controller

SendInput = ctypes.windll.user32.SendInput

# KEY PRESS NOTES
# The standard "Twitch Plays" tutorial key commands do NOT work in DirectX games (they only work in general windows applications)
# Instead, we use DirectX key codes and input functions below.
# This DirectX code is partially sourced from: https://stackoverflow.com/questions/53643273/how-to-keep-pynput-and-ctypes-from-clashing

# Presses and permanently holds down a keyboard key
def PressKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# Releases a keyboard key if it is currently pressed down
def ReleaseKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# Helper function. Holds down a key for the specified number of seconds, then releases it.
def PressAndHoldKey(hexKeyCode, seconds):
    PressKeyPynput(hexKeyCode)
    time.sleep(seconds)
    ReleaseKeyPynput(hexKeyCode)

def command(commandname, chance = "1"):
    if random.randint(1,int(chance)) == 1:
        i = 0
        for i in range(len(commandname)):
            PressAndHoldKey(alphabetkeys[alphabetlist.index(commandname[i])], 0.1)
# Mouse Controller, using pynput
    # pynput.mouse functions are found at: https://pypi.org/project/pynput/
    # NOTE: pyautogui's click() function permanently holds down in DirectX, so I used pynput instead for mouse instead.
mouse = Controller()

###############################################
# DIRECTX KEY CODES
# These codes identify each key on the keyboard.
# Note that DirectX's key codes (or "scan codes") are NOT the same as Windows virtual hex key codes.
#   DirectX codes are found at: https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-6.0/aa299374(v=vs.60)
Q = 0x10
W = 0x11
E = 0x12
R = 0x13
T = 0x14
Y = 0x15
U = 0x16
I = 0x17
O = 0x18
P = 0x19
A = 0x1E
S = 0x1F
D = 0x20
F = 0x21
G = 0x22
H = 0x23
J = 0x24
K = 0x25
L = 0x26
Z = 0x2C
X = 0x2D
C = 0x2E
V = 0x2F
B = 0x30
N = 0x31
M = 0x32
alphabetlist = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
alphabetkeys = [0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x32]
ESC = 0x01
ONE = 0x02
TWO = 0x03
THREE = 0x04
FOUR = 0x05
FIVE = 0x06
SIX = 0x07
SEVEN = 0x08
EIGHT = 0x09
NINE = 0x0A
ZERO = 0x0B
MINUS = 0x0C
EQUALS = 0x0D
BACKSPACE = 0x0E
SEMICOLON = 0x27
TAB = 0x0F
CAPS = 0x3A
ENTER = 0x1C
LEFT_CONTROL = 0x1D
LEFT_ALT = 0x38
LEFT_SHIFT = 0x2A
SPACE = 0x39
DELETE = 0x53
COMMA = 0x33
PERIOD = 0x34
BACKSLASH = 0x35
NUMPAD_0 = 0x52a
NUMPAD_1 = 0x4F
NUMPAD_2 = 0x50
NUMPAD_3 = 0x51
NUMPAD_4 = 0x4B
NUMPAD_5 = 0x4C
NUMPAD_6 = 0x4D
NUMPAD_7 = 0x47
NUMPAD_8 = 0x48
NUMPAD_9 = 0x49
NUMPAD_PLUS = 0x4E
NUMPAD_MINUS = 0x4A
LEFT_ARROW = 0xCB
RIGHT_ARROW = 0xCD
UP_ARROW = 0xC8
DOWN_ARROW = 0xD0
LEFT_MOUSE = 0x100
RIGHT_MOUSE = 0x101
MIDDLE_MOUSE = 0x102
MOUSE3 = 0x103
MOUSE4 = 0x104
MOUSE5 = 0x105
MOUSE6 = 0x106
MOUSE7 = 0x107
MOUSE_WHEEL_UP = 0x108
MOUSE_WHEEL_DOWN = 0x109
########################################################

# An optional countdown before the code actually starts running, so you have time to load up the game before messages are processed.
# TODO: Set the "countdown" variable to whatever countdown length you want.
countdown = 0 #The number of seconds before the code starts running
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

# Connects to your twitch chat, using your username and OAuth token.
# TODO: make sure that your Twitch username and OAuth token are added to the "TwitchPlays_AccountInfo.py" file
t = TwitchPlays_Connection.Twitch();
t.twitch_connect(TWITCH_USERNAME, TWITCH_OAUTH_TOKEN);

##########################################################

while True:
    # Check for new chat messages
    new_messages = t.twitch_recieve_messages();
    if not new_messages:
        continue
    else:
        for message in new_messages:
            # We got a new message! Get the message and the username.
            msg = message['message'].lower()
            username = message['username'].lower()

            # TODO:
            # Now that you have a chat message, this is where you add your game logic.
            # Use the "PressKeyPynput(KEYCODE)" function to press and hold down a keyboard key.
            # Use the "ReleaseKeyPynput(KEYCODE)" function to release a specific keyboard key.
            # Use the "PressAndHoldKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
            # Use "mouse.press(Button.left)" or "mouse.release(Button.left)" to press/release the mouse. Can use Button.right for right click.

            # I've added some example videogame logic code below:

            ###################################
            # Example GTA V Code
            ###################################

            # If the chat message is "left", then hold down the A key for 2 seconds
            if msg == "left":
                PressAndHoldKey(A, 2)

            # If the chat message is "right", then hold down the D key for 2 seconds
            if msg == "right":
                PressAndHoldKey(D, 2)

            # If message is "drive", then permanently hold down the W key
            if msg == "drive":
                ReleaseKeyPynput(S) #release brake key first
                PressKeyPynput(W) #start permanently driving

            # If message is "reverse", then permanently hold down the S key
            if msg == "reverse":
                ReleaseKeyPynput(W) #release drive key first
                PressKeyPynput(S) #start permanently reversing

            # Release both the "drive" and "reverse" keys
            if msg == "stop":
                print("recieved")
                ReleaseKeyPynput(W)
                ReleaseKeyPynput(S)

            # Press the spacebar for 0.7 seconds
            if msg == "brake":
                PressAndHoldKey(SPACE, 0.7)

            # Presses the left mouse button down for 1 second, then releases it
            if msg == "health, armor, $250k, repairs car":
                command("hesoyam")
            if msg == "(semi)infinite health":
                command("baguvix", 20)
            if msg == "infinite oxygen":
                command("cvwkxam")
            if msg == "weapon set 1":
                command("lxgiwyl")
            if msg == "weapon set 2":
                command("professionalskit")
            if msg == "weapon set 3":
                command("uzumymw")
            if msg == "perfect vehicle handling":
                command("sticklikeglue")
            if msg == "adrenaline mode":
                command("anoseonglass")
            if msg == "infinite ammo, no reloading":
                command("fullclip")
            if msg == "increase wanted level +2":
                command("turnuptheheat")
            if msg == "clear wanted level":
                command("turndowntheheat")
            if msg == "fat body":
                command("btcdbcb")
            if msg == "muscular body":
                command("buffmeup")
            if msg == "skinny body":
                command("kvgyzqk")
            if msg == "disable wanted level":
                command("aezakmi")
            if msg == "six star wanted level":
                command("bringiton", 50)
            if msg == "maximum respect":
                command("worshipme")
            if msg == "maximum sex appeal":
                command("helloladies")
            if msg == "maximum stamina":
                command("vkypqcf")
            if msg == "hitman level for all weapon stats":
                command("professionalkiller")
            if msg == "maximize all vehicle skill stats":
                command("naturaltalent")0
            if msg == "fast motion":
                command("speeditup")
            if msg == "slow motion":
                command("slowitdown", 20)
            if msg == "people attack each other with golf clubs":
                command("ajlojyqy")
            if msg == "have a bounty on your head":
                command("bagowpg", 25)
            if msg == "pedestrians hunt you":
                command("foooxft", 25)
            if msg == "suicide":
                command("goodbyecruelworld")
            if msg == "elvis models for people":
                command("bluesuedeshoes")
            if msg == "people attack with rocket launchers":
                command("bgluawml")
            if msg == "beach party mode":
                command("lifesabeach")
            if msg == "gang members mode":
                command("onlyhomiesallowed")
            if msg == "gang control":
                command("bifbuzz")
            if msg == "ninja theme":
                command("ninjatown")
            if msg == "women talk to you":
                command("bekknqv")
            if msg == "big bunny hop":
                command("cjphonehome")
            if msg == "mega jump":
                command("kangaroo")
            if msg == "riot mode":
                command("stateofemergency", 50)
            if msg == "funhouse mode":
                command("crazytown")
            if msg == "recruit anyone":
                command("sjmahpe")
            if msg == "recruit anyone":
                command("rocketmayhem")
            if msg == "blow up all cars":
                command("cpktnwt", 100)
            if msg == "invisible car":
                command("wheelsonlyplease")
            if msg == "all green lights":
                command("zeiivg")
            if msg == "aggressive drivers":
                command("ylteicz")
            if msg == "pink cars":
                command("llqpfbn")
            if msg == "black cars":
                command("iowdlac")
            if msg == "all cheap cars":
                command("everyoneispoor")
            if msg == "all fast cars":
                command("everyoneisrich")
            if msg == "flying cars":
                command("chittychittybangbang")
            if msg == "flying boats":
                command("flyingfish")
            if msg == "cars blow up easily":
                command("jcnruad", 50)
            if msg == "all cars have nitro":
                command("speedfreak")
            if msg == "moon car gravity":
                command("bubblecars")
            if msg == "free aim while driving":
                command("ouiqdmw")
            if msg == "reduced traffic":
                command("ghosttown")
            if msg == "country vehicles":
                command("fvtmnbz")
            if msg == "country vehicles and people":
                command("bmtpwhr")


            if msg == "spawn jetpack":
                command("rocketman")
            if msg == "spawn rhino":
                command("iwprton")
            if msg == "spawn parachute":
                command("aiypwzqp")
            if msg == "spawn bloodring banger":
                command("oldspeeddemon")
            if msg == "spawn rancher":
                command("jqntdmh")
            if msg == "spawn racecar":
                command("vrockpokey")
            if msg == "spawn racecar":
                command("vpjtqwv")
            if msg == "spawn romero":
                command("wheresthefuneral")
            if msg == "spawn stretch":
                command("celebritystatus")
            if msg == "spawn trashmaster":
                command("truegrime", 20)
            if msg == "spawn caddy":
                command("rzhsuew")
            if msg == "spawn hydra":
                command("jumpjet")
            if msg == "spawn vortex hovercraft":
                command("kgggdkp")
            if msg == "spawn hunter":
                command("ohdude")
            if msg == "spawn quad":
                command("fourwheelfun")
            if msg == "spawn tanker truck":
                command("amomhrer")
            if msg == "spawn dozer":
                command("itsallbull")
            if msg == "spawn stunt plane":
                command("flyingtostunt")
            if msg == "spawn monster":
                command("monstermash")


            if msg == "sunny weather":
                command("pleasantlywarm")
            if msg == "very sunny weather":
                command("toodamnhot")
            if msg == "overcast weather":
                command("alnsfmzo")
            if msg == "rainy weather":
                command("auifrvqs")
            if msg == "foggy weather":
                command("cfvfgmj")
            if msg == "faster clock":
                command("ysohnul")
            if msg == "always midnight":
                command("nightprowler")
            if msg == "orange sky":
                command("ofviac")
            if msg == "thunderstorm":
                command("scottishsummer")
            if msg == "sandstorm":
                command("cwjxuoc")
            ###################################
            # Example Miscellaneous Code
            ###################################

            # Clicks and drags the mouse upwards, using the Pyautogui commands.
            # NOTE: unfortunately, Pyautogui does not work in DirectX games like GTA V. It will work in all other environments (e.g. on your desktop)
            # If anyone finds a reliable way to move the mouse in DirectX games, please let me know!
            if msg == "drag mouse up":
                pyautogui.drag(0, -50, 0.25, button='left')

            # Clicks and drags the mouse downwards, using the Pyautogui commands
            if msg == "drag mouse down":
                pyautogui.drag(0, 50, 0.25, button='left')

            # An example of pressing 2 keys at once.
            # First holds down the LEFT_CONTROL key, then presses the A key for 0.1 seconds, then releases the LEFT_CONTROL key.
            if msg == "select all":
                PressKeyPynput(LEFT_CONTROL)
                PressAndHoldKey(A, 0.1)
                ReleaseKeyPynput(LEFT_CONTROL)

            # Can use pyautogui.typewrite() to type messages from chat into the keyboard.
            # Here, if a chat message says "type ...", it will type out their text.
            if msg.startswith("type "):
                try:
                    typeMsg = msg[5:] # Ignore the "type " portion of the message
                    pyautogui.typewrite(typeMsg)
                except:
                    # There was some issue typing the msg. Print it out, and move on.
                    print("Typing this particular message didn't work: " + msg)
