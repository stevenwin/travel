from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='UserInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('astro_sun', models.CharField(max_length=50)),
                ('astro_moon', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
    ]