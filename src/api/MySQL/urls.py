from django.conf.urls import include, url
from django.contrib import admin
from users.user import user
from users.views import login_message
from users.log_in_out import user_login, user_logout
from src.api.MySQL.views.itemview import item
from src.api.MySQL.views.bidview import bid




urlpatterns = [
                url('^', include('django.contrib.auth.urls')),
                url(r'^admin/', include(admin.site.urls)),
                url(r'^user/', user),
                url(r'^login_message/', login_message),
                url(r'^user_login/', user_login),
                url(r'^user_logout/', user_logout),
                url(r'^item/', item),
                url(r'^bid/', bid),
                ]
