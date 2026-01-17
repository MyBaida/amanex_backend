from django.urls import path
from .views import*

urlpatterns = [
    path('categories/', category_list),
    path('categories/<int:pk>/', category_detail),
    path('categories/create/', category_create),
    path('categories/<int:pk>/update/', category_update),
    path('categories/<int:pk>/delete/', category_delete),

    path('products/', product_list),
    path('products/<int:pk>/', product_detail),
    path('products/<int:category_id>/category/', product_list_by_category),
    path('products/create/', product_create),
    path('products/<int:pk>/update/', product_update),
    path('products/<int:pk>/delete/', product_delete),

    path('products/best-sellers/', best_seller_products),

    path("variants/", variant_list),
    path('variants/create/', product_variant_create),
    path('variants/<int:pk>/', product_variant_detail),
    path('variants/<int:pk>/update/', product_variant_update),
    path('variants/<int:pk>/delete/', product_variant_delete),

    path('jobs/', job_list),
    path('jobs/<int:pk>/', job_detail),
    path('jobs/create/', job_create),
    path('jobs/<int:pk>/toggle/', toggle_job),
    path('jobs/<int:pk>/update/', job_update),
    path('jobs/<int:pk>/delete/', job_delete),

    path('story-video/', our_story_video),
    path('story-video/update/', update_our_story_video),

    path('mission-video/', our_mission_video),
    path('mission-video/update/', update_our_mission_video),

]
