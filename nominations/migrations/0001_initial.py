# Generated by Django 4.2 on 2023-07-01 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nomination',
            fields=[
                ('nomineeID', models.IntegerField(primary_key=True, serialize=False)),
                ('session', models.IntegerField(default=0)),
                ('year', models.IntegerField(null=True)),
                ('n_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('position', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('studentid', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=12)),
                ('student_email', models.EmailField(max_length=254)),
                ('student_password', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votedate', models.DateTimeField()),
                ('nomineeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nominee_votes', to='nominations.nomination')),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_votes', to='nominations.voter')),
            ],
        ),
        migrations.AddField(
            model_name='nomination',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nominations.position'),
        ),
    ]
