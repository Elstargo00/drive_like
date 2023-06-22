from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import File, Folder
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name="dispatch") # !!! THIS LINE JUST FOR TESTING PURPOSES. DON'T FORGET TO REMOVE !!!
class CreateFolderView(View):
    def post(self, request):
        name = request.POST["name"]
        parent_id = request.POST.get("parent_id")

        if parent_id:
            parent = Folder.objects.get(id=parent_id)
            new_folder = Folder(name=name, parent=parent)
        else:
            new_folder = Folder(name=name)

        new_folder.save()
        return JsonResponse({"message": "Folder created successfully"})

@method_decorator(csrf_exempt, name="dispatch") # !!! THIS LINE JUST FOR TESTING PURPOSES. DON'T FORGET TO REMOVE !!!
class RenameFolderView(View):
    def post(self, request, folder_id):
        new_name = request.POST["name"]
        folder = Folder.objects.get(id=folder_id)
        folder.name = new_name
        folder.save()
        return JsonResponse({"message": "Folder renamed successfully"})

@method_decorator(csrf_exempt, name="dispatch") # !!! THIS LINE JUST FOR TESTING PURPOSES. DON'T FORGET TO REMOVE !!!
class DeleteFolderView(View):
    def post(self, request, folder_id):
        folder = Folder.objects.get(id=folder_id)
        folder.delete()
        return JsonResponse({"message": "Folder deleted successfully"})

@method_decorator(csrf_exempt, name="dispatch") # !!! THIS LINE JUST FOR TESTING PURPOSES. DON'T FORGET TO REMOVE !!!
class UploadFileView(View):
    def post(self, request, folder_id):
        file = request.FILES["file"]
        folder = Folder.objects.get(id=folder_id)
        new_file = File(name=file.name, file=file, parent_folder=folder)
        new_file.save()
        return JsonResponse({"message": "File uploaded successfully"})

@method_decorator(csrf_exempt, name="dispatch") # !!! THIS LINE JUST FOR TESTING PURPOSES. DON'T FORGET TO REMOVE !!!    
class RenameFileView(View):
    def post(self, request, file_id):
        new_name = request.POST["name"]
        file = File.objects.get(id=file_id)
        file.name = new_name 
        file.save()
        return JsonResponse({"message": "File renamed successfully"})

@method_decorator(csrf_exempt, name="dispatch") # !!! THIS LINE JUST FOR TESTING PURPOSES. DON'T FORGET TO REMOVE !!!    
class DeleteFileView(View):
    def post(self, request, file_id):
        file = File.objects.get(id=file_id)
        file.delete()
        return JsonResponse({"message": "File deleted successfully"})