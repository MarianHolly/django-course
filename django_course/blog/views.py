from django.shortcuts import render

posts = [
    { 'author': 'John', 'title': 'Hello World', 'content': 'This is my first post', 'date': '2022-01-01' },
    { 'author': 'Jane', 'title': 'Goodbye World', 'content': 'This is my last post', 'date': '2022-01-02' },
]

def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

