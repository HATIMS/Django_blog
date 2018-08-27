from django.conf.urls import url
from myblog.views import stub_view
from myblog.views import list_view
from myblog.views import detail_view
from django.conf.urls import url, include
from rest_framework import routers
from myblog import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.UserViewSet)
router.register(r'categories', views.GroupViewSet)

urlpatterns = [
    url(r'^$', list_view, name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$', detail_view, name="blog_detail"),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]




