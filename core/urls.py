from django.urls import path
from .views import index, about, business, contact, catview, ItemDetailView


app_name = 'core'


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('business/', business, name='business'),
    path('contact/', contact, name='contact'),
    path('category/', catview, name='category'),
    path('product/<slug>/', ItemDetailView.as_view(),
         name='product'),

]
