from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    """
    displays list of posts
    :param request:
    :return: HttpResponse with rendered text (normally HTML code)
    """
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})


def post_detail(request, id):
    """
    displays a single post with given id - or in case of exception raises 404 page
    :param request:
    :param id: id of the post (should really be changed as it shadows a built-in name)
    :return: returns HttpResponse with rendered text (normally HTML code)
    :get_object_or_404: shortcut to display an object or HTTP404(not found) exception.
    """
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)

    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
