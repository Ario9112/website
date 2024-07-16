from django.db import models
from django.utils import timezone
# Create your models here.   
      
class Catagory(models.Model):

    title = models.CharField(max_length=200,verbose_name='titulo')
    slug = models.SlugField(max_length =100,unique=True )
    status = models.BooleanField()
    position = models.IntegerField()

    class Meta:
        verbose_name="Categoria" 
        ordering = ['position']



class Article(models.Model):
    STATUS_CHOICES = (
        ("p","publicado") ,   
        ("d" ,"draft"),
    )
    title = models.CharField(max_length=200,verbose_name='titulo')
    slug = models.SlugField(max_length =100,unique=True )
    catagory = models.ManyToManyField(Catagory, verbose_name="categoria")
    description = models.TextField(verbose_name='descricao')
    #img = models.ImageField(upload_to='images', null=True)
    img_url = models.CharField(max_length=200,blank=True, null=True,verbose_name='imagem')
    published = models.DateField(default=timezone.now,verbose_name='publicado')
    created = models.DateField(auto_now_add=True,verbose_name="criado")
    updated = models.DateField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, null=True)
    #test = models.CharField(max_length=1, null=True, blank=True)
    
    class Meta:
        verbose_name="Artigo" 



    def __str__(self):
        return self.title
        