# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Imagem.slug'
        db.add_column('galeria_imagem', 'slug', self.gf('django.db.models.fields.SlugField')(db_index=True, default='', max_length=100, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Imagem.slug'
        db.delete_column('galeria_imagem', 'slug')


    models = {
        'armazem.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '100', 'blank': 'True'}),
            'supercategoria': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'subcategorias'", 'null': 'True', 'to': "orm['armazem.Categoria']"})
        },
        'armazem.produto': {
            'Meta': {'object_name': 'Produto'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'produtos'", 'to': "orm['armazem.Categoria']"}),
            'data_cadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_modificacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'preco': ('django.db.models.fields.FloatField', [], {}),
            'publicado': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '100', 'blank': 'True'})
        },
        'galeria.imagem': {
            'Meta': {'object_name': 'Imagem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legenda': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'original': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'principal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'imagens'", 'to': "orm['armazem.Produto']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '100', 'blank': 'True'}),
            'thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['galeria']
