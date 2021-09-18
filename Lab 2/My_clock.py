import time
import subprocess
from PIL import Image, ImageDraw, ImageFont
import digitalio
import board
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import

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
    x_offset=67,
    y_offset=120,
)

# Create blank image for drawing.
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
#padding = -2
#top = padding
#bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
#x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)


MoleImage = Image.open("./Moles/tile019.png")


# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

MoleImage = MoleImage.rotate(90)

image_ratio = MoleImage.width / MoleImage.height
screen_ratio = width / height
if screen_ratio < image_ratio:
    scaled_width = MoleImage.width * height // MoleImage.height
    scaled_height = height
else:
    scaled_width = width
    scaled_height = MoleImage.height * width // MoleImage.width
MoleImage = MoleImage.resize((int(scaled_width/2-10), int(scaled_height/2-10)), Image.BICUBIC)

print(scaled_height/2)
print(scaled_width/2)







def image_format(picture):
    picture = picture.convert('RGB')
    picture = picture.rotate(90)
    picture = picture.resize((120, 200), Image.BICUBIC)

    return picture



#image = image_format(image)
#draw = ImageDraw.Draw(image)
# Display image.
disp.image(MoleImage)













