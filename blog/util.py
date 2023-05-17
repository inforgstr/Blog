from .models import Post

def list_post():
    return [str(x) for x in Post.objects.all()]
