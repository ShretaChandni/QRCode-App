import streamlit as st
import qrcode
from io import BytesIO

st.title("🎉 QR Code Generator")

data = st.text_input("Enter the text or URL to generate a QR Code:")
fill_color = st.color_picker("Choose fill color", "#000000")
back_color = st.color_picker("Choose background color", "#FFFFFF")

def generate_qr_code(data, fill_color, back_color):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)

    img_bytes = BytesIO()
    qr_img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    return img_bytes

if st.button("Generate QR Code"):
    if data:
        qr_bytes = generate_qr_code(data, fill_color, back_color)
        st.image(qr_bytes, caption="Your QR Code", use_column_width=False)
        st.download_button(label="Download QR Code", data=qr_bytes.getvalue(), file_name="qrcode.png", mime="image/png")
    else:
        st.warning("⚠️ Please enter text or a URL!")
