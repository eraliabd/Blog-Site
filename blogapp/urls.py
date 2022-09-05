from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('login_page/', views.login_page, name='login_page'),
    path('logout_page/', views.logout_page, name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('', views.index, name="index"),
    path('blog/', views.PostListView.as_view(), name='blog'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name="post_detail"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('search/', views.search, name="search"),
    # path('category/<int:pk>', views.category, name="category"),
]