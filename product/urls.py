from . import views
from django.conf.urls import url

app_name = 'product'

urlpatterns = [

    # /product/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /product/123
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /product/register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # /product/account/
    url(r'^account/$', views.account, name='account'),
    # /product/user/123
    url(r'^user/(?P<pk>[0-9]+)/$', views.AccountUpdateView.as_view(), name='account-update'),
    # /product/123/cart/
    url(r'^(?P<product_id>[0-9]+)/cart/$', views.purchase, name='purchase'),
    # /product/purchase_history/
    url(r'^user/(?P<user_id>[0-9]+)/purchase_history/$', views.PurchaseHistory, name='purchase-history'),
    # /user/login/
    url(r'^user/login/$', views.UserLoginView.as_view(), name='login'),
    # /user/logout/
    url(r'^logout/$', views.user_logout, name='logout'),
    # /change_password/
    url(r'^password/$', views.change_password, name='change-password'),
]

