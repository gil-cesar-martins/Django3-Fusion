import uuid
from django.db import models
from stdimage.models import StdImageField

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    
    class Meta:
        abstract = True;

class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog','Engrenagem'),
        ('lni-stats-up','Gráfico'),
        ('lni-users','Usuários'),
        ('lni-layers','Design'),
        ('lni-mobile','Mobile'),
        ('lni-rocket','Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
    
    def __str__(self):
        return self.servico
    
class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)
    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    
    def __str__(self):
        return self.cargo

class Desenvolvedor(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb':{'width':480, 'height':480, 'crop':True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    
    class Meta:
        verbose_name = 'Desenvolvedor'
        verbose_name_plural = 'Desenvolvedores'
    
    def __str__(self):
        return self.nome
    
class Cliente(Base):
    nome = models.CharField('Nome', max_length=100)
    empresa = models.CharField('Empresa', max_length=100)
    comentario = models.TextField('Comentário', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb':{'width':75, 'height':75, 'crop':True}})
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.nome
    

    

        
        
    
