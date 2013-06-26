from django.conf.urls import patterns, url
from gplusacts import views

urlpatterns = patterns("",
    url(r"^$", views.index, name="index"),
    url(r"^page/(?P<pagenum>\d+)$", views.page, name="index"),
)
