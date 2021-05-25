from django.shortcuts import render

def post_show(request):
    return render(request, 'blog/blog-post.html')
    