import os
import uuid
from typing import Dict, Union


def rename_post_img_video(instance, filename: str) -> str:
    """
    Rename an uploaded file to a unique name using UUID and organize it into subdirectories based on the instance's ID to prevent large directory listings.
    """
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4()}.{ext}'

    # Organize files into subdirectories based on the instance's ID
    return os.path.join('posts', str(instance.id), new_filename)




#Upload preset for cloudinary

UPLOAD_PRESET = "sharehub"

upload_preset_config = {
    "upload_preset": UPLOAD_PRESET,
    "cloud_name": "sharehub",
    "api_key": "856165385862893",
    "api_secret": "bN7eBdQZJo4aZZ0k7uJHbI1e_Rg",
    "folder": "sharehub",
    "resource_type": "auto",
    "overwrite": True,
    "notification_url": "https://webhook.site/7d0a6e4a-4d7d-4e6d-8c7d-4e6d8c7d",
    "tags": "sharehub",
    "use_filename": True,
    "unique_filename": False,
    "eager": [
        {"width": 300, "height": 300, "crop": "pad", "audio_codec": "none"},
        {"width": 160, "height": 100, "crop": "crop", "gravity": "south", "audio_codec": "none"}
    ],
    "eager_async": True,
    "eager_notification_url": "https://webhook.site/7d0a6e4a-4d7d-4e6d-8c7d-4e6d8c7d",
    "type": "upload"
}

def get_comment_data(comment: Dict[str, Union[str, int]]) -> Dict[str, Union[str, int]]:
    return {
        "id": comment["id"],
        "content": comment["content"],
        "author": comment["author"],
        "created_at": comment["created_at"],
        "updated_at": comment["updated_at"],
        "post_id": comment["post_id"],
    }
