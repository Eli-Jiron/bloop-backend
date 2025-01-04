from django.urls import path
from apps.Users.views import RolView, UserRolesView, UsersView


urlpatterns = [
    path('', UsersView.as_view(), name='users_list'),
    path('roles/', RolView.as_view(), name='roles_list'),
    path('user-roles/', UserRolesView.as_view(), name='user_roles_list')
]