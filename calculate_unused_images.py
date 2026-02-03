import os
import re

IMAGE_DIR = '/home/king/Documents/devops-blog/src/assets/images'
SRC_DIR = '/home/king/Documents/devops-blog/src'

def get_images():
    images = set()
    for f in os.listdir(IMAGE_DIR):
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg')):
            images.add(f)
    return images

def get_used_images():
    used_images = set()
    # Regex to capture filename.ext
    # We look for any word characters followed by dot and extension
    pattern = re.compile(r'[\w-]+\.(?:png|jpg|jpeg|gif|webp|svg)', re.IGNORECASE)
    
    for root, dirs, files in os.walk(SRC_DIR):
        for file in files:
            # Skip checking the image directory itself to avoiding self-referencing if we were just grepping names
            # But the user content is in src/data/blog. 
            # We want to find references IN TEXT files.
            # So we should probably skip binary files or just try to read everything as text and ignore errors.
            filepath = os.path.join(root, file)
            
            # Skip the images directory itself from being SEARCHED for content
            if os.path.abspath(root) == os.path.abspath(IMAGE_DIR):
                continue

            try:
                with open(filepath, 'r', errors='ignore') as f:
                    content = f.read()
                    matches = pattern.findall(content)
                    used_images.update(matches)
            except Exception as e:
                pass
                
    return used_images

def main():
    available = get_images()
    used = get_used_images()
    
    unused = available - used
    
    print("UNUSED IMAGES:")
    for img in sorted(list(unused)):
        print(img)

if __name__ == "__main__":
    main()
