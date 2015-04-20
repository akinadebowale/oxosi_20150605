# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Block.block_video_autostart'
        db.alter_column(u'oxosi_0126_block', 'block_video_autostart', self.gf('django.db.models.fields.CharField')(max_length=5))

        # Changing field 'Block.block_hover_stay'
        db.alter_column(u'oxosi_0126_block', 'block_hover_stay', self.gf('django.db.models.fields.CharField')(max_length=5))

    def backwards(self, orm):

        # Changing field 'Block.block_video_autostart'
        db.alter_column(u'oxosi_0126_block', 'block_video_autostart', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Block.block_hover_stay'
        db.alter_column(u'oxosi_0126_block', 'block_hover_stay', self.gf('django.db.models.fields.BooleanField')())

    models = {
        u'oxosi_0126.block': {
            'Meta': {'ordering': "('-publish_date',)", 'object_name': 'Block', '_ormbases': [u'pages.Page']},
            'block_custom_styles': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'block_hover_stay': ('django.db.models.fields.CharField', [], {'default': "'no'", 'max_length': '5'}),
            'block_html_content': ('django.db.models.fields.TextField', [], {'default': "'<div>HTML goes here</div>'"}),
            'block_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'block_ratio': ('django.db.models.fields.CharField', [], {'default': "'block_ratio_22'", 'max_length': '15'}),
            'block_slider_transition_delay': ('django.db.models.fields.IntegerField', [], {'default': "'2000'"}),
            'block_slider_transition_speed': ('django.db.models.fields.IntegerField', [], {'default': "'1000'"}),
            'block_slider_transition_type': ('django.db.models.fields.CharField', [], {'default': "'scrollLeft'", 'max_length': '20'}),
            'block_subtext': ('django.db.models.fields.CharField', [], {'default': "'some subtext goes here'", 'max_length': '30'}),
            'block_text_font_styles': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'block_type': ('django.db.models.fields.CharField', [], {'default': "'image'", 'max_length': '10'}),
            'block_video_autostart': ('django.db.models.fields.CharField', [], {'default': "'no'", 'max_length': '5'}),
            'block_video_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
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