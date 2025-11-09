-- rebuild_ppai.sql
-- Uso: sqlite3 ./PPAI_DATABASE.db < rebuild_ppai.sql
PRAGMA foreign_keys = OFF;
BEGIN;

-- 1) Dropear objetos existentes (genérico, si sabés nombres concretos podés listarlos)
-- DROP VIEW IF EXISTS ...;
-- DROP TRIGGER IF EXISTS ...;
-- DROP INDEX IF EXISTS ...;

-- 2) Dropear tablas (si querés forzar orden explícito, listalas acá)
-- (No listamos manualmente para evitar desincronización; se puede usar el script Python para hacerlo automáticamente.)

COMMIT;
VACUUM;
PRAGMA foreign_keys = ON;

-- 3) Crear estructura
.read schema_ppai.sql
