namespace Backend.models
{
    public class Session
    {
        public DateTime? FechaHoraFin { get; set; }
        public DateTime FechaHoraInicio { get; set; }

        public Usuario Usuario { get; set; }

        public Usuario ObtenerLogueado() { return Usuario; }
    }
}
