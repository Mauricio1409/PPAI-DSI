namespace Backend.models
{
    public class MuestraSismica
    {
        public DateTime FechaHoraMuestra { get; set; }

        public List<DetalleMuestraSismica> Detalles { get; set; } = new List<DetalleMuestraSismica>();

        public object ObtenerDatos() 
        {
            return new
            {
                FechaHoraMuestra = FechaHoraMuestra,
                Detalles = Detalles.Select(d => new
                {
                    valor = d.Valor
                })

            };
        }
    }
}