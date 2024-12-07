
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20191129_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='regularpizza',
            name='category_description',
            field=models.TextField(default='pizza description here'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sicilianpizza',
            name='category_description',
            field=models.TextField(default='pizza description here too'),
            preserve_default=False,
        ),
    ]
