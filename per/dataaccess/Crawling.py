import requests
from bs4 import BeautifulSoup
import os

def download_images(url, folder="images"):
    try:
        # Tạo thư mục để lưu ảnh nếu nó không tồn tại
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Tải nội dung trang web
        response = requests.get(url)
        response.raise_for_status()  # kiểm tra có lỗi khi tải trang không

        # Phân tích cú pháp HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Tìm tất cả các thẻ img trong trang
        imgs = soup.find_all('img')
        print(f"Found {len(imgs)} images")

        jpg_count = 0

        # Tải về từng ảnh
        for img in imgs:
            # Lấy URL của ảnh
            img_url = img.get('src')
            if img_url.endswith('.png'):
                if not img_url.startswith(('http:', 'https:')):
                    img_url = requests.compat.urljoin(url, img_url)

                # Tải ảnh và lưu vào thư mục
                print(f"Downloading {img_url}")
                img_response = requests.get(img_url)
                img_response.raise_for_status()  # kiểm tra có lỗi khi tải ảnh không

                # Lưu ảnh
                img_name = os.path.join(folder, img_url.split('/')[-1])
                with open(img_name, 'wb') as f:
                    f.write(img_response.content)

                jpg_count += 1

        print(f"Downloaded {jpg_count} .jpg images.")
    except Exception as e:
        print(f"An error occurred: {e}")