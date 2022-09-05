from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, SendMessage, Category
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.core.mail import send_mail
#Register
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Register
# Admin: adminerali
def login_required_decorator(func):
    return login_required(func, login_url='blogapp:login_page')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('blogapp:login_page')

def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect('blogapp:index')
    return render(request, 'login.html')

class SignUpView(CreateView):
    form_class =UserCreationForm
    success_url = reverse_lazy("blogapp:login_page")
    template_name = "signup.html"

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog.html'


@login_required_decorator
def index(request):
    queryset = Post.published.all()
    queryset1 = Post.published.all()[:2]
    queryset2 = Post.published.all()[:5]
    cats = Category.objects.all()

    context = {
        "posts": queryset,
        "posts1": queryset1,
        "posts2": queryset2,
        'categories': cats,
    }
    return render(request, "index.html", context)

@login_required_decorator
def about(request):
    return render(request, "about.html")

# def contact(request):
#     return render(request, "contact.html")

# def post_detail(request):
#     return render(request, "post-details.html")

@login_required_decorator
def post_detail(request, year, month, day, slug):
    queryset = Post.published.all()
    queryset1 = Post.published.all()
    post = get_object_or_404(Post, slug=slug,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)
    if request.POST:
        comment = Comment()
        comment.name = request.POST.get('name', '')
        comment.email = request.POST.get('email', '')
        comment.subject = request.POST.get('subject', '')
        comment.body = request.POST.get('message', '')
        comment.post = post
        comment.save()

    return render(request, 'post-details.html',
                  {'posts': post,
                   'comments': comments,
                   "last_posts": queryset,
                   "categories": queryset1,
                   })

@login_required_decorator
def contact(request):
    if request.POST:
        model = SendMessage()
        model.name = request.POST.get('name', '')
        model.email = request.POST.get('email', '')
        model.subject = request.POST.get('subject', '')
        model.message = request.POST.get('message', '')
        model.save()
    return render(request, 'contact.html')

@login_required_decorator
def search(request):
    query = request.GET['q']

    if not query or query.isspace():
        messages.error(request, 'Please refine your search query...')
        return redirect("blogapp:blog")

    search_results = Post.objects.filter(Q(title__icontains=query) | Q(small__icontains=query) | Q(body__icontains=query))

    context = {
        'search_results': search_results,
        'query': query
    }
    return render(request, 'search.html', context)


# def category(request):
#     queryset = Category.objects.all()
#     print(queryset)
#     return render(request, 'blog.html', {'categories': queryset})