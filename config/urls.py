
from django.contrib import admin
from django.urls import path, include
from home.views import home
from django.conf.urls.static import static
from config import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('forum/', include("pythonbb.urls")),
    path('', include("authentication.urls")),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
