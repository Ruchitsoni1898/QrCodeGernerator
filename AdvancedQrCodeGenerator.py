import qrcode

# Create a QR code object
qr_obj = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

# Add data to the QR code
qr_obj.add_data("https://www.tutorialspoint.com/python/index.htm")
qr_obj.make(fit=True)

# Generate the image with specified colors
qr_img = qr_obj.make_image(fill='blue', back_color='red')

# Save the QR code image to a file
qr_img.save("img1.png")
