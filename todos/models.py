from datetime import date

from django.db import models


class Todo(models.Model):
    titulo = models.CharField(
        verbose_name="Título", max_length=100, null=False, blank=False
    )
    data_criacao = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    data_entrega = models.DateField(
        verbose_name="Data de entrega", null=False, blank=False
    )
    data_finalizacao = models.DateField(null=True)

    class Meta:
        ordering = ["data_entrega"]

    def mark_has_complete(self):
        if not self.data_finalizacao:
            self.data_finalizacao = date.today()
            self.save()
