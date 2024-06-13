import os
from celery import shared_task
from PIL import Image
from django.conf import settings
from django.utils import timezone

@shared_task
def resize_images(image_path: str, image_name: str, sizes: list) -> None:
    """
    Resize an image to a smaller size.
    """
    image = Image.open(image_path)
    for size in sizes:
        resized_image = image.resize(size, Image.ANTIALIAS)
        resized_image_path = os.path.join(
            settings.MEDIA_ROOT, 
            f"{os.path.splitext(image_path)[0]}_{size[0]}x{size[1]}.{image.format.lower()}"
        )
        resized_image.save(resized_image_path)
        
        
@shared_task
def delete_image(image_path: str) -> None:
    """
    Delete an image.
    """
    os.remove(image_path)
    
    
@shared_task
def clean_up_old_files() -> None:
    """
    Delete old files.
    """
    now = timezone.now()
    for root, dirs, files in os.walk(settings.MEDIA_ROOT):
        for file in files:
            file_path = os.path.join(root, file)
            file_modified_time = timezone.datetime.fromtimestamp(os.path.getmtime(file_path))
            if (now - file_modified_time).days > settings.MEDIA_FILE_MAX_AGE:
                os.remove(file_path)
    