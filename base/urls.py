from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import base_detail_page


urlpatterns = [

    url(r'^base/(?P<slug>[-\w]+).html$', base_detail_page, name='base_detail_page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
