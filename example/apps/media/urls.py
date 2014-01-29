from django.conf.urls import patterns, url

from .views import MediaList

urlpatterns = patterns('',
   url(r'admin/media/mediapicker$', MediaList.as_view(), name="admin_media_mediapicker"),
)

