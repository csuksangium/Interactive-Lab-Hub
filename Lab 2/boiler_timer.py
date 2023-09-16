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


def display_image_horizontal_center(image_to_open):
    center_size = 110
    center_image = Image.open(image_to_open)
    center_image = center_image.resize((center_size, center_size), Image.BICUBIC)
    center_image = center_image.rotate(90, Image.NEAREST, expand=True)

    x_center = width // 2 - center_image.width // 2
    y_center = height // 2 - center_image.height // 2

    draw.rectangle((0, 0, width, height), outline=0, fill="#FFFFFF")
    # paste the center image (sun/moon) onto the background
    image.paste(center_image, (x_center + 10, y_center), mask=center_image)
    disp.image(image)

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
            draw.rectangle((0, 0, width, height), outline=0, fill='#000000')
            disp.image(image)
            return image_to_open

        display_image_horizontal_center(image_to_open)
        time.sleep(0.1)


def draw_image_while_cooking(food_choice):
    food_choice_dict = {'egg_choice.png': 'boiling_food.png',
                        'noodle_ready.png': 'noodle_cooking.png',
                        'pasta_choice.png': 'pasta_cooking.png'}
    food_cooking = food_choice_dict[food_choice]

    string_msg = "{}".format("food_cooking")
    y = top
    draw.text((20, 30), string_msg, font=font, fill="#7FFF00")
    disp.image(image, 90)
    center_size = 110
    while(True):

        # draw.rectangle((0, 0, width, height), outline=0, fill="#000000")



        # image_to_open = looping_list(curr_index)
        # if buttonA.value and not buttonB.value:
        #     curr_index -= 1
        #     image_to_open = looping_list(curr_index)
        # elif buttonB.value and not buttonA.value:
        #     curr_index += 1
        #     image_to_open = looping_list(curr_index)
        # elif not buttonB.value and not buttonA.value:
        #     print("BREAK")
        #     draw.rectangle((0, 0, width, height), outline=0, fill=400)
        #     disp.image(image)
        #     break
        #
        # center_image = Image.open(image_to_open)
        # center_image = center_image.resize((center_size, center_size), Image.BICUBIC)
        # center_image = center_image.rotate(90, Image.NEAREST, expand=True)
        #
        # x_center = width // 2 - center_image.width // 2
        # y_center = height // 2 - center_image.height // 2
        #
        # # make sure the sky color is in line with the time of day
        # draw.rectangle((0, 0, width, height), outline=0, fill="#FFFFFF")
        # # paste the center image (sun/moon) onto the background
        # image.paste(center_image, (x_center + 10, y_center), mask=center_image)
        # disp.image(image)
        time.sleep(0.2)

food_choice = draw_image_to_cook()
draw_image_while_cooking(food_choice)
while True:
    y = top
    CURR_TIME = time.strftime("%m/%d/%Y %H:%M:%S")
    draw.text((x, y), CURR_TIME, font=font, fill="#FFFFFF")

    # if buttonA.value and not buttonB.value and start_time == 0:
    #   print("BUTTONA")
    #   start_time = time.time()
    #   is_time_keeping = True
    # elif buttonA.value and not buttonB.value and start_time != 0:
    #   if is_time_keeping:
    #     print("BUTTONAPAUSE")
    #     is_time_keeping = False
    #     pause_time = time.time()
    #   else:
    #     print("BTTNARESUME")
    #     is_time_keeping = True
    #     pause_time_dur = time.time() - pause_time
    #     start_time = start_time + pause_time_dur
    #     pause_time = 0
    #     pause_time_dur = 0
    # if buttonB.value and not buttonA.value and not is_time_keeping:
    #   start_time = 0
    #   pause_time = 0
    #   is_time_keeping = False
    # print(is_time_keeping)
    # time_to_display = 0
    # if is_time_keeping and start_time != 0:
    #   print("starttimekeep")
    #   time_to_display = time.time() - start_time
    # elif not is_time_keeping and start_time == 0:
    #   print("not start")
    #   time_to_display = 0
    # elif not is_time_keeping and start_time != 0:
    #   print("pause")
    #   time_to_display = pause_time - start_time
    #
    # y += 30
    # draw.text((x, y), str(time_to_display), font=font, fill="#FFFF00")
    #
    # # Display image.
    # disp.image(image, rotation)
    time.sleep(1)

