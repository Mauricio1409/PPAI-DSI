namespace Backend.models
{
    public class Estado
    {
        public string Ambito { get; set; }
        public string NombreEstado { get; set; }

        public bool SosAmbitoEvento() 
        {
            return Ambito == "Evento";
        }
        public bool SosBloqueado() 
        {
            return NombreEstado == "Bloqueado";
        }
        public bool SosPendienteRevision() 
        {
            return NombreEstado == "PendienteRevision";
        }
        public bool SosRechazado() 
        {
            return NombreEstado == "Rechazado";
        }
    }
}