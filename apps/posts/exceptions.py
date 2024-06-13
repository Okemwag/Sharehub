from rest_framework import status
from rest_framework.exceptions import APIException


class PostDoesNotExist(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Post does not exist.'
    default_code = 'not_found'
    
    
class PostAlreadyExists(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Post already exists.'
    default_code = 'bad_request'
    
    
class AlreadyLikedPost(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Post already liked.'
    default_code = 'bad_request'
    
    

    
    
