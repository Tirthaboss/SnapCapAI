import streamlit as st

st.write("App is coming soon")
# Import Modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import streamlit as st
from PIL import Image
import io
import google.generativeai as genai

# Streamlit Page Config
st.set_page_config(
    page_title="SnapCapAI",
    page_icon="img/icon.png",  # Replace with a valid path if local
    layout="wide",
    initial_sidebar_state="expanded",
)

# Configure Gemini API
api = st.secrets["AI"]["key"]
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-2.0-flash-preview-image-generation")

# Email Sender Function
def send_email(subject, message, from_addr, to_addr, password, image_bytes, image_name="image.png"):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    # Attach the image from bytes
    image = MIMEImage(image_bytes, name=image_name)
    image.add_header('Content-ID', '<image>')
    msg.attach(image)

    # Attach the HTML message
    html_message = f"""
    <html>
    <body>
    <p>{message}</p>
    <img src="cid:image">
    </body>
    </html>
    """
    msg.attach(MIMEText(html_message, 'html'))

    # SMTP Server Setup
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Email sending failed: {e}")

# Streamlit App UI
st.title("📸 SnapCapAI - Generate Social Media Captions from Images")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
name = st.text_input("Your Name (Required)")
usermail = st.text_input("Your Email (Required)")

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image to bytes
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    image_bytes = buffered.getvalue()

    if st.button("Generate Caption"):
        with st.spinner("Generating caption..."):
            try:
                # Generate caption using Gemini API
                response = model.generate_content(
                    [
                        {"mime_type": "image/png", "data": image_bytes},
                        {"text": "Generate a creative and engaging social media caption in different tone for this image."}
                    ]
                )
                caption = response.text
                # Send email notification (if email provided)
                if usermail:
                    subject = f"{name or 'Someone'} used SnapCapAI"
                    message = f"Name: {name or 'Unknown'}, Email: {usermail} used SnapCapAI to generate a caption."
                    from_addr = st.secrets["Email"]["sender"]
                    to_addr = st.secrets["Email"]["reciever"]
                    password = st.secrets["Email"]["password"]
                    send_email(subject, message, from_addr, to_addr, password, image_bytes, uploaded_file.name)
                    st.balloons()
                    st.success("Caption Generated:")
                    st.write(caption)

             
>>>>>>> ed3732d (Install Project)
