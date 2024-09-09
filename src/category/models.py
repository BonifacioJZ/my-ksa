import uuid
from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(verbose_name="Nombre",max_length=150,null=False,blank=False)
    description = models.TextField(verbose_name="Descripcion",null=True, blank=True)
    guard_name = models.CharField(verbose_name="Guard Name",max_length=13,blank=False,null=False)
    slug = models.SlugField()
    
    class Meta:
        managed = True
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self) -> str:
        return self.slug
    
    
    
class Sub_Category(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(verbose_name="Nombre",max_length=150,null=False,blank=True)
    slug = models.SlugField()
    category = models.ForeignKey(Category,verbose_name="category",on_delete=models.CASCADE)
    class Meta:
        managed = True
        verbose_name = 'sub_category'
        verbose_name_plural = 'sub_categories'
    
    def __str__(self) -> str:
        return self.slug