from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True, auto_created=True)

    class Meta:
        abstract = True


class Lead(BaseModel):
    first_name = models.CharField(null=True, max_length=265)
    last_name = models.CharField(null=True, max_length=265)
    mobile = models.CharField(null=True, max_length=265)
    email = models.CharField(null=True, max_length=265)
    location_type = models.CharField(null=True, max_length=265)
    location_string = models.CharField(null=True, max_length=265)
