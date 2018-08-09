from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search_results, name = 'search_results'),
    url(r'^hood/(?P<id>\d+)', views.hood, name='hood'),
    url(r'^business/(?P<hood_id>\d+)', views.business, name='business'),
    url(r'^new/post$', views.new_biz, name='new_biz'),
    url(r'^new/profile$', views.new_profile, name='new-profile'),
    url(r'^biz_in_hood/(?P<neighbourhood_id>\d+)', views.biz_in_hood, name='biz_in_hood'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)