from django.urls import path
from .views import (
    BoshSahifaView,
    FilmQoshishView,
    FilmlarRoyxatiView,
    JanrBoyichaFilmlarView,
    FilmDetailView,
)
from django.views.generic import RedirectView

urlpatterns = [
    path('', BoshSahifaView.as_view(), name='bosh_sahifa'),
    path('film/qoshish/', FilmQoshishView.as_view(), name='film_qoshish'),
    path('filmlar/', FilmlarRoyxatiView.as_view(), name='filmlar_royxati'),
    path('janr/<str:janr_nomi>/', JanrBoyichaFilmlarView.as_view(), name='janr_boyicha_filmlar'),
    path('film/<int:id>/', FilmDetailView.as_view(), name='film_detail'),
    path('movies/', RedirectView.as_view(pattern_name='filmlar_royxati', permanent=True)),
]
