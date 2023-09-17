import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

is_time_keeping = False
start_time = 0
pause_time = 0

cooking_times_in_seconds = {'egg_choice.png': 360,
                        'noodle_ready.png': 240,
                        'pasta_choice.png': 720}


def looping_list(index):
    food_choices = ['egg_choice.png', 'noodle_ready.png', 'pasta_choice.png']
    return food_choices[index % len(food_choices)]


def display_image_horizontal_center(image_to_open, image2, bg_color="#FFFFFF"):
    img_size = 100
    image_to_display = Image.open(image_to_open)
    image_to_display = image_to_display.resize((img_size, img_size), Image.BICUBIC)
    image_to_display = image_to_display.rotate(90, Image.NEAREST, expand=True)

    offset = 30
    x_center = width // 2 - image_to_display.width // 2
    y_center = height // 2 - image_to_display.height // 2 + offset

    draw.rectangle((0, 0, width, height), outline=0, fill=bg_color)
    image.paste(image_to_display, (x_center, y_center + 30), mask=image_to_display)

    px, py = 10, 10
    sx, sy = image2.size
    image.paste(image2, (px, py, px + sx, py + sy), image2)

    disp.image(image)


def display_info(curr_mode, food_choice=None) -> Image:
    pre_text = ''
    text = ''
    if curr_mode == 'SELECT':
        cooking_time = cooking_times_in_seconds[food_choice]
        pre_text = 'Please select food to cook'
        text = str(cooking_time) + ' seconds'
    elif curr_mode == 'COOKING':
        text = 'Food is cooking'
    elif curr_mode == 'DONE':
        pre_text = 'DONE COOKING!'
        text = 'Any button to exit'

    image2 = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw2 = ImageDraw.Draw(image2)
    draw2.text((0, 80), text=pre_text, font=font, fill="#000000")
    draw2.text((0, 100), text=text, font=font, fill="#000000")
    image2 = image2.rotate(90, expand=1)
    return image2


def draw_image_to_cook():
    curr_index = 0
    while(True):
        # food menu, use button to cycle
        # select with 2 buttons
        image_to_open = looping_list(curr_index)
        if buttonA.value and not buttonB.value:
            curr_index -= 1
            image_to_open = looping_list(curr_index)
        elif buttonB.value and not buttonA.value:
            curr_index += 1
            image_to_open = looping_list(curr_index)
        elif not buttonB.value and not buttonA.value:
            return image_to_open
        img2 = display_info(curr_mode='SELECT', food_choice=image_to_open)
        display_image_horizontal_center(image_to_open, image2=img2)
        time.sleep(0.1)


def draw_image_while_cooking(food_choice):
    food_choice_dict = {'egg_choice.png': 'boiling_food.png',
                        'noodle_ready.png': 'noodle_cooking.png',
                        'pasta_choice.png': 'pasta_cooking.png'}

    cooking_time = cooking_times_in_seconds[food_choice]
    food_cooking = food_choice_dict[food_choice]

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    disp.image(image)
    # Draw some shapes.
    timeout = cooking_time
    timeout_start = time.time()
    pre_text = 'Cooking...'
    while time.time() < timeout_start + timeout:
        time_to_display = time.time() - timeout_start
        to_display = str(round(time_to_display, 2)) + ' / ' + str(cooking_time)

        image2 = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw2 = ImageDraw.Draw(image2)
        draw2.text((0, 80), text=pre_text, font=font, fill="#000000")
        draw2.text((40, 100), text=str(to_display), font=font, fill="#000000")
        image2 = image2.rotate(90, expand=1)

        display_image_horizontal_center(food_cooking, image2=image2)
        time.sleep(0.2)


def draw_image_done(food_choice):
    food_done_dict = {'egg_choice.png': 'egg_done.png',
                      'noodle_ready.png': 'noodle_done.png',
                      'pasta_choice.png': 'pasta_ready.png'}
    food_done = food_done_dict[food_choice]

    img2 = display_info(curr_mode='DONE')
    display_image_horizontal_center(food_done, image2=img2)

    while(True):
        # exit with
        if buttonA.value and not buttonB.value:
            return
        elif buttonB.value and not buttonA.value:
            return
        time.sleep(0.1)


while True:
    food_choice = draw_image_to_cook()
    draw_image_while_cooking(food_choice)
    draw_image_done(food_choice)
