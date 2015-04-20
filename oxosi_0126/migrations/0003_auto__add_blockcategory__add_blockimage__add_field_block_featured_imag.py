# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BlockCategory'
        db.create_table(u'oxosi_0126_blockcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
        ))
        db.send_create_signal(u'oxosi_0126', ['BlockCategory'])

        # Adding model 'BlockImage'
        db.create_table(u'oxosi_0126_blockimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'images', to=orm['oxosi_0126.Block'])),
            ('file', self.gf('mezzanine.core.fields.FileField')(max_length=200)),
        ))
        db.send_create_signal(u'oxosi_0126', ['BlockImage'])

        # Adding field 'Block.featured_image'
        db.add_column(u'oxosi_0126_block', 'featured_image',
                      self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field categories on 'Block'
        m2m_table_name = db.shorten_name(u'oxosi_0126_block_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('block', models.ForeignKey(orm[u'oxosi_0126.block'], null=False)),
            ('blockcategory', models.ForeignKey(orm[u'oxosi_0126.blockcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['block_id', 'blockcategory_id'])


    def backwards(self, orm):
        # Deleting model 'BlockCategory'
        db.delete_table(u'oxosi_0126_blockcategory')

        # Deleting model 'BlockImage'
        db.delete_table(u'oxosi_0126_blockimage')

        # Deleting field 'Block.featured_image'
        db.delete_column(u'oxosi_0126_block', 'featured_image')

        # Removing M2M table for field categories on 'Block'
        db.delete_table(db.shorten_name(u'oxosi_0126_block_categories'))


    models = {
        u'oxosi_0126.block': {
            'Meta': {'ordering': "(u'-publish_date',)", 'object_name': 'Block', '_ormbases': [u'pages.Page']},
            'block_custom_styles': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'block_hover_stay': ('django.db.models.fields.CharField', [], {'default': "u'no'", 'max_length': '5'}),
            'block_html_content': ('django.db.models.fields.TextField', [], {'default': "u'<div>HTML goes here</div>'"}),
            'block_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'block_ratio': ('django.db.models.fields.CharField', [], {'default': "u'block_ratio_22'", 'max_length': '15'}),
            'block_slider_transition_delay': ('django.db.models.fields.IntegerField', [], {'default': "u'2000'"}),
            'block_slider_transition_speed': ('django.db.models.fields.IntegerField', [], {'default': "u'1000'"}),
            'block_slider_transition_type': ('django.db.models.fields.CharField', [], {'default': "u'scrollLeft'", 'max_length': '20'}),
            'block_subtext': ('django.db.models.fields.CharField', [], {'default': "u'some subtext goes here'", 'max_length': '30'}),
            'block_text_font_styles': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'block_type': ('django.db.models.fields.CharField', [], {'default': "u'image'", 'max_length': '10'}),
            'block_video_autostart': ('django.db.models.fields.CharField', [], {'default': "u'no'", 'max_length': '5'}),
            'block_video_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'blocks'", 'blank': 'True', 'to': u"orm['oxosi_0126.BlockCategory']"}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'featured_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'oxosi_0126.blockcategory': {
            'Meta': {'ordering': "(u'title',)", 'object_name': 'BlockCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'oxosi_0126.blockimage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'BlockImage'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'block': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'images'", 'to': u"orm['oxosi_0126.Block']"}),
            'file': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['oxosi_0126']