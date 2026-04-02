from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from taxi.views import index


less_words = settings.STATIC_ROOT
urlpatterns = ([path("",
                     index,
                     name="index")
                ] + static(settings.STATIC_URL, document_root=less_words))

app_name = "taxi"
