from django.contrib import admin
from django.urls import path,include
import blog.views
import account.urls
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name = "home"),
    path('blog/<int:blog_id>',blog.views.detail,name = "detail"),
    path('blog/new', blog.views.new, name = "new"),
    path('blog/create', blog.views.create, name = "create"),
    path('blog/edit/<int:blog_id>',blog.views.edit, name = "edit"),
    path('blog/update/<int:blog_id>',blog.views.update, name = "update"),
    path('blog/delete/<int:blog_id>',blog.views.delete, name= "delete"),
    path('account/',include(account.urls)),
    path('blog/commenting/<int:blog_id>', blog.views.commenting, name = 'commenting'),
    path('blog/like/<int:blog_id>',blog.views.like, name = 'like'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
#urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) #위와 똑같은 방법이다.
