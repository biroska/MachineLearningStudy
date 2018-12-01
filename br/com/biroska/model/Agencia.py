class Agencia:
    def __init__(self, numero, digito ):
        self.numero = numero
        self.digito = digito

    def __str__(self):
        return 'Ag: %s-%s' % ( self.numero,  self.digito)
