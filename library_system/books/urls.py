from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'books'
urlpatterns = [
    path('', views.index, name = 'index'),
    #Home Page
    path('home/' ,views.home, name = 'home'),
    #Search page
    path('search_book/' ,views.search_book, name = 'search_book'),
    #Borrow page
    path('borrow/<int:book_id>' ,views.borrow, name = 'borrow'),
    # #Borrowed book page in the profile
    path('requested_book/', views.requested_book, name = 'requested_book'),
    #Returned book page in the profile
    path('remove_book/<int:id>/', views.remove_book, name = 'remove_book'),
    # #Notifications book page in the profile
    path('notifications/', views.notifications, name = 'notifications'),
    #Fines page
    path('returned_book/', views.returned_book, name = 'returned_book'),
    # #Confirm borrow page
    path('confirm_borrow/<int:id>', views.confirm_borrow, name = 'confirm_borrow'),
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)