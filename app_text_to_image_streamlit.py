import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# FastAPI URL
API_URL = "https://enactment-wreath-massager.ngrok-free.dev"

st.title("🎨 AI Image Generation App")

# Prompt input
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="A beautiful futuristic city at sunset..."
)

# Generate button
if st.button("Generate Image"):

    if not prompt.strip():
        st.warning("Please enter a prompt.")

    else:

        data = {
            "prompt": prompt
        }

        try:

            response = requests.post(
                API_URL + "/generate",
                json=data,
                timeout=300
            )

            if response.status_code == 200:

                # Convert API response into image
                image = Image.open(
                    BytesIO(response.content)
                )

                st.subheader("Generated Image")

                st.image(
                    image,
                    caption=prompt,
                    use_container_width=True
                )

                # Download button
                st.download_button(
                    label="⬇️ Download Image",
                    data=response.content,
                    file_name="generated_image.png",
                    mime="image/png"
                )

            else:

                st.error(
                    f"API Error: {response.status_code}"
                )

                st.write(response.text)

        except requests.exceptions.RequestException as e:

            st.error(
                f"Connection error: {e}"
            )