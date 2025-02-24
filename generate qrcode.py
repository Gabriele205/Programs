import qrcode
link = input('Enter the link:\n')
qr = qrcode.make(link)

qr.save('Qr.png')

print('QR code generated successfully!')