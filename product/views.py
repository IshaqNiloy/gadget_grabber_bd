from django.views import generic
from .models import Product, User, Purchase
from .forms import UserForm, UserLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.shortcuts import get_object_or_404
import datetime
from django.contrib import messages


class IndexView(generic.ListView):
    template_name = 'product/index.html'

    def get_queryset(self):
        return Product.objects.all()


class DetailView(generic.DetailView):
    model = Product
    template_name = 'product/detail.html'
        #return render(request, template_name, {'pk': pk})


def purchase(request, product_id):
    if get_object_or_404(User, pk=request.user.id).is_authenticated:
        template_name = 'product/detail.html'
        object = Purchase()
        product_object = get_object_or_404(Product, pk=product_id)

        object.user = get_object_or_404(User, pk=request.user.id)
        object.purchase_date = datetime.datetime.now()
        object.user_name = get_object_or_404(User, pk=request.user.id).username
        object.user_address = get_object_or_404(User, pk=request.user.id).address
        object.user_phone = get_object_or_404(User, pk=request.user.id).phone
        object.product_name = get_object_or_404(Product, pk=product_id).name
        object.quantity = request.POST['product_quantity']
        object.unit_price = get_object_or_404(Product, pk=product_id).price
        index_of_comma_in_price = object.unit_price.index(',')
        total_price = int(object.unit_price[:index_of_comma_in_price] + object.unit_price[index_of_comma_in_price+1:-3]) * int(object.quantity)
        object.total_price = str(total_price) + 'BDT'

        object.save()
        messages.success(request, 'Product(s) added to your cart!')
        return render(request, template_name, {'product': product_object})
    else:
        return render(request, 'product/login.html')


def PurchaseHistory(request, user_id):
    template_name = 'product/purchase_history.html'
    purchase = get_object_or_404(User, pk=user_id).purchase_set.all()
    return render(request, template_name, {'purchase_list': purchase})



class UserFormView(View):
    form_class = UserForm
    template_name = 'product/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('product:account')

        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'product/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(None)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'product/index.html')

        messages.error(request, 'Invalid Credentials! Try Again.')
        return render(request, self.template_name, {'form': form})


def user_logout(request):
    logout(request)
    return redirect('product:index')


class AccountUpdateView(generic.UpdateView):
    model = User
    template_name = 'product/update_form.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address', 'city', 'post_code']


def change_password(request):
    template_name = 'product/change_password_form.html'
    if request.method == 'GET':
        return render(request, template_name)
    else:
        if request.POST['password'] == request.POST['confirm_password']:
            get_object_or_404(User, pk=request.user.id).set_password(request.POST['password'])
            messages.success(request, 'Password Changed Successfully!')
            return redirect('product:change-password')
        else:
            messages.error(request, 'Passwords Do Not Match! Try Again.')
            return redirect('product:change-password')


def account(request):
    template_name = 'product/account.html'
    return render(request, template_name)


