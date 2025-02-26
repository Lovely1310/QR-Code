import qrcode

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = "https://www.youtube.com/@monikasaini1188"
qr.add_data(data)
qr.make(fit=True)

# Generate the image and store it in a variable
img = qr.make_image(fill="black", back_color="white")

# Save the image
img.save('text.png')

