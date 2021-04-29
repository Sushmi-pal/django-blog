from .views import HomePageView
from django.urls import path
from .views import blogpage,authdesc,Create,BlogTry,detailblog,BlogPage,BlogDetail
app_name='landing'
urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    # path('blog/',BlogPage.as_view(),name='blog'),
    path('blog/',blogpage,name='blog'),
    path('desc/<int:user_id>',authdesc,name='desc'),
    # path('detail/<int:pk>',BlogDetail.as_view(),name='detail'),
    path('detail/<int:id>',detailblog,name='detail'),
    path('create/',Create,name='create'),
    path('blogtry/',BlogTry,name='blogtry')

]