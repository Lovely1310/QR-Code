import qrcode

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = "https://www.meesho.com/RRSHREEKRISHNATRADERS?_ms=2&page=1&fbclid=PAY2xjawIB-ZxleHRuA2FlbQIxMQABpgpAOrxqDxwQi8RSM1_y1aEPZLOI1G6aAh3Kzd8eo8sNloOtOUy31CVaeg_aem_WnPzIZBhWBIxVkCBM4WZ0A"
qr.add_data(data)
qr.make(fit=True)

# Generate the image and store it in a variable
img = qr.make_image(fill="black", back_color="white")

# Save the image
img.save('text.png')

