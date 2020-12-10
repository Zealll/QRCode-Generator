import pyqrcode
import png
from pyqrcode import QRCode
import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
)

data='https://zealll.github.io/test/index.html'

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('test.png')

# s = 

# url = pyqrcode.create(s)

# url.png('myqr.png', scale=6)

# print(url)





