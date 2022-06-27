#asociado a cada estado, una regla
#actualizar estado
#MAQUINA EXPENDEDORA CON 5 ESTADOS
#Estados: sin-moneda, con-moneda, a1-servida, a2-servida, a3-servida
#Acciones: pedir-moneda, pedir-codigo, esperar.
#Percepciones: moneda, a1, a2, servida.

REGLAS ={ 'sin-moneda': 'pedir-moneda',
          'con-moneda': 'pedir-codigo',
          'a1-servida': 'esperar',
          'a2-servida': 'esperar',
          'a3-servida': 'esperar'}

MODELO = {('sin-moneda', 'pedir-moneda', 'moneda'): 'con-moneda',
          ('con-moneda', 'pedir-codigo', 'a1'): 'a1-servida',
          ('con-moneda', 'pedir-codigo', 'a2'): 'a2-servida',
          ('con-moneda', 'pedir-codigo', 'a3'): 'a3-servida',
          ('a1-servida', 'esperar', 'servida'): 'sin-moneda',
          ('a2-servida', 'esperar', 'servida'): 'sin-moneda',
          ('a3-servida', 'esperar', 'servida'): 'sin-moneda'}

class AgenteReactivoBasadoModelos:
    
   def __init__(self, modelo,estado_inicial='', reglas, accion_inicial=''):
       #Agente racional de tipo reactivo basado en modelo.
       self.modelo = modelo
       self.reglas = reglas
       self.estado_inicial = estado_inicial
       self.accion_inicial = accion_inicial
       self.accion = None
       self.estado = self.estado_inicial
       self.ulti_accion = self.accion_inicial


    
    def actuar(self, percepcion):
        #Actua segun la percepcion, devolviendo una accion
        if not percepcion:
            return self.accion_inicial
        clave = (self.estado, self.ulti_accion, percepcion)
        if clave not in self.modelo.keys():
            self.accion = None
            self.estado = self.estado_inicial
            self.ulti_accion = self.accion_inicial
            return self.accion_inicial
        self.estado = self.modelo[clave]
        if self.estado not in self.reglas.keys():
            self.accion = None
            self.estado = self.estado_inicial
            self.ulti_accion = self.accion_inicial
            return self.accion_inicial
        accion = self.reglas[self.estado]
        self.ulti_accion = accion
        return accion


print("..Agente Reactivo Basado en Modelos: Maquina Expendedora..")
expendedora = AgenteReactivoBasadoModelos(MODELO, REGLAS, 'sin-moneda', 'pedir-moneda')
percepcion = input("Indicar percepcion: ")
while percepcion:
    accion = expendedora.actuar(percepcion)
    print(accion)
    percepcion = input("Indicar Percepcion: ")

