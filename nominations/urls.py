from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("voter/", views.voter, name="voter"),
    path("voterdata/", views.voterdata, name="voterdata"),
    path("nominees/", views.nominees, name="nominees"),
    path("nomineesdata/", views.nomineesdata, name="nomineesdata"),
    path("position/", views.position, name="position"),
    path("dashboard/<int:studentid>/", views.dashboard, name='dashboard'),
    path("voted/<int:studentid>/", views.voted, name="voted"),
    path('voting/<int:studentid>/<int:nomineeID>/', views.voting, name='voting'),
    path('profile/<int:studentid>/', views.profile_view, name='profile')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
