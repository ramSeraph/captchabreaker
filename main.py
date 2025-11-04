from PIL import Image
import captchabreaker

if __name__ == '__main__':
    # This is an example of how to use the captchabreaker package.
    # You need to have a captcha image file (e.g., captcha.png) in the same directory.
    try:
        img = Image.open("sample.png")
        text = captchabreaker.solve(img)
        print(f"Predicted text: {text}")
    except FileNotFoundError:
        print("Error: captcha.png not found. Please provide a captcha image.")
