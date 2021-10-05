from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name = 'Contact',
            fields = [('id', models.BigAutoField(auto_created=True)),
            ('name', models.CharField(max_length=50)),
            ('email', models.CharField(max_length=200)),
            ('phone', models.IntegerField(blank = True)),
            ('is_favorite', models.TextField(help_text="yes mean's favorite, no mean's not favorite")),
            ],

        ),
    ]