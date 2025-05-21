namespace Backend.models
{
    public class Sismografo
    {
        public DateTime FechaAdquisicion { get; set; }
        public int IdentificadorSismografo { get; set; }
        public int NumeroSerie { get; set; }

        public EstacionSismologica Estacion { get; set; }

        public List<SerieTemporal> serieTemporales { get; set; }
    }
}
