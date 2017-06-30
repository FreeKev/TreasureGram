from django.conf.urls import url
from main_app import views
from views import show
from views import post_treasure

urlpatterns = [
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^([0-9]+)/$', views.show, name="show"),
    url(r'^post_url/$', views.post_treasure, name="post_treasure"),
    url(r'^$', views.index),
]
