from datetime import datetime, timedelta
from Entitys.AlcanceSismo import AlcanceSismo
from Entitys.AlcanceSismo import AlcanceSismo
from Entitys.ClasificacionSismo import ClasificacionSismo
from Entitys.CambioEstado import CambioEstado
from Entitys.Estado import Estado
from Entitys.DetalleMuestraSismica import DetalleMuestraSismica
from Entitys.MuestraSismica import MuestraSismica
from Entitys.OrigenDeGeneracion import OrigenDeGeneracion
from Entitys.SerieTemporal import SerieTemporal
from Entitys.EstacionSismologica import EstacionSismologica
from Entitys.Empleado import Empleado
from Entitys.EventoSismico import EventoSismico
from Entitys.AnalistaSismos import AnalistaSismos
from Entitys.Usuario import Usuario
from Entitys.Sesion import Sesion

# -----------------------------
# Datos para AnalistaSismos
# -----------------------------
analista1 = AnalistaSismos("Juan", "Rodriguéz", 1)

# -----------------------------
# Datos para Usuario
# -----------------------------
usuario1 = Usuario("Juan", "1234", analista1)

# -----------------------------
# Datos para Sesión
# -----------------------------

sesion1 = Sesion("sesion_001", usuario1, datetime.now(), datetime.now() + timedelta(hours=1))

# -----------------------------
# Datos para AlcanceSismo
# -----------------------------

alcances_sismo = [
    AlcanceSismo("Leve", "Alcance local"),
    AlcanceSismo("Moderado", "Alcance regional"),
    AlcanceSismo("Fuerte", "Alcance nacional"),
    AlcanceSismo("Devastador", "Alcance internacional")
]

# -----------------------------
# Datos para ClasificacionSismo
# -----------------------------
clasificaciones_sismo = [
    ClasificacionSismo(0, 70, "Superficial"),
    ClasificacionSismo(71, 300, "Intermedio"),
    ClasificacionSismo(301, 700, "Profundo")
]

# -----------------------------
# Datos para CambioEstado
# -----------------------------
# Estados disponibles
estado_detectado = Estado("Detectado", "EventoSismico")
estado_confirmado = Estado("Confirmado" , "EventoSismico")
estado_finalizado = Estado("Finalizado", "EventoSismico")
estado_bloqueado = Estado("Bloqueado", "EventoSismico")

estados = [estado_finalizado, estado_detectado, estado_finalizado, estado_bloqueado]

# Fechas de ejemplo
ahora = datetime.now()

cambios_estado = [
    CambioEstado(ahora - timedelta(days=3), estado_detectado, analista1, ahora - timedelta(days=2),),
    CambioEstado(ahora - timedelta(days=2), estado_confirmado, analista1, ahora - timedelta(days=1)),
    CambioEstado(ahora - timedelta(days=1), estado_finalizado, analista1)
]

# -----------------------------
# Detalles de muestras sísmicas
# -----------------------------
detalles_muestra = [
    DetalleMuestraSismica(150),
    DetalleMuestraSismica(200),
    DetalleMuestraSismica(175)
]

# -----------------------------
# Muestras sísmicas
# -----------------------------
fecha_muestra1 = datetime.now() - timedelta(hours=2)
fecha_muestra2 = datetime.now() - timedelta(hours=1)

muestras_sismicas = [
    MuestraSismica(fecha_muestra1, detalles_muestra[0]),
    MuestraSismica(fecha_muestra2, detalles_muestra[1])
]

# -----------------------------
# Serie temporal de muestras
# -----------------------------
fecha_inicio_registro = datetime.now() - timedelta(hours=3)
fecha_registro = datetime.now()


# -----------------------------
# Estaciones Sismológicas
# -----------------------------
estaciones_sismologicas = [
    EstacionSismologica(
        codigoEstacion=101,
        documentoCertificacionAdq=123456,
        fechaSolicitudCertificacion=datetime(2023, 5, 20),
        latitud=-31.4167,
        longitud=-64.1833,
        nombre="Estación Córdoba",
        numeroCertificacionAdquisicion=78910
    ),
    EstacionSismologica(
        codigoEstacion=102,
        documentoCertificacionAdq=654321,
        fechaSolicitudCertificacion=datetime(2022, 11, 15),
        latitud=-34.6037,
        longitud=-58.3816,
        nombre="Estación Buenos Aires",
        numeroCertificacionAdquisicion=98765
    )
]
# -----------------------------
# Datos SerieTemporal
# -----------------------------

series_temporales = [
    SerieTemporal(
        condicionAlarma=0,
        fechaHoraInicioRegistroMuestras=fecha_inicio_registro,
        fechaHoraRegistro=fecha_registro,
        frecuenciaMuestreo=100,
        muestraSismica=muestras_sismicas,
        estacionSismologica=estaciones_sismologicas[0]
    ),
    SerieTemporal(
        condicionAlarma=1,
        fechaHoraInicioRegistroMuestras=fecha_inicio_registro + timedelta(hours=1),
        fechaHoraRegistro=fecha_registro,
        frecuenciaMuestreo=200,
        muestraSismica=muestras_sismicas,
        estacionSismologica=estaciones_sismologicas[1]
    )
]


origen_generacion = OrigenDeGeneracion("Generación Natural", "Origen natural de los sismos")

# -----------------------------
# Eventos sismicos
# -----------------------------
eventosSismicos = [
            EventoSismico(datetime(2023, 5, 21, 12, 0, 0), 5.0, -34.0, -58.0, cambios_estado, Estado("PendienteRevision","EventoSismico"), clasificaciones_sismo[1], alcances_sismo[1], origen_generacion, series_temporales),
            EventoSismico(datetime(2023, 10, 2, 14, 30, 0), 4.5, -35.0, -59.0, cambios_estado, Estado("PendienteRevision","EventoSismico"), clasificaciones_sismo[2], alcances_sismo[2], origen_generacion, series_temporales),
            EventoSismico(datetime(2025, 10, 1, 10, 0, 0), 5.5, -34.5, -58.5, cambios_estado, Estado("PendienteRevision","EventoSismico"), clasificaciones_sismo[1], alcances_sismo[3], origen_generacion, series_temporales),
            EventoSismico(datetime(2023, 10, 3, 16, 0, 0), 6.0, -36.0, -60.0, cambios_estado, Estado("PendienteRevision","EventoSismico"), clasificaciones_sismo[2], alcances_sismo[0], origen_generacion, series_temporales),
            EventoSismico(datetime(2023, 10, 4, 18, 0, 0), 7.0, -37.0, -61.0, cambios_estado, Estado("PendienteRevision","EventoSismico"), clasificaciones_sismo[1], alcances_sismo[1], origen_generacion, series_temporales),
            EventoSismico(datetime(2023, 10, 5, 20, 0, 0), 5.7, -38.0, -62.0, cambios_estado, Estado("PendienteRevision","EventoSismico"), clasificaciones_sismo[0], alcances_sismo[3], origen_generacion, series_temporales),
        ]


# -----------------------------
# Empleados (sin atributos definidos)
# -----------------------------
empleados = [
    Empleado(),
    Empleado()
]
