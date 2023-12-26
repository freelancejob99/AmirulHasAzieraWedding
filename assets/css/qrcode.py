import pyqrcode

link = "https://www.zlansataykesuma.com"
qr_code = pyqrcode.create(link)
qr_code.png("zlansateqr.png", scale = 5)