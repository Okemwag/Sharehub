from typing import Dict, Union


def get_comment_data(comment: Dict[str, Union[str, int]]) -> Dict[str, Union[str, int]]:

    return {
        'id': comment['id'],
        'content': comment['content'],
        'author': comment['author'],
        'created_at': comment['created_at'],
        'updated_at': comment['updated_at'],
        'post_id': comment['post_id']
    }
