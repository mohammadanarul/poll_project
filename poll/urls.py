from django.urls import path
from poll.views import (
    home_page_view,
    poll_list_page_view,
    vote_page_view,
    poll_details_page_view
)

urlpatterns = [
    path('', home_page_view, name='home'),
    path('poll-list', poll_list_page_view, name='poll-list'),
    path('vote/<int:pk>/', vote_page_view, name='vote'),
    path('poll-detials/<int:pk>/', poll_details_page_view, name='detials'),
]
