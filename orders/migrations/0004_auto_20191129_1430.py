
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20191129_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regularpizza',
            name='category',
        ),
        migrations.RemoveField(
            model_name='sicilianpizza',
            name='category',
        ),
    ]
