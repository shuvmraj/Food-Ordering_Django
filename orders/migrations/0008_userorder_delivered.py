
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_userorder_time_of_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='delivered',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
