from django.urls import path
from . import views
urlpatterns = [
    path("login/",views.login_view, name = "login"),
    path("logout/",views.logout_view, name = "logout"),
    path("register/",views.register_view, name = "register"),
]
#urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) #위와 똑같은 방법이다.
