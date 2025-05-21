namespace Backend.models
{
    public class EstacionSismologica
    {
        public string CodigoEstacion { get; set; }
        public string DocumentoCertificacionAct { get; set; }
        public DateTime FechaSolicitudCertificacion { get; set; }
        public double Latitud { get; set; }
        public double Longitud { get; set; }
        public string Nombre { get; set; }
        public int NumeroCertificacionAdquisicion { get; set; }

        public string GetNombre() { return Nombre; }
    }
}