"""django_music URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from web_pages.views import basic_web_page
from web_app.views import basic_web_app, dynamic_web_app

apipatterns = [
    url(r'^v1/', include('web_endpoints.urls', namespace='v1')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pages/$', basic_web_page),  # the web_pages app. We call the view's callable function
    # the web_app app.
    url(r'^app/$', basic_web_app),
    url(r'^app/song/$', dynamic_web_app),
    # the web_db app. In this case, we'll include instead of specifying each view
    url(r'^db/', include('web_db.urls', namespace='db')),
    # And finally, our endpoints
    url(r'^api/', include(apipatterns, namespace='api')),
]
