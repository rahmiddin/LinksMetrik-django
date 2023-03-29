from django.urls import path
from .views import UploadLinks, DomainView


urlpatterns = [
    path('visited_links', UploadLinks.as_view(), name='upload-links'),
    path('visited_domains', DomainView.as_view, name='get_visited_domains')
]
