"""awaards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as viewauth

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index, name="home"),
    url(r'^search/', views.search_results, name="search"),
    url(r'^profile/(\d+)', views.profile, name="profile"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', viewauth.logout, {"next_page": '/index'}),
    url(r'^project/project_id/(\d+)', views.project, name="project"),
    url(r'^new/project/$', views.new_project, name="new_project"),
    url(r'^update/profile/$', views.update_profile, name="update_profile"),
    url(r'^api/profileinfo/$', views.ProfileDetails.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)