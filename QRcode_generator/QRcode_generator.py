import qrcode

data = input("Enter the text or URL for your QR code: ")

qr = qrcode.make(data)

qr.save("my_qr_code.png")

print(" QR Code generated successfully!")
print(" Saved as: my_qr_code.png")
