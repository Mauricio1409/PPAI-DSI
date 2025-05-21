namespace Backend.models
{
    public class ClasificacionSismo
    {
        public int KmProfundidadDesde { get; set; }
        public int KmProfundidadHasta { get; set; }
        public string Nombre { get; set; }

        public string GetNombre() { return Nombre; }
    }
}