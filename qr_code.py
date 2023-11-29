import qrcode

def generate_qr_code(link, save_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)

if __name__ == "__main__":
    link = input("Enter the link you want to generate a QR code for: ")
    save_path = input("Enter the filename to save the QR code (e.g., qr_code.png): ")

    generate_qr_code(link, save_path)
    print(f"QR code saved as {save_path}")
