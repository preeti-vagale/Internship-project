import cv2

def decode_message(image_path, original_message_length):
    """Decodes a hidden message from an image."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Error: Could not open or read the image file: {image_path}")

    decoded_message = ""
    index = 0
    height, width, _ = img.shape

    for i in range(height):
        for j in range(width):
            if index < original_message_length:
                decoded_message += chr(img[i, j, 0])  # Read from Blue channel
                index += 1
            else:
                break

    print("Decrypted message:", decoded_message)
    return decoded_message

if __name__ == "__main__":
    encrypted_image_path = r"C:\Users\komal\OneDrive - Manipal University Jaipur\UNI PRITI\ibm internship\encrypted_image.jpg"
    original_message_length = len("Hello, this is a secret!")

    decode_message(encrypted_image_path, original_message_length)
