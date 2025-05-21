namespace Backend.models
{
    public class SerieTemporal
    {
        public string CondicionAlarma { get; set; }
        public DateTime FechaHoraInicioRegistroMuestras { get; set; }
        public DateTime FechaHoraRegistro { get; set; }
        public double FrecuenciaMuestreo { get; set; }

        public List<MuestraSismica> Muestras { get; set; } = new List<MuestraSismica>();

    }
}