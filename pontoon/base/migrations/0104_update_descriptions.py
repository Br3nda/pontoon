# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-19 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import pontoon.base.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0103_bug_1398108_rename_groups_with_duplicate_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locale',
            name='cldr_plurals',
            field=models.CharField(blank=True, help_text='\n        A comma separated list of\n        <a href="http://www.unicode.org/cldr/charts/dev/supplemental/language_plural_rules.html">\n        CLDR plural rules</a>, where 0 represents zero, 1 one, 2 two, 3 few, 4 many, and 5 other.\n        E.g. 1,5\n        ', max_length=11, validators=[pontoon.base.models.validate_cldr], verbose_name='CLDR Plurals'),
        ),
        migrations.AlterField(
            model_name='locale',
            name='direction',
            field=models.CharField(choices=[('ltr', 'left-to-right'), ('rtl', 'right-to-left')], default='ltr', help_text='\n        Writing direction of the script. Set to "right-to-left" if "rtl" value\n        for the locale script is set to "YES" in\n        <a href="https://github.com/unicode-cldr/cldr-core/blob/master/scriptMetadata.json">\n        CLDR scriptMetadata.json</a>.\n        ', max_length=3),
        ),
        migrations.AlterField(
            model_name='locale',
            name='population',
            field=models.PositiveIntegerField(default=0, help_text='\n        Number of native speakers. Find locale code in CLDR territoryInfo.json:\n        https://github.com/unicode-cldr/cldr-core/blob/master/supplemental/territoryInfo.json\n        and multiply its "_populationPercent" with the territory "_population".\n        Repeat if multiple occurrences of locale code exist and sum products.\n        '),
        ),
        migrations.AlterField(
            model_name='locale',
            name='script',
            field=models.CharField(default='Latin', help_text='\n        The script used by this locale. Find it in\n        <a\n        href="http://www.unicode.org/cldr/charts/latest/supplemental/languages_and_scripts.html">\n        CLDR Languages and Scripts</a>.\n        ', max_length=128),
        ),
    ]
