import requests
import os

# API endpoint
API_URL = "http://localhost:8000/detect/"

# Path to test images folder
TEST_IMAGE_DIR = "test_images"

# Results dictionary
test_results = {}

# List all .jpg images in the folder
image_files = [f for f in os.listdir(TEST_IMAGE_DIR) if f.lower().endswith(".jpg")]

def run_test(image_filename, test_number):
    image_path = os.path.join(TEST_IMAGE_DIR, image_filename)

    if not os.path.exists(image_path):
        print(f"[Test {test_number}] File not found: {image_path}")
        test_results[f"Test {test_number}"] = "Skipped (file not found)"
        return

    # label: "bird_test.jpg" → "bird"
    label = os.path.splitext(image_filename)[0].replace("_test", "")

    with open(image_path, "rb") as f:
        files = {"image": (image_filename, f, "image/jpeg")}
        data = {"label": label}
        response = requests.post(API_URL, files=files, data=data)

    if response.status_code == 200:
        resp = response.json()

        print(f"\n[Test {test_number}] {image_filename} | Label: {label}")

        objects = resp.get("objects", [])

        if not objects:
            print("No objects detected!")
            test_results[f"Test {test_number}"] = "No Match"
            return

        detected_labels = [obj.get("label", label) for obj in objects]
        print("Detected labels:", detected_labels)

        match = any(label in d for d in detected_labels)
        test_results[f"Test {test_number}"] = "Success" if match else "No Match"
    else:
        print(f"[Test {test_number}] API error {response.status_code}")
        print("Error:", response.text)
        test_results[f"Test {test_number}"] = f"API Error {response.status_code}"

# Run all tests
for i, image_file in enumerate(image_files, 1):
    run_test(image_file, i)

# Summary
print("\n Results:")
for test, result in test_results.items():
    print(f"{test}: {result}")
