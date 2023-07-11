from django.urls import path
# from .views import (CreateFolderView, RenameFolderView,
#                     DeleteFolderView, UploadFileView,
#                     RenameFileView, DeleteFileView)

from . import views 

urlpatterns = [
    # For the forms and views
    # path("folder/create/", CreateFolderView.as_view(), name="create_folder"),
    # path("folder/<int:folder_id>/rename/", RenameFolderView.as_view(), name="rename_folder"),
    # path("folder/<int:folder_id>/delete/", DeleteFolderView.as_view(), name="delete_folder"),
    # path("file/<int:folder_id>/upload/", UploadFileView.as_view(), name="upload_file"),
    # path("file/<int:file_id>/rename/", RenameFileView.as_view(), name="rename_file"),
    # path("file/<int:file_id>/delete/", DeleteFileView.as_view(), name="delete_file"),
    path("api/folders/", views.FolderListCreate.as_view()),
    path("api/folders/<int:pk>/", views.FolderRetrieveUpdateDestroy.as_view()),
    path("api/files/", views.FileListCreate.as_view()),
    path("api/files/<int:pk>/", views.FileListCreate.as_view()),
    path("api/files/<int:pk>/", views.FileRetrieveUpdateDestroy.as_view()),
]