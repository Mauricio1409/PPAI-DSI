namespace Backend.models
{
    public class CambioEstado
    {
        public CambioEstado(DateTime fecha, Estado estado, Empleado empleado)
        {
            Estado = estado;
            Empleado = empleado;
            FechaHoraInicio = fecha;
        }
        public DateTime? FechaHoraFin { get; set; } // Changed to nullable DateTime  
        public DateTime FechaHoraInicio { get; set; }

        public Estado Estado { get; set; }

        public Empleado Empleado { get; set; }

        public void SetFechaHoraFin(DateTime fecha) { FechaHoraFin = fecha; }
        public bool SoActual()
        {
            return FechaHoraFin != null;
        }
    }
}