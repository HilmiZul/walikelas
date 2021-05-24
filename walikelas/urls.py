from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.leger.views import *
from apps.master.views import *
from apps.master.view_api import *
from rest_framework import routers
from apps.leger import urls as urls_leger
from apps.master import urls as urls_master
from django.contrib.auth.views import LoginView, LogoutView

router = routers.DefaultRouter()
router.register('guru', GuruViewset)
router.register('gurumapel', GuruMapelViewset)
router.register('rombel', RombelViewset)
router.register('siswa', SiswaViewset)
router.register('mapel', MapelViewset)

urlpatterns = [
  path('api/v1/', include(router.urls)),

  path('login/', LoginView.as_view(), name="login"),
  path('logout/', LogoutView.as_view(next_page='login'), name="logout"),

  path('', home, name='home'),

  path('master/', include(urls_master)),

  path('nilai/', include(urls_leger)),

  path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
