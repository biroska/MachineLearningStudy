from br.com.biroska.model.Agencia import Agencia

class Conta:

    def __init__(self, agencia, agDigito, numero, digito, cliente ):
        self.numero = numero
        self.digito =  digito
        self.cliente = cliente
        self.agencia = Agencia(agencia, agDigito)

    def __str__(self):
        return 'Cliente: %s CC: %s-%s' % ( self.cliente, self.numero,  self.digito)

print( Conta( '1', '2', '1','2','3')     )
print( Agencia('7984','3') )