from django.db import models
from autoslug import AutoSlugField
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
import uuid
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models import F


# == MODELO PARA PERFIL DE USUÁRIO ==
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='Usuário')
    website = models.URLField(blank=True, null=True)
    bio = models.TextField(max_length=240, blank=True, null=True, verbose_name='Biografia')
    profile_image = models.ImageField(upload_to='foto_de_perfil/', blank=True, null=True, verbose_name='Foto de Perfil')

    # FUNÇÃO PARA PEGAR O NOME COMPLETO DO USUÁRIO
    def __str__(self):
        return self.user.get_full_name()
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
    

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("post_list_by_category", kwargs={"category_slug": self.slug})
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


  
# == MODELO PARA POSTAGENS ==
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = RichTextUploadingField(verbose_name='Conteúdo')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoria')
    image = models.ImageField(upload_to='thumbnail_de_post', verbose_name='Miniatura da Postagem')
    meta_description = models.CharField(max_length=160, default=None, blank=True, verbose_name='Meta Descrição')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False, verbose_name='Publicar')
    highlighted = models.BooleanField(default=False)
    main_01 = models.BooleanField(default=False)
    main_02 = models.BooleanField(default=False)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    
    
    # == CONFIGURAÇÃO DAS VARIÁVEIS PARA SLUG AUTOMÁTICO ==
    slug = AutoSlugField(max_length=255, populate_from='get_slug', unique=True)
    year = models.PositiveIntegerField(editable=False)
    month = models.IntegerField(editable=False)
    
    # == FUNÇÃO PARA GERAR UM SLUG ==
    def get_slug(self):
        date_str = self.created_at.strftime('%Y/%m')
        return f"{slugify(self.title)}"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
            self.year = self.created_at.year
            self.month = self.created_at.month
        super().save(*args, **kwargs)
        
    # == MONITORAR VISUALIÇÃO DE POSTAGENS ==
    views = models.PositiveIntegerField(editable=False, default=0)
    def increase_views(self):
        self.views = F('views') + 1
        self.save(update_fields=['views'])
        
    # == FUNÇÃO PARA CRIAR UMA URL DO SLUG GERADO ==
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"year": self.year, "month": self.month, "slug_url": self.slug})
    
    # PEGAR O THUMBNAIL DA POSTAGEM
    def get_thumbnail_url(self):
        if self.image:
            return self.image.url
        else:
            return None
        
    # RETORNAR O TITULO DA POSTAGEM
    def __str__(self):
        return self.title
    
    # USO DA CLASSE META PARA MANIPULAR A INTERFACE DO MODELO
    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        