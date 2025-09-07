# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class UsersTable(models.Model):
    email = models.TextField(primary_key=True)  # This field type is a guess.
    username = models.TextField(unique=True)  # This field type is a guess.
    password = models.TextField()
    confirm_password = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_table'


class UsersPublic(models.Model):
    email = models.CharField(primary_key=True, max_length=255)   # <-- primary key is email
    username = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_public'


class Enrollments(models.Model):
    user_email = models.ForeignKey(UsersTable, models.DO_NOTHING, db_column='user_email')
    user_name = models.TextField()
    academic_year = models.TextField()
    grade = models.TextField()
    school = models.TextField(blank=True, null=True)
    enrollment_id = models.TextField(primary_key=True)
    current_pct_overall = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    predictive_pct_overall = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    descriptive_overall = models.TextField(blank=True, null=True)
    prescriptive_overall = models.TextField(blank=True, null=True)
    engagement_analysis = models.JSONField(blank=True, null=True)
    strongest_subject = models.TextField(blank=True, null=True)
    weakest_subject = models.TextField(blank=True, null=True)
    subjects_taken = models.TextField(blank=True, null=True)  # This field type is a guess.
    current = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'enrollments'
        unique_together = (('user_email', 'academic_year'),)


class AssessmentsEol(models.Model):
    pk = models.CompositePrimaryKey('enrollment_id', 'subject')
    enrollment = models.ForeignKey(Enrollments, models.DO_NOTHING)
    subject = models.TextField()
    grade = models.TextField()
    assessment_type = models.TextField()
    topic = models.TextField(blank=True, null=True)  # This field type is a guess.
    teachers = models.TextField(blank=True, null=True)  # This field type is a guess.
    obtained_marks = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_marks = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)
    average = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessments_eol'


class AssessmentsFa(models.Model):
    pk = models.CompositePrimaryKey('enrollment_id', 'subject', 'evaluation_criteria')
    enrollment = models.ForeignKey(Enrollments, models.DO_NOTHING)
    subject = models.TextField()
    grade = models.TextField()
    assessment_type = models.TextField()
    month = models.TextField()  # This field type is a guess.
    evaluation_criteria = models.TextField()
    task_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    teachers = models.TextField(blank=True, null=True)  # This field type is a guess.
    student_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    max_score_old = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    count_sdl_t1 = models.IntegerField(blank=True, null=True)
    count_sdl_t2 = models.IntegerField(blank=True, null=True)
    count_sdl_t3 = models.IntegerField(blank=True, null=True)
    count_wt_t1 = models.IntegerField(blank=True, null=True)
    count_wt_t2 = models.IntegerField(blank=True, null=True)
    count_wt_t3 = models.IntegerField(blank=True, null=True)
    count_fawriting_t1 = models.IntegerField(blank=True, null=True)
    count_fawriting_t2 = models.IntegerField(blank=True, null=True)
    count_fawriting_t3 = models.IntegerField(blank=True, null=True)
    count_steam_t1 = models.IntegerField(blank=True, null=True)
    count_steam_t2 = models.IntegerField(blank=True, null=True)
    count_steam_t3 = models.IntegerField(blank=True, null=True)
    count_ia_t1 = models.IntegerField(blank=True, null=True)
    count_ia_t2 = models.IntegerField(blank=True, null=True)
    count_ia_t3 = models.IntegerField(blank=True, null=True)
    current_average_t1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    current_average_t2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    current_average_t3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    current_percentage = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    current_percentage_t1 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    current_percentage_t2 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    current_percentage_t3 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    predicted_percentage = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    predicted_percentage_t1 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    predicted_percentage_t2 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    predicted_percentage_t3 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    descriptive_analysis = models.TextField(blank=True, null=True)
    prescriptive_analysis = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessments_fa'


class AssessmentsSa(models.Model):
    pk = models.CompositePrimaryKey('enrollment_id', 'subject', 'evaluation_criteria')
    enrollment = models.ForeignKey(Enrollments, models.DO_NOTHING)
    subject = models.TextField()
    grade = models.TextField()
    assessment_type = models.TextField()
    month = models.TextField()  # This field type is a guess.
    evaluation_criteria = models.TextField()
    task_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    teachers = models.TextField(blank=True, null=True)  # This field type is a guess.
    student_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    max_score_old = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    count_sa = models.IntegerField(blank=True, null=True)
    count_hye_t1 = models.IntegerField(blank=True, null=True)
    count_hye_t2 = models.IntegerField(blank=True, null=True)
    count_project_t1 = models.IntegerField(blank=True, null=True)
    count_project_t2 = models.IntegerField(blank=True, null=True)
    count_projects_t1 = models.IntegerField(blank=True, null=True)
    count_projects_t2 = models.IntegerField(blank=True, null=True)
    count_december_test = models.IntegerField(blank=True, null=True)
    count_mock = models.IntegerField(blank=True, null=True)
    count_others = models.IntegerField(blank=True, null=True)
    current_average_t1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    current_average_t2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    current_percentage = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    predicted_percentage = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    predicted_percentage_t1 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    predicted_percentage_t2 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    descriptive_analysis = models.TextField(blank=True, null=True)
    prescriptive_analysis = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessments_sa'


class Subjects(models.Model):
    pk = models.CompositePrimaryKey('enrollment_id', 'subject')
    enrollment = models.ForeignKey(Enrollments, models.DO_NOTHING)
    subject = models.TextField()
    grade = models.TextField()
    current_sub_pct = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    predicted_sub_pct = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    descriptive_sub = models.TextField(blank=True, null=True)
    prescriptive_sub = models.TextField(blank=True, null=True)
    current_sub = models.TextField(blank=True, null=True)  # This field type is a guess.
    dates = models.TextField(blank=True, null=True)  # This field type is a guess.
    engagement_analysis = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subjects'


class AssessmentWeights(models.Model):
    pk = models.CompositePrimaryKey('academic_year', 'grade', 'term', 'assessment_type')
    academic_year = models.TextField()
    grade = models.IntegerField()
    term = models.TextField()
    assessment_type = models.TextField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'assessment_weights'
