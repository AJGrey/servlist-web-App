# Generated by Django 4.2.5 on 2023-09-09 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('business_id', models.AutoField(primary_key=True, serialize=False)),
                ('business_name', models.CharField(max_length=100)),
                ('business_type', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=5000)),
                ('location', models.CharField(max_length=50)),
                ('email_contact', models.EmailField(max_length=100)),
                ('phone_contact', models.CharField(max_length=20)),
                ('status', models.IntegerField(choices=[(0, 'inactive'), (1, 'active')])),
                ('date_created', models.DateField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'verbose_name_plural': 'Businesses',
                'db_table': 'businesses',
                'managed': True,
            },
        ),
    ]
