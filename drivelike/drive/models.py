from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="files/")
    parent_folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name="files")


    def __str__(self):
        return self.name