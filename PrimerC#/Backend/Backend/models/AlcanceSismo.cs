namespace Backend.models
{
    public class AlcanceSismo
    {
        public string Descripcion { get; set; }
        public string Nombre { get; set; }

        public string GetNombre() { return Nombre; }
    }
}