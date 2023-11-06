from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.urls import reverse
# Create your models here.

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_length=10, decimal_places=2, max_digits=20)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField('Изображение', upload_to='shrekproject/')


    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, default=None)

    @admin.display(description='Дата создания')
    def created_data(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color: green; font_weight; bold;'>Сегодня в {}</span>", created_time
            )
        return self.created_at.strftime('%d:%m:%Y в %H:%M:%S')

    @admin.display(description='Дата обновления')
    def updated_data(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color: orange; font_weight; bold;'>Сегодня в {}</span>", updated_time
            )
        return self.created_at.strftime('%d:%m:%Y в %H:%M:%S')




    class Meta():
        db_table = 'advertisements'

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'

    def get_absolute_url(self):
        return reverse('adv-detail', kwargs={'pk': self.pk})