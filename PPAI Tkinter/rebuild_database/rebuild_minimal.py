import rebuild_database
import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent  # .../rebuild_database/.. = raíz del proyecto
DB_PATH = PROJECT_ROOT / "infrastructure" / "database" / "PPAI_DATABASE.db"
QUERIES_PATH = PROJECT_ROOT / "rebuild_database" / "SQL_QUERIES.sql"  # ruta a la query

def main():
    # Limpiar la BDD
    rebuild_database.main()

    with sqlite3.connect(str(DB_PATH)) as conn:
        conn.isolation_level = None  # control manual de transacciones
        cur = conn.cursor()
        queries = QUERIES_PATH.read_text(encoding="utf-8")

        print("[*] Insertando datos iniciales...")

        cur.executescript(queries)

        print("[✔] Se han insertado los datos iniciales correctamente.")

        print("============================================")
        print("  ✅  Proceso finalizado.")
        print("============================================")

    conn.close()


if __name__ == "__main__":
    main()