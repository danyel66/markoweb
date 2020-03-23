from django.urls import path
from .views import (index, contact, signupPage, loginPage,
                    logoutPage, CategoryView, ItemDetailView, about)


app_name = 'core'


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('signup/', signupPage, name='signup'),
    path('contact/', contact, name='contact'),
    path('category/', CategoryView.as_view(), name='category'),
    path('product/<slug>/', ItemDetailView.as_view(),
         name='product'),

]
