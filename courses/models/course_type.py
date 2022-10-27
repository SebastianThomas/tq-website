from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from parler.models import TranslatableModel, TranslatedFields


class CourseType(TranslatableModel):
    styles = models.ManyToManyField('Style', related_name='course_types', blank=True)
    level = models.IntegerField(default=None, blank=True, null=True)
    couple_course = models.BooleanField(default=True)

    translations = TranslatedFields(
        title=models.CharField(
            verbose_name='[TR] Title', max_length=64, blank=False,
            help_text="This will be the title shown for all courses of this type."),
        subtitle=models.CharField(
            verbose_name='[TR] Subtitle', max_length=128, blank=True, null=True,
            help_text="A short teaser, that is displayed below the title for more information."),
        description=HTMLField(
            verbose_name='[TR] Description', blank=True, null=True,
            help_text="This text is added to the description of each course instance.")
    )

    def format_styles(self) -> str:
        return ', '.join(map(str, self.styles.all()))

    format_styles.short_description = "Styles"

    def __str__(self) -> str:
        return self.title
