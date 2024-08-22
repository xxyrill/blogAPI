from django.contrib import admin
from django.urls import include, path
# from rest_framework.documentation import include_docs_urls
# from .views import CustomLogoutView     # this is used for custom logout view / not in book

from django.urls import re_path     # schema documentation
from rest_framework import permissions     # schema documentation
from drf_yasg.views import get_schema_view  # for API schema
from drf_yasg import openapi     # schema documentation



# schema_view = get_schema_view(title='Blog API')     # used to view all the project API endpoints
# NEW schema documentation
schema_view = get_schema_view(
   openapi.Info(
      title="Blog Project API",
      default_version='v1',
      description="This is the list of the all your project API endpoints"
                  " and response schemas.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="xyrillariel@gmail.com"),
      license=openapi.License(name="No license"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),    # admin route
    path('api/v1/', include('posts.urls')),     # app route
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # rest framework login page route
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')),   # rest framework auth route
    path('api/v1/dj_rest_auth/registration/',
         include('dj_rest_auth.registration.urls')),   # route for user registration
#    path('docs/', include_docs_urls(title='Blog API')),
#    path('schema', schema_view),    # http://127.0.0.1:8000/schema
#    path('api-auth/logout/', CustomLogoutView.as_view(), name='custom_logout'), # ERROR!!!!!!!!!!
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),   #
         name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),   # route that lists all your API endpoints: http://127.0.0.1:8000/swagger/
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),   # route that list all your response schema: http://127.0.0.1:8000/redoc
         name='schema-redoc'),
]



# explanation of v1: Flexibility for Changes: When you make significant
# updates to your API, not all users (consumers) can update their applications
# immediately to use the new version. By versioning your APIs, you can
# continue to support the old version (e.g., v1) while rolling
# out the new version (e.g., v2).