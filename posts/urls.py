from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, PostViewSet   # combines the two POST and USER views

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls

# *** BELOW IS THE PREVIOUS CODE WITHOUT USING VIEWSETS ****

#from .views import (UserList,   # this imports views.py
#                    UserDetail,
#                    PostList,
#                    PostDetail)gisr

#urlpatterns = [
#    path('users/', UserList.as_view()),     # user list route
#    path('users/<int:pk>', UserDetail.as_view()),  # single user route (use user number such as 1 to view user)
#    path('<int:pk>/', PostDetail.as_view()),    # single post route (use post ID number to view post)
#    path('posts', PostList.as_view()),   # post list route
#]re