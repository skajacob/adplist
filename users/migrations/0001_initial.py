# Generated by Django 3.2.13 on 2022-06-12 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('rating', models.FloatField(blank=True, default=0, null=True)),
                ('reviews_count', models.IntegerField(default=0)),
                ('first_name', models.CharField(max_length=30, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last_name')),
                ('location', models.CharField(choices=[('mexico', 'MEXICO'), ('colombia', 'COLOMBIA'), ('peru', 'PERU'), ('chile', 'CHILE'), ('brazil', 'BRAZIL')], help_text='format: required, max-100', max_length=100, verbose_name='The Place where you live like')),
                ('employer', models.CharField(help_text='format: required, max-100', max_length=100, verbose_name='Your employer')),
                ('user_type', models.CharField(choices=[('mentor', 'Mentor'), ('member', 'Member')], help_text='format: required, max-40', max_length=40, verbose_name='User type')),
                ('title', models.CharField(help_text='format: required, max-100', max_length=100, verbose_name='Your title')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
