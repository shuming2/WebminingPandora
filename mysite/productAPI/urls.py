from django.conf.urls import url, include
from rest_framework import routers

from . import views
from .APIviews import *



router = routers.DefaultRouter()
router.register(r'product', ProductViewSet, base_name='product-detail')
urlpatterns = [
    url(r'^$', views.test, name='test'),
    url(r'^updateGroupData$', views.updateGroupData, name='update-group-data'),
    url(r'^updateProductData$', views.updateProductData, name='update-product-data'),

    url(r'^api/collection/$', CollectionListView.as_view(), name='collection-list'),
    url(r'^api/subcategory/$', SubCategoryListView.as_view(), name='subcategory-list'),

    url(r'^api/', include(router.urls))
    # url(r'^api/posts/(?P<post_id>[a-z0-9-]+)/$', PostDetailView.as_view(), name='post-detail'),
    # url(r'^api/author/posts/$', PostsAuthorCanSeeView.as_view(), name='posts-author-can-see'),
    # url(r'^api/author/(?P<author_id>[a-z0-9-]+)/posts/$', AuthorPostsView.as_view(), name='author-posts'),
    # url(r'^api/posts/(?P<post_id>[a-z0-9-]+)/comments/$', CommentView.as_view(), name='comments'),
    #
    # url(r'^api/friendrequest/$', FriendRequestView.as_view(), name='friend-request'),
    #
    # url(r'^api/', include(router.urls)),
    # url(r'^api/author/(?P<author_id>[0-9a-fA-F\-]+)/friends/'r'(?P<friend_id>.*)$', RemoteFriendView.as_view(),
    #     name='remote-friend-checking'),

]

