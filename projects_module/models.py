from django.db import models
from django.utils.text import slugify
# Create your models here.


class Skill(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان مهارت")
    image = models.FileField(upload_to="skills/", verbose_name="تصویر مهارت")

    class Meta:
        verbose_name = "مهارت"
        verbose_name_plural = "مهارت‌ها"

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان پروژه")
    url_title = models.SlugField(max_length=200, null=True, blank=True, db_index=True, unique=True, verbose_name="عنوان در URL")
    skill = models.ManyToManyField(Skill, related_name="projects", blank=True, verbose_name="تکنولوژی‌ها",)
    image = models.ImageField(upload_to="projects/", verbose_name="تصویر اصلی پروژه")
    description = models.TextField(verbose_name="توضیحات پروژه")
    start_date = models.DateField(verbose_name="تاریخ شروع پروژه")
    end_date = models.DateField(null=True, blank=True, verbose_name="تاریخ پایان پروژه")
    is_completed = models.BooleanField(default=False, verbose_name="تکمیل شده")
    github_url = models.URLField(blank=True, verbose_name="آدرس گیت‌هاب")
    def save(self, *args, **kwargs):
        self.url_title = slugify(self.title, allow_unicode=True)
        super(Project, self).save(*args, **kwargs)


    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"
        ordering = ["-start_date"]

    def __str__(self):
        return self.title

class ProjectFeature(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="features", verbose_name="پروژه")
    title = models.CharField(max_length=200, verbose_name="عنوان قابلیت")
    icon_name = models.CharField(max_length=200, verbose_name="نام آیکون")
    description = models.TextField(verbose_name="توضیحات قابلیت")

    class Meta:
        verbose_name = "قابلیت پروژه"
        verbose_name_plural = "قابلیت‌های پروژه"

    def __str__(self):
        return f"{self.project.title} - {self.title}"

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="gallery", verbose_name="پروژه")
    image = models.ImageField(upload_to="projects/gallery/", verbose_name="تصویر")
    title = models.CharField(max_length=200, blank=True, verbose_name="عنوان تصویر")

    class Meta:
        verbose_name = "تصویر پروژه"
        verbose_name_plural = "گالری تصاویر پروژه"

    def __str__(self):
        return self.title or f"تصویر پروژه {self.project.title}"

class ProjectChallenge(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="challenges", verbose_name="پروژه")
    challenge = models.TextField(verbose_name="چالش")
    solution = models.TextField(verbose_name="راه‌حل")

    class Meta:
        verbose_name = "چالش پروژه"
        verbose_name_plural = "چالش‌های پروژه"

    def __str__(self):
        return f"{self.project.title} - چالش"