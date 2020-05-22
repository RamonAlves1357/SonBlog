from django.shortcuts import render

# Create your views here.
def home(request):
    post = Post.object.all()
    return render(request, 'home.html', {'post', posts})