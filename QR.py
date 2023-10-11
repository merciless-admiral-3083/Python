import pyqrcode
import png
from pyqrcode import QRCode
a= "https://www.instagram.com/ritu.nahal" #just add the websiite link you want
url = pyqrcode.create(a)
url.svg("myqr.svg", scale = 8)
url.png('myqr.png', scale = 6)