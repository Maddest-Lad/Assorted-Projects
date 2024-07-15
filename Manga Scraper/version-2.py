import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageOps
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import tempfile
import os
from urllib.parse import urlparse

def download_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        content_type = response.headers['Content-Type']
        if 'image' in content_type:
            return Image.open(BytesIO(response.content))
        else:
            print(f"URL {url} did not point to an image. Content-Type: {content_type}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None

def optimize_image(image):
    # Check if image is in LA mode and convert to RGB
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Resize image to a maximum width of 900 pixels while maintaining aspect ratio
    max_width = 900
    if image.width > max_width:
        image = ImageOps.contain(image, (max_width, int(max_width * image.height / image.width)))
    
    # Compress image using JPEG format with quality 85
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_img_file:
        image.save(temp_img_file, format='JPEG', quality=85)
        temp_img_file_path = temp_img_file.name

    optimized_image = Image.open(temp_img_file_path)
    return optimized_image, temp_img_file_path

def save_images_as_pdf(images, pdf_filename):
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter

    for img in images:
        img, temp_img_file_path = optimize_image(img)
        c.drawImage(temp_img_file_path, 0, 0, width, height)
        c.showPage()

    c.save()

def get_image_urls_and_next_chapter(current_url):
    try:
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract image URLs
        image_tags = soup.find_all('img', src=True)
        image_urls = []
        min_width = 500  # Define a minimum width for manga images
        for img in image_tags:
            parsed_url = urlparse(img['src'])
            file_ext = os.path.splitext(parsed_url.path)[1].lower()
            if file_ext in ['.jpg', '.jpeg', '.png', '.webp']:
                image_urls.append(img['src'])

        
        # Extract next chapter URL
        next_link_tag = soup.find('div', class_='nav-next').find('a', href=True)
        next_chapter_url = next_link_tag['href'] if next_link_tag else None
        
        return image_urls, next_chapter_url
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {current_url}: {e}")
        return [], None

def main(start_url):
    current_url = start_url
    chapter = 1

    while current_url:
        images = []
        image_urls, next_chapter_url = get_image_urls_and_next_chapter(current_url)
        
        for image_url in image_urls:
            image = download_image(image_url)
            if image and image.width > 500: # 500px, Minimum Manga Panel Size
                images.append(image)
        
        if images:
            pdf_filename = f"chapter-{chapter}.pdf"
            save_images_as_pdf(images, pdf_filename)
            print(f"Chapter {chapter} saved as {pdf_filename}")
        else:
            print(f"No images found for Chapter {chapter}")

        if not next_chapter_url:
            break

        current_url = next_chapter_url
        chapter += 1

if __name__ == "__main__":
    start_url = "https://www.chainsaw-man-manga.online/manga/chainsaw-man-chapter-1/"
    main(start_url)
