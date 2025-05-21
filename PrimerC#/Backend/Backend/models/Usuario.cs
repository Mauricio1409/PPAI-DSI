namespace Backend.models
{
    public class Usuario
    {
        public string Contrasenia { get; set; }
        public string Nombre { get; set; }

        public Empleado Empleado { get; set; }

        public Empleado GetLogueado() { return Empleado; }
    }
}
