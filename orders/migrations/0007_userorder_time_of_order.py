
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_userorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='time_of_order',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
