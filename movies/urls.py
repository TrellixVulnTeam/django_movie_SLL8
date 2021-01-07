from django.urls import path

app_name = "movies"
urlparttners = [
    path('', views.index, name=index)
]