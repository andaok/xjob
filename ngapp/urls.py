from django.conf.urls import url
from ngapp import views

app_name = "ngapp"

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^ng/(?P<id>[\w\-]+)/$',views.get_ng_info,name="ng"),
    url(r'^upstream/(?P<ng_name>.*)/(?P<vip>.*)/(?P<upstream_name>.*)/$',views.get_upstream_info,name="upstream"),
]