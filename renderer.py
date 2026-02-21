import cv2

# Character sets
SHADING = "@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvu/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
BLOCKS = "█▓▒░ "

def render_ascii(frame, width=100, mode="normal"):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if mode == "edge":
        gray = cv2.Canny(gray, 80, 150)

    gray = cv2.resize(gray, (width, int(width * 0.5)))

    chars = SHADING if mode != "blocks" else BLOCKS
    scale = len(chars)

    ascii_img = "\n".join(
        "".join(chars[pixel * scale // 256] for pixel in row)
        for row in gray
    )

    return ascii_img