from django.urls import path

from .views import NoteList, NoteDetails


urlpatterns = [
    path('<int:pk>/', NoteDetails.as_view()),
    path('', NoteList.as_view()),
]
