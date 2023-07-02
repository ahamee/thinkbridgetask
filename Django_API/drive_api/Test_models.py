# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FifaData(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    photo = models.TextField(db_column='Photo', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nationality = models.TextField(db_column='Nationality', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    flag = models.TextField(db_column='Flag', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    overall = models.BigIntegerField(db_column='Overall', blank=True, null=True)  # Field name made lowercase.
    potential = models.BigIntegerField(db_column='Potential', blank=True, null=True)  # Field name made lowercase.
    club = models.TextField(db_column='Club', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    club_logo = models.TextField(db_column='Club Logo', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    value_field = models.FloatField(db_column='Value(£)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    wage_field = models.FloatField(db_column='Wage(£)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    special = models.BigIntegerField(db_column='Special', blank=True, null=True)  # Field name made lowercase.
    preferred_foot = models.TextField(db_column='Preferred Foot', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    international_reputation = models.FloatField(db_column='International Reputation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    weak_foot = models.FloatField(db_column='Weak Foot', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skill_moves = models.FloatField(db_column='Skill Moves', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_rate = models.TextField(db_column='Work Rate', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    body_type = models.TextField(db_column='Body Type', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    real_face = models.TextField(db_column='Real Face', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    position = models.TextField(db_column='Position', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    jersey_number = models.FloatField(db_column='Jersey Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    joined = models.TextField(db_column='Joined', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    loaned_from = models.TextField(db_column='Loaned From', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contract_valid_until = models.FloatField(db_column='Contract Valid Until', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    height_cm_field = models.FloatField(db_column='Height(cm.)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    weight_lbs_field = models.BigIntegerField(db_column='Weight(lbs.)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    crossing = models.FloatField(db_column='Crossing', blank=True, null=True)  # Field name made lowercase.
    finishing = models.FloatField(db_column='Finishing', blank=True, null=True)  # Field name made lowercase.
    headingaccuracy = models.FloatField(db_column='HeadingAccuracy', blank=True, null=True)  # Field name made lowercase.
    shortpassing = models.FloatField(db_column='ShortPassing', blank=True, null=True)  # Field name made lowercase.
    volleys = models.FloatField(db_column='Volleys', blank=True, null=True)  # Field name made lowercase.
    dribbling = models.FloatField(db_column='Dribbling', blank=True, null=True)  # Field name made lowercase.
    curve = models.FloatField(db_column='Curve', blank=True, null=True)  # Field name made lowercase.
    fkaccuracy = models.FloatField(db_column='FKAccuracy', blank=True, null=True)  # Field name made lowercase.
    longpassing = models.FloatField(db_column='LongPassing', blank=True, null=True)  # Field name made lowercase.
    ballcontrol = models.FloatField(db_column='BallControl', blank=True, null=True)  # Field name made lowercase.
    acceleration = models.FloatField(db_column='Acceleration', blank=True, null=True)  # Field name made lowercase.
    sprintspeed = models.FloatField(db_column='SprintSpeed', blank=True, null=True)  # Field name made lowercase.
    agility = models.FloatField(db_column='Agility', blank=True, null=True)  # Field name made lowercase.
    reactions = models.FloatField(db_column='Reactions', blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    shotpower = models.FloatField(db_column='ShotPower', blank=True, null=True)  # Field name made lowercase.
    jumping = models.FloatField(db_column='Jumping', blank=True, null=True)  # Field name made lowercase.
    stamina = models.FloatField(db_column='Stamina', blank=True, null=True)  # Field name made lowercase.
    strength = models.FloatField(db_column='Strength', blank=True, null=True)  # Field name made lowercase.
    longshots = models.FloatField(db_column='LongShots', blank=True, null=True)  # Field name made lowercase.
    aggression = models.FloatField(db_column='Aggression', blank=True, null=True)  # Field name made lowercase.
    interceptions = models.FloatField(db_column='Interceptions', blank=True, null=True)  # Field name made lowercase.
    positioning = models.FloatField(db_column='Positioning', blank=True, null=True)  # Field name made lowercase.
    vision = models.FloatField(db_column='Vision', blank=True, null=True)  # Field name made lowercase.
    penalties = models.FloatField(db_column='Penalties', blank=True, null=True)  # Field name made lowercase.
    composure = models.FloatField(db_column='Composure', blank=True, null=True)  # Field name made lowercase.
    marking = models.FloatField(db_column='Marking', blank=True, null=True)  # Field name made lowercase.
    standingtackle = models.FloatField(db_column='StandingTackle', blank=True, null=True)  # Field name made lowercase.
    slidingtackle = models.FloatField(db_column='SlidingTackle', blank=True, null=True)  # Field name made lowercase.
    gkdiving = models.FloatField(db_column='GKDiving', blank=True, null=True)  # Field name made lowercase.
    gkhandling = models.FloatField(db_column='GKHandling', blank=True, null=True)  # Field name made lowercase.
    gkkicking = models.FloatField(db_column='GKKicking', blank=True, null=True)  # Field name made lowercase.
    gkpositioning = models.FloatField(db_column='GKPositioning', blank=True, null=True)  # Field name made lowercase.
    gkreflexes = models.FloatField(db_column='GKReflexes', blank=True, null=True)  # Field name made lowercase.
    best_position = models.TextField(db_column='Best Position', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    best_overall_rating = models.FloatField(db_column='Best Overall Rating', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    release_clause_field = models.FloatField(db_column='Release Clause(£)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year_joined = models.BigIntegerField(db_column='Year_Joined', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fifa_data'


class TblDetail1(models.Model):
    name = models.CharField(db_column='Name', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_detail1'
