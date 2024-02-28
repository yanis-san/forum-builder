from django.urls import path
from pythonbb.views import index, forum,create_forum, forum_update, forum_delete, thread_index, create_thread , thread_delete,join_forum, message_ban

app_name = "pythonbb"

urlpatterns = [
    path("", index, name="index"),
    path("create/", create_forum, name="create-forum"),
    path("<str:forum_slug>/", forum, name="forum"),
    path("<str:forum_slug>/join/", join_forum, name="join-forum"),
    path("<str:forum_slug>/update/", forum_update, name="forum-update"),
    path("<str:forum_slug>/delete/", forum_delete, name="forum-delete"),
    path("<str:forum_slug>/create/", create_thread, name="create-thread"),
    path("<str:forum_slug>/<str:thread_slug>/", thread_index, name="thread-index"),
    path("<str:forum_slug>/<str:thread_slug>/delete/", thread_delete, name="thread-delete"),
    path("<str:forum_slug>/<str:thread_slug>/delete/<int:message_id>/", message_ban, name="message-ban"),
]
