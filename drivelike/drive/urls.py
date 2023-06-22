from django.urls import path
from .views import (CreateFolderView, RenameFolderView,
                    DeleteFolderView, UploadFileView,
                    RenameFileView, DeleteFileView)

urlpatterns = [
    path("folder/create/", CreateFolderView.as_view(), name="create_folder"),
    path("folder/<int:folder_id>/rename/", RenameFolderView.as_view(), name="rename_folder"),
    path("folder/<int:folder_id>/delete/", DeleteFolderView.as_view(), name="delete_folder"),
    path("file/<int:folder_id>/upload/", UploadFileView.as_view(), name="upload_file"),
    path("file/<int:file_id>/rename/", RenameFileView.as_view(), name="rename_file"),
    path("file/<int:file_id>/delete/", DeleteFileView.as_view(), name="delete_file"),
]