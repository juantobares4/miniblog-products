from django.urls import path

from home.views import (
        index_view,
        LogoutView,
        LoginView,
        RegisterView,
        ChangeLanguage

    )

urlpatterns = [
    path(route = '', view = index_view, name = 'index'),
    path(route = 'login/', view = LoginView.as_view(), name = 'login'), # Trae todos los métodos de la clase.
    path(route = 'logout/', view = LogoutView.as_view(), name = 'logout'), # Trae todos los métodos de la clase.
    path(route = 'register/', view = RegisterView.as_view(), name = 'register'),
    path(route = 'change_language/', view = ChangeLanguage.as_view(), name = 'change_language'),


]