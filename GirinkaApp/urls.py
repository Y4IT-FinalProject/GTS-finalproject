#file urls configurations
from django.conf import settings
from django.conf.urls.static import static
#end of file configuration

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from .views import HomeView

app_name = "GirinkaApp"
urlpatterns = [
	path('', HomeView.as_view(), name="HomeView"),
    path('announcement/', views.AdAnnouncement, name="AdAnnouncement"),
    path('announce-uploaded/', views.announce_list, name="announce_list"),
    path('login1/', views.login1, name="login1"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login")
	
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)