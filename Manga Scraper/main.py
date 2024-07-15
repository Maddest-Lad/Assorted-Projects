import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import tempfile
import os

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

def save_images_as_pdf(images, pdf_filename):
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter

    for img in images:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_img_file:
            img.convert('RGB').save(temp_img_file, format='JPEG')
            temp_img_file_path = temp_img_file.name
            c.drawImage(temp_img_file_path, 0, 0, width, height)
            c.showPage()

    c.save()

def get_next_chapter_url(current_url):
    try:
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        next_link_tag = soup.find('div', class_='next-post').find('a')
        return next_link_tag['href'] if next_link_tag else None
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {current_url}: {e}")
        return None

def main(start_url):
    current_url = start_url
    chapter = 126

    while current_url:
        images = []
        page = 1
        while True:
            image_url = f"https://cdn.readkakegurui.com/file/cdnpog/sousou-no-frieren/chapter-{chapter}/{page}.webp"
            image = download_image(image_url)
            if image:
                images.append(image)
                page += 1
            else:
                break

        if images:
            pdf_filename = f"sousou-no-frieren-chapter-{chapter}.pdf"
            save_images_as_pdf(images, pdf_filename)
            print(f"Chapter {chapter} saved as {pdf_filename}")
        else:
            print(f"No images found for Chapter {chapter}")

        current_url = get_next_chapter_url(current_url)
        chapter += 1

if __name__ == "__main__":
    start_url = "https://sousou-no-frieren.com/manga/sousou-no-frieren-chapter-1/"
    main(start_url)