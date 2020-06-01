from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Item
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

app_name = 'core'


# view for homepage
def index(request):
    return render(request, 'core/index.html')


# view for business page
def business(request):
    return render(request, 'core/business.html')


# view for about page
def about(request):
    return render(request, 'core/about.html')


# view for product categories
# class CategoryView(ListView):
#     model = Item
#     context_object_name = 'items'
#     template_name = 'core/category.html'
#     # paginate_by = 1
#
#     def get_queryset(self):
#         queryset = {
#             'animals': Item.objects.all().filter(category='A'),
#             'crops': Item.objects.all().filter(category='C'),
#             'services': Item.objects.all().filter(category='S')
#         }
#         return queryset


def catview(request):

    animals = Item.objects.all().filter(category='A')
    crops = Item.objects.all().filter(category='C')
    services = Item.objects.all().filter(category='S').order_by('-id')
    # paginator = Paginator(services, 1)
    #
    # page = request.GET.get('page')
    # try:
    #     page_obj = paginator.page(page)
    # except PageNotAnInteger:
    #     page_obj = paginator.page(1)
    # except EmptyPage:
    #     page_obj = paginator.page(paginator.num_pages)
    #
    # print(page_obj.paginator.count)
    # print(page_obj.paginator.num_pages)
    # page_obj = paginator.get_page(page)
    return render(request, 'core/category.html', {'animals': animals,
                                                  'crops': crops,
                                                  'services': services,
                                                  })


# view for single product page
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'core/product.html'


# view for contact page
def contact(request):
    return render(request, 'core/contact.html')
