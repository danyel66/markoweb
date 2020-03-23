from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from .models import Item
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

app_name = 'core'


# view for homepage
def index(request):
    return render(request, 'core/index.html')


# view for aboutpage
def about(request):
    return render(request, 'core/about.html')


# view for product categories
class CategoryView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'core/category.html'
    # paginate_by = 1

    def get_queryset(self):
        queryset = {
            'animals': Item.objects.all().filter(category='A'),
            'crops': Item.objects.all().filter(category='C')
        }
        return queryset

# def category(request):
#     queryset_list = {
#                 'animals': Item.objects.filter(category='A'),
#                 'crops': Item.objects.filter(category='C')
#             }
#     paginator = Paginator(queryset_list, 1)
#
#     page = request.GET.get('page')
#     try:
#         queryset = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         queryset = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         queryset = paginator.page(paginator.num_pages)
#
#     context = {
#         'object': queryset,
#         'title':  'List'
#     }
#
#     return render(request, 'core/category.html', context)


# view for single product page
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'core/product.html'


# view for contact page
def contact(request):
    return render(request, 'core/contact.html')


# view for login page
def loginPage(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            p1 = len(password)
            user = auth.authenticate(request, username=username, password=p1)

            if user is not None:
                auth.login(request, user)
                return redirect('core:index')
            else:
                messages.info(request, 'Username or password is incorrect')
                return redirect('core:login')
        else:
            return render(request, 'core/login.html')
    else:
        return render(request, 'core/index.html')


# view for signup page
def signupPage(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            p1 = len(password1)
            p2 = len(password2)

            if p1 == p2 and p1 >= 8:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Already Exist.')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Address Already Exist.')
                else:
                    user = User.objects.create_user(username=username, email=email, password=p1)
                    user.save()
                    messages.info(request, 'Congrats!! Account created for ' + username)
                    return redirect('core:login')
            elif p1 == p2 and p1 < 8:
                messages.info(request, 'This password is too short. It must contain at least 8 characters.')
                return redirect('core:signup')
            else:
                messages.info(request, 'Passwords do not match. Please input the correct passwords.')
                return redirect('core:signup')
            return redirect('core:signup')

        else:
            return render(request, 'core/signup.html')
    else:
        return render(request, 'core/index.html')


# view for logout
def logoutPage(request):
    auth.logout(request)
    return redirect('account_login')


# def password_reset(request):
#     return render(request, 'core/password_reset.html')
#
#
# def password_reset_done(request):
#     return render(request, 'core/password_reset_done.html')
#
#
# def password_reset_confirm(request):
#     return render(request, 'core/password_reset_confirm.html')
