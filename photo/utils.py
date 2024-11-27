import os


def get_local_images():
    images = []
    image_dir = 'C:/Users/h_takahashi/tei_app/photoproject/media/images'  # 画像が保存されているディレクトリの正しいパス
    for filename in os.listdir(image_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):  # 複数の拡張子を指定
            images.append({'name': filename, 'url': f'/media/images/{filename}'})
    return images
