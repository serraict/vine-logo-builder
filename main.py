import os
from PIL import Image, ImageDraw, ImageFont

# Configuration
input_dir = "input"
output_dir = "output"
icon_list = [
    {"name": "phone", "unicode": "\uF095"},
    {"name": "book", "unicode": "\uF02D"},
    {"name": "laptop", "unicode": "\uF109"},
]  # Replace unicode values with correct ones for your icons
icon_color_dark = (22, 22, 22)  # Black-ish
icon_color_light = (222, 222, 222)  # White-ish
icon_size_ratio = 0.6  # Icon size relative to the logo size

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

font_path = "./fonts/fa-solid-900.ttf"
font_size = None  # Will be calculated based on the image size

# Processing each image
for filename in os.listdir(input_dir):

    if filename.endswith(".png"):
        logo_path = os.path.join(input_dir, filename)
        logo = Image.open(logo_path)

        # Calculate the icon size based on the logo size
        icon_size = int(min(logo.size) * icon_size_ratio)
        font_size = icon_size
        font = ImageFont.truetype(font_path, font_size)

        # Overlay icons
        for icon in icon_list:
            icon_name = icon["name"]
            icon_unicode = icon["unicode"]

            for color_name, color in [
                ("dark", icon_color_dark),
                ("light", icon_color_light),
            ]:
                # Create a copy of the logo to overlay the icon
                logo_with_icon = logo.copy()
                draw = ImageDraw.Draw(logo_with_icon)

                # Calculate position to center the icon
                text_width = draw.textlength(icon_unicode, font=font)
                text_height = font.size
                position = (
                    0.3 * ((logo.size[0] - text_width) // 2),
                    1.8 * ((logo.size[1] - text_height) // 2),
                )

                # Draw the icon
                draw.text(position, icon_unicode, font=font, fill=color)

                # Save the image
                output_filename = (
                    f"{os.path.splitext(filename)[0]}_{icon_name}_{color_name}.png"
                )
                output_path = os.path.join(output_dir, output_filename)
                logo_with_icon.save(output_path)

        print(f"Processed {filename}")

print("All logos processed successfully.")
