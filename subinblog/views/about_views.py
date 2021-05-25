from django.shortcuts import render

def about_show(request):
    return render(request, 'blog/blog-about.html')
    