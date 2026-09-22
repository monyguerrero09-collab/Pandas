import requests
import sqlite3
import pandas as pd

# --- CONFIGURACIÓN ---
DB_NAME = "pokedex_proyecto.db"
CSV_NAME = "pokemon_analisis_final.csv"

def ejecutar_proyecto():
    # 1. CONEXIÓN Y CREACIÓN DE TABLAS
    print("1. Inicializando base de datos...")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.executescript('''
        DROP TABLE IF EXISTS Pokemon_Type;
        DROP TABLE IF EXISTS Pokemon;
        DROP TABLE IF EXISTS Type;

        CREATE TABLE Pokemon (
            id_pokemon INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE Type (
            id_type INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE Pokemon_Type (
            id_pokemon INTEGER,
            id_type INTEGER,
            PRIMARY KEY (id_pokemon, id_type),
            FOREIGN KEY (id_pokemon) REFERENCES Pokemon (id_pokemon),
            FOREIGN KEY (id_type) REFERENCES Type (id_type)
        );
    ''')
    conn.commit()

    # 2. EXTRACCIÓN Y CARGA DE TIPOS
    print("2. Extrayendo catálogos de tipos (21 tipos)...")
    try:
        res_types = requests.get("https://pokeapi.co/api/v2/type?limit=21").json()
        for t in res_types['results']:
            t_id = t['url'].split('/')[-2]
            cursor.execute("INSERT INTO Type (id_type, name) VALUES (?, ?)", (t_id, t['name']))
        conn.commit()
    except Exception as e:
        print(f"Error al obtener tipos: {e}")

    # 3. EXTRACCIÓN Y CARGA DE POKÉMON
    print("3. Extrayendo datos de 1328 Pokémon (Esto puede tardar 2-3 minutos)...")
    try:
        res_poke_list = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1328").json()
        
        for item in res_poke_list['results']:
            p_data = requests.get(item['url']).json()
            p_id = p_data['id']
            p_name = p_data['name']
            
            # Insertar en tabla Pokemon
            cursor.execute("INSERT INTO Pokemon (id_pokemon, name) VALUES (?, ?)", (p_id, p_name))
            
            # Insertar relaciones en Pokemon_Type
            for t_info in p_data['types']:
                t_id = t_info['type']['url'].split('/')[-2]
                cursor.execute("INSERT INTO Pokemon_Type (id_pokemon, id_type) VALUES (?, ?)", (p_id, t_id))
            
            # Feedback visual cada 100 registros
            if p_id % 100 == 0:
                print(f"   > Procesados {p_id} de 1328...")
        
        conn.commit()
    except Exception as e:
        print(f"Error al obtener pokemon: {e}")

    # 4. MOSTRAR CÓMO QUEDÓ LA BASE DE DATOS (VISTA PREVIA)
    print("\n" + "="*50)
    print("VISTA PREVIA DE LAS TABLAS CARGADAS")
    print("="*50)
    
    tablas = ['Pokemon', 'Type', 'Pokemon_Type']
    for tabla in tablas:
        print(f"\n--- Tabla: {tabla} (Primeros 5 registros) ---")
        df_preview = pd.read_sql_query(f"SELECT * FROM {tabla} LIMIT 5", conn)
        print(df_preview.to_string(index=False))

    # 5. EXPORTACIÓN A CSV CON JOIN
    print("\n4. Generando reporte CSV final...")
    query_join = """
        SELECT p.id_pokemon, p.name AS pokemon_name, t.name AS tipo
        FROM Pokemon p
        JOIN Pokemon_Type pt ON p.id_pokemon = pt.id_pokemon
        JOIN Type t ON pt.id_type = t.id_type
        ORDER BY p.id_pokemon ASC
    """
    df_final = pd.read_sql_query(query_join, conn)
    df_final.to_csv(CSV_NAME, index=False)
    
    print(f"¡Éxito! Archivo '{CSV_NAME}' generado.")
    print(f"Base de datos guardada como '{DB_NAME}'.")
    
    conn.close()

if __name__ == "__main__":
    ejecutar_proyecto()