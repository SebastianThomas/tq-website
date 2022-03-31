from django.urls import path

from survey import views

app_name = 'survey'
urlpatterns = [
    path('', views.overview, name='overview'),
    path('<int:survey_id>/', views.survey_view, name='survey'),
    path('<int:survey_id>/results/', views.survey_results, name='results'),
    path('<int:survey_id>/<url_key>/', views.survey_view, name='survey_with_key'),
]
