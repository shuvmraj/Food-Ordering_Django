
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_userorder_delivered'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedCarts',
            fields=[
                ('username', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('cart', models.TextField()),
            ],
        ),
    ]
