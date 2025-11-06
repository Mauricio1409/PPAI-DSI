from abc import ABC

class Estado(ABC):
    def __init__(self, nombre: str, ambito : str):
        self._nombre = nombre
        self._ambito = ambito

    def esAmbito(self, ambito : str):
        if self.ambito == ambito:
            return True
        return False

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevoNombre: str):
        self._nombre = nuevoNombre
    @property
    def ambito(self):
        return self._ambito

    @ambito.setter
    def ambito(self, nuevoAmbito : int):
        self._ambito = nuevoAmbito

    def __str__(self):
        return (f"Estado: {self.nombre}")
    
    def adquirirDatos(self):
        """
        Método para adquirir datos del evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'adquirirDatos' no permitida en estado: {self.nombre}")
        return False
    
    def revisar(self):
        """
        Método para revisar el evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'revisar' no permitida en estado: {self.nombre}")
        return False
    
    def confirmarRevision(self):
        """
        Método para confirmar la revisión del evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'confirmarRevision' no permitida en estado: {self.nombre}")
        return False
    
    def registrarAutomatico(self):
        """
        Método para registrar automáticamente el evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'registrarAutomatico' no permitida en estado: {self.nombre}")
        return False
    
    def anular(self):
        """
        Método para anular el evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'anular' no permitida en estado: {self.nombre}")
        return False
    
    def controlarTiempo(self):
        """
        Método para controlar el tiempo del evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'controlarTiempo' no permitida en estado: {self.nombre}")
        return False
    
    def confirmar(self):
        """
        Método para confirmar el evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'confirmar' no permitida en estado: {self.nombre}")
        return False
    
    def derivar(self):
        """
        Método para derivar el evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'derivar' no permitida en estado: {self.nombre}")
        return False
    
    def rechazar(self):
        """
        Método para rechazar el evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'rechazar' no permitida en estado: {self.nombre}")
        return False
    
    def registrarPendientesCierre(self):
        """
        Método para registrar el evento como pendiente de cierre.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'registrarPendientesCierre' no permitida en estado: {self.nombre}")
        return False
    
    def cerrar(self):
        """
        Método para cerrar el evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'cerrar' no permitida en estado: {self.nombre}")
        return False

