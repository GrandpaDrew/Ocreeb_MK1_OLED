print("Starting")

import board
import neopixel

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.tapdance import TapDance
from kmk.extensions.RGB import RGB
from midi import Midi

######## OLED SETUP HERE #########
import busio as io
import display
import displayio
from kmk.extensions.oled_1306 import DisplayOLED, LogoScene, StatusScene, KeypressesScene

layers_names = ['Colemak-DH', 'QWERTY', 'Sym-Nav', 'Number', 'Function']
scenes = [
    BitmapLogoScene("/canvas_raw.bmp"),
    KeypressesScene(matrix_width=16, matrix_height=4, split=True),
    StatusScene(layers_names=layers_names, separate_default_layer=True, rgb_ext=rgb_ext),
]
oled = display(i2c, scenes, rotation=180)
keyboard.extensions.append(oled)
displayio.release_displays()
i2c = busio.I2C(scl=board.SCL, sda=board.SDA, frequency=400000)
######## LED COLOR SETUP HERE #########
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.2
pixel.fill((0, 255, 255))
#######################################
    
# KEYTBOARD SETUP
layers = Layers()
keyboard = KMKKeyboard()
encoders = EncoderHandler()
tapdance = TapDance()
tapdance.tap_time = 250
keyboard.modules = [layers, encoders, tapdance]

# SWITCH MATRIX
keyboard.col_pins = (board.D3, board.D4, board.D5, board.D6)
keyboard.row_pins = (board.D7, board.D8, board.D9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ENCODERS
encoders.pins = ((board.A2, board.A1, board.A0, False), (board.SCK, board.MISO, board.MOSI, False),)

# EXTENSIONS
rgb_ext = RGB(pixel_pin = board.D10, num_pixels=4, hue_default=100)
midi_ext = Midi()
keyboard.extensions.append(rgb_ext)
keyboard.extensions.append(midi_ext)
keyboard.debug_enabled = False

####################################
##RUN GAME "CODE"##
Lethal = simple_key_sequence([KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(200), send_string('Powershell'), KC.ENTER, KC.MACRO_SLEEP_MS(200), send_string('Start Steam://run/1966720'), KC.ENTER, send_string('exit'), KC.ENTER])
    
####################################

# MACROS ROW 1
MACRO9 = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('open steam://rungameid/1966720'), KC.ENTER])
MACRO_10 = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('git status'), KC.ENTER])
MACRO_11 = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('print "Test"'), KC.ENTER])
MACRO_12 = Lethal

# MACROS ROW 2
MACRO5 = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('open https://ocrism.studio'), KC.ENTER])
MACRO6= simple_key_sequence([KC.LCMD(KC.LSFT(KC.BSPC))])
MACRO7 = simple_key_sequence([KC.LCMD(KC.LALT(KC.I))])
MACRO8 = simple_key_sequence([KC.LCMD(KC.LSFT(KC.R))])

# MACROS ROW 3
MACRO1 = KC.KP_1
MACRO2 = simple_key_sequence([KC.LCMD(KC.LALT(KC.ESCAPE))])
MACRO3 = KC.KP_3
LOCK = simple_key_sequence([KC.LCTRL(KC.LCMD(KC.Q)), KC.MACRO_SLEEP_MS(400), KC.ESCAPE])


_______ = KC.TRNS
xxxxxxx = KC.NO

# LAYER SWITCHING TAP DANCE
MACRO4 = KC.TD(LOCK, KC.MO(1), xxxxxxx, KC.TO(2))
MIDI_OUT = KC.TD(KC.MIDI(70), xxxxxxx, xxxxxxx, KC.TO(0))

# array of default MIDI notes
# midi_notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]

# KEYMAPS

keyboard.keymap = [
    # MACROS
    [
        MACRO1,    MACRO2,        MACRO3,    MACRO4,
        MACRO5,    MACRO6,        MACRO7,    MACRO8,
        MACRO9,    MACRO_10,      MACRO_11,  MACRO_12,
    ],
    # RGB CTL
    [
        xxxxxxx,    xxxxxxx,            xxxxxxx,                xxxxxxx,
        xxxxxxx,    KC.RGB_MODE_SWIRL,  KC.RGB_MODE_KNIGHT,     KC.RGB_MODE_BREATHE_RAINBOW,
        xxxxxxx,    KC.RGB_MODE_PLAIN,  KC.RGB_MODE_BREATHE,    KC.RGB_MODE_RAINBOW,
    ],
    # MIDI
    [
        KC.MIDI(30),    KC.MIDI(69),      KC.MIDI(70),       MIDI_OUT,
        KC.MIDI(67),    KC.MIDI(66),      KC.MIDI(65),       KC.MIDI(64),
        KC.MIDI(60),    KC.MIDI(61),      KC.MIDI(62),       KC.MIDI(63),
    ]
]

encoders.map = [    ((KC.VOLD, KC.VOLU, KC.MUTE),           (KC.MINUS,    KC.EQUAL,     KC.MUTE)),   # MACROS
                    ((KC.RGB_AND, KC.RGB_ANI, xxxxxxx),     (KC.RGB_HUD,    KC.RGB_HUI,     _______   )),   # RGB CTL
                    ((KC.VOLD, KC.VOLU, KC.MUTE),           (KC.RGB_VAD,    KC.RGB_VAI,     KC.RGB_TOG)),   # MIDI
                ]


if __name__ == '__main__':
    keyboard.go()
