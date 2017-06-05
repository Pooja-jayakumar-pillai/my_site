from django.conf.urls import url

from blog.views import home,view_post
from django.conf.urls.static import static
from mysite import settings

urlpatterns = [
  url(r'^$', home,name="home"),
    url(r'^(?P<id>[0-9]+)/$',view_post,name="post")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
