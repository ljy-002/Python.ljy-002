from qrcode import *


print('\n       欢迎来到二维码制造机')
x = input('\n请输入你想在二维码里面储存的文字：')
print('\n若想查看二维码，请返回桌面查看')
print('\n若没有看见二维码，请等待一会，此二维码制造机无bug')
qr = QRCode()
qr.add_data(x)
img = qr.make_image()
img.show()
