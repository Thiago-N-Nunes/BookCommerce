from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('Data da Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Livro(Base):
    titulo = models.CharField('Titulo', max_length=100)
    autor = models.CharField('Autor', max_length=100)
    qtd_paginas = models.IntegerField('Paginas')
    descricao = models.CharField('Sinopse', max_length=250)
    preco = models.DecimalField('Preço', max_digits=8,decimal_places=2)
    estoque = models.IntegerField('Estoque')
    capa = StdImageField('imagem', upload_to='ca', variations={'thumb' : {124,124}})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome



# Create your models here.
