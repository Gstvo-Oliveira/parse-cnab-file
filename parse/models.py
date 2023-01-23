from django.db import models


class TypesOfTransactions(models.IntegerChoices):
    DEBITO = 1, "Débito"
    BOLETO = 2, "Boleto"
    FINANCIAMENTO = 3, "Financiamento"
    CREDITO = 4, "Crédito"
    EMPRESTIMO = 5, "Recebimento Empréstimo"
    VENDAS = 6, "Vendas"
    TED = 7, "Recebimento TED"
    DOC = 8, "Recebimento DOC"
    ALUGUEL = 9, "Aluguel"


class ParseCnab(models.Model):
    type_of_transaction = models.IntegerField(choices=TypesOfTransactions.choices)
    date = models.CharField(max_length=8)
    value = models.CharField(max_length=10)
    CPF = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.CharField(max_length=6)
    owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)

    file = models.FileField(upload_to='uploads/')

    class Meta:
        ordering = ['id']


    