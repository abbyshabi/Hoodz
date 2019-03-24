from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.index,name='home'),
    url(r'^profile',views.profile, name= 'profile'),
    url(r'^update',views.update_profile, name= 'update'),
    url(r'^new_post',views.new_post ,name= 'new_post'),
    url(r'^add/neighbourhood',views.new_project, name= 'add_project'),
]