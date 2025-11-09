#!/usr/bin/env python3
import sqlite3
from pathlib import Path

# ===============================
# CONFIGURACIÓN DE RUTAS (ajusta PROJECT_ROOT según tu repo local si lo necesitas)
# ===============================
PROJECT_ROOT = Path(__file__).resolve().parent.parent  # .../rebuild_database/.. = raíz del proyecto
DB_PATH = PROJECT_ROOT / "infrastructure" / "database" / "PPAI_DATABASE.db"
SCHEMA_PATH = PROJECT_ROOT / "rebuild_database" / "schema_ppai.sql"  # usa tu schema existente

def _prefetch_names(cur, obj_type):
    return [row[0] for row in cur.execute(
        "SELECT name FROM sqlite_master WHERE type=? AND name NOT LIKE 'sqlite_%';", (obj_type,)
    ).fetchall()]

def drop_all(cur):
    """Elimina todos los objetos del schema sin romper el cursor de iteración."""
    cur.execute("PRAGMA foreign_keys=OFF;")
    try:
        # Importante: prefetchear nombres antes de empezar a dropear
        triggers = _prefetch_names(cur, "trigger")
        views    = _prefetch_names(cur, "view")
        indexes  = _prefetch_names(cur, "index")
        tables   = _prefetch_names(cur, "table")

        for name in triggers:
            cur.execute(f'DROP TRIGGER IF EXISTS "{name}";')

        for name in views:
            cur.execute(f'DROP VIEW IF EXISTS "{name}";')

        for name in indexes:
            cur.execute(f'DROP INDEX IF EXISTS "{name}";')

        for name in tables:
            cur.execute(f'DROP TABLE IF EXISTS "{name}";')


    except Exception:
        raise

    # Limpieza de archivo y reactivación de FKs
    cur.execute("VACUUM;")
    cur.execute("PRAGMA foreign_keys=ON;")

def main():
    print("============================================")
    print("  🔁  RECONSTRUCCIÓN DE PPAI_DATABASE.db")
    print("============================================")
    print(f"[*] Base de datos: {DB_PATH}")
    print(f"[*] Schema:        {SCHEMA_PATH}")

    if not SCHEMA_PATH.exists():
        print(f"[❌] No se encontró el archivo schema: {SCHEMA_PATH}")
        return

    with sqlite3.connect(str(DB_PATH)) as conn:
        conn.isolation_level = None  # control manual de transacciones
        cur = conn.cursor()

        print("[*] Eliminando objetos antiguos...")
        drop_all(cur)

        print("[*] Creando estructura desde schema...")
        sql = SCHEMA_PATH.read_text(encoding="utf-8")

        try:
            cur.execute("PRAGMA foreign_keys=OFF;")
            cur.executescript(sql)
            print("[✔] Estructura creada correctamente.")
        except Exception as e:
            print("[❌] Error reconstruyendo la base de datos:")
            print(e)
            raise e
        finally:
            cur.execute("PRAGMA foreign_keys=ON;")

        print("============================================")
        print("  ✅  Proceso finalizado.")
        print("============================================")

    conn.close()


if __name__ == "__main__":
    main()
