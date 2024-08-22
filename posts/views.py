from django.contrib.auth import get_user_model  # imports the user model
from rest_framework import viewsets  # combines the two POST and USER classes
# from rest_framework.views import APIView    # this is used fpr custom logout view / not in book

from .models import Post  # imports Post model
from .permissions import IsAuthorOrReadOnly  # allows only authors to edit/delete posts
from .serializers import (PostSerializer,  # imports the PostSerializer/UserSerializer
                          UserSerializer)  # in serializers.py


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# class CustomLogoutView(APIView): # ERROR!!!!!!!
#    def get(self, request, *args, **kwargs):
#        logout(request)
 #       return Response(status=status.HTTP_204_NO_CONTENT)

#    def post(self, request, *args, **kwargs):
#        logout(request)
 #       return Response(status=status.HTTP_204_NO_CONTENT)

# *** BELOW IS THE PREVIOUS CODE WITHOUT USING VIEWSETS ****
# View of Post List
# class PostList(generics.ListCreateAPIView):
# permissions_classes = (permissions.IsAuthenticated,)    # for permissions
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer


# View of Post Detail
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
# permission_classes = (permissions.IsAuthenticated,)     # for permissions
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# View of the user list
# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# View of the user detail
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = UserSerializer

# YOU CAN CHANGE THE CLASSES INTO VIEWSETS THAT MAKES THE TWO POST AND USER
# CLASSES INTO ONE SEPARATE CLASSES MAKING THE CODE SHORTER. SEE P.161
