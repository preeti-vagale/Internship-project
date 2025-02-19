import cv2

def encode_message(image_path, secret_message, output_path="encrypted_image.jpg"):
    """Encodes a secret message into an image."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Error: Could not open or read the image file: {image_path}")

    height, width, _ = img.shape

    if len(secret_message) > (height * width):
        raise ValueError("Error: Message too long to encode in this image.")

    index = 0
    for i in range(height):
        for j in range(width):
            if index < len(secret_message):
                img[i, j, 0] = ord(secret_message[index])  # Encode in Blue channel
                index += 1
            else:
                break

    success = cv2.imwrite(output_path, img)
    if success:
        print(f"Message encoded and saved as: {output_path}")
    else:
        print("Error: Failed to save the encrypted image.")

if __name__ == "__main__":
    image_path = r"C:\Users\komal\OneDrive - Manipal University Jaipur\UNI PRITI\ibm internship\wp3539910.jpg"
    output_path = r"C:\Users\komal\OneDrive - Manipal University Jaipur\UNI PRITI\ibm internship\encrypted_image.jpg"
    
    secret_message = "Hello, this is a secret!"
    
    encode_message(image_path, secret_message, output_path)
