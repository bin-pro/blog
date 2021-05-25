from django.shortcuts import render

def list_show(request):
    return render(request, 'blog/blog-list.html')
    