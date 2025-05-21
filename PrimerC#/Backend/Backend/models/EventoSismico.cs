namespace Backend.models
{
    public class EventoSismico
    {
        public int Id { get; set; }
        public DateTime FechaHoraFin { get; set; }
        public DateTime FechaHoraOcurrencia { get; set; }
        public double LatitudEpicentro { get; set; }
        public double LongitudEpicentro { get; set; }
        public double LatitudHipocentro { get; set; }
        public double LongitudHipocentro { get; set; }
        public double ValorMagnitud { get; set; }

        public Estado estado { get; set; }
        public List<CambioEstado> cambioEstados { get; set; } = new List<CambioEstado>();
        public List<SerieTemporal> seriesTemporales { get; set; } = new List<SerieTemporal>();
        public MagnitudRichter Magnitud { get; set; }
        public OrigenDeGeneracion Origen { get; set; }
        public AlcanceSismo AlcanceSismo { get; set; }
        public ClasificacionSismo ClasificacionSismo { get; set; }

        public List<List<double>> GetUbicacion()
        {
            List<List<Double>> coordebadas = new List<List<double>>();
            coordebadas.Add(GetCoordenadasEpicentro());
            coordebadas.Add(GetCoordenadasHipocentro());
            return coordebadas;
        }

        public List<double> GetCoordenadasEpicentro()
        {
            List<double> coordenadas = new List<double>();
            coordenadas.Add(LatitudEpicentro);
            coordenadas.Add(LongitudEpicentro);
            return coordenadas;  
        }
        public List<double> GetCoordenadasHipocentro()
        {
            List<double> coordenadas = new List<double>();
            coordenadas.Add(LatitudHipocentro);
            coordenadas.Add(LongitudHipocentro);
            return coordenadas;
        }

        public bool EsPendienteRevision()
        {
            return estado.SosPendienteRevision();
        }
        public void RegistrarBloqueado() { }
        public void Revisar() { }
    }
}
