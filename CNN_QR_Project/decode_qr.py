# decode_qr.py - QR Code Decoding Using pyzbar

from pyzbar.pyzbar import decode
import cv2

def decode_qr(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError(f"Image at path {image_path} cannot be read.")
    
    # Decode QR code(s)
    decoded_objects = decode(image)
    
    # Extract and print data from the QR code(s)
    for obj in decoded_objects:
        print(f"Detected QR code: {obj.data.decode('utf-8')}")
        print(f"QR Code type: {obj.type}")
        # Optionally draw the QR code bounding box
        points = obj.polygon
        if len(points) == 4:
            points = [(point.x, point.y) for point in points]
            cv2.polylines(image, [np.array(points, dtype=np.int32)], isClosed=True, color=(0, 255, 0), thickness=2)
    
    # Show the image with QR code detection
    cv2.imshow("QR Code Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    image_path = "path_to_qr_image.jpg"
    decode_qr(image_path)
