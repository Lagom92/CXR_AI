from django.conf import settings

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Xray',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='img/%Y%m%d')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('prediction', models.CharField(blank=True, max_length=100, null=True)),
                ('heatmap', models.ImageField(blank=True, null=True, upload_to='heat/%Y%m%d')),
                ('plot', models.ImageField(blank=True, null=True, upload_to='plot/%Y%m%d')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
