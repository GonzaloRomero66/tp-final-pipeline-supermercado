import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import sqlite3 
    import pandas as pd

    conexion = sqlite3.connect("datos/stock.sqlite")
    return conexion, pd


@app.cell
def _(conexion, pd):
    tablas = pd.read_sql_query(
        "SELECT name FROM sqlite_master WHERE type='table'", conexion
    )
    tablas
    return


@app.cell
def _(conexion, pd):
    columnas = pd.read_sql_query(
        "PRAGMA table_info(movimientos)", conexion
    )
    columnas
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _(conexion, pd):
    total_registros = pd.read_sql_query(
        "SELECT COUNT(*) AS total FROM movimientos", conexion
    )
    total_registros
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Etamos contando la cantidad de registros que serian filas en la tabla movimientos
    """)
    return


@app.cell
def _(conexion, pd):
    datos = pd.read_sql_query(
        "SELECT * FROM movimientos", conexion
    )
    datos.isna().sum()
    return (datos,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Estamos sumando las cantidades de valores nulos de cada columna
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(conexion, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """,
        engine=conexion
    )
    return


@app.cell
def _(datos):
    datos[datos.isna().any(axis=1)].head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Estamos buscando filas que tengan al menos un dato vacio y muestra las primeras 10
    any() sirve para comprobar si al menos una condición se cumple.
    axis=1 indica que revise por filas, si usamos axis=0 estaremos haciendo que revise por columnas
    """)
    return


@app.cell
def _(datos):
    datos.nunique()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    nunique() cuenta cuántos valores hay sin repetirlos e ignorando los nulos
    """)
    return


@app.cell
def _(datos):
    datos["sucursal"].value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    En la actividad se nos aclaro que solo son 3 sucursales pero como podemos ver algunas estan mal escritas y entonces se toman como si fueran 12
    """)
    return


@app.cell
def _(datos):
    datos["tipo_movimiento"].value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Como podemos ver, pasa lo mismo con los tipos de movimientos por eso aparecen mal y hacen como si fuesen mas de lo que deberia
    """)
    return


@app.cell
def _(datos):
    datos["categoria"].value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Categoria esta todo bien escrito
    """)
    return


@app.cell
def _(datos):
    datos["producto"].value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    En producto esta todo bien escrito los respectivos nombres
    """)
    return


@app.cell
def _(datos):
    datos["fecha"].describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Estamos viendo un resumen, en este caso como las fechas estan en texto podemos mostrar informacion como la cantidad de registros valores unicos, etc
    """)
    return


@app.cell
def _(datos):
    datos["fecha"].str.contains("/", na=False).sum()
    return


@app.cell
def _(datos):
    datos["fecha"].str.contains("-", na=False).sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    El formato de las fechas es con -
    """)
    return


@app.cell
def _(datos):
    datos["cantidad"].describe()
    return


@app.cell
def _(datos):
    datos[datos["cantidad"] < 0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hay cantidades en cantidad negativa, ese es otro problema
    """)
    return


@app.cell
def _(datos):
    datos["costo_unitario"].describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ¿Qué encontramos?
    - Hay 2575 movimientos en total.
    - Solamente 2445 tienen costo registrado.
    - Por lo tanto, hay 130 valores faltantes.
    - Los costos existentes van de 650 a 2800.
    - No aparecen costos negativos.
    """)
    return


@app.cell
def _(datos):
    datos["proveedor"].value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    No encontramos ningun problema con los proveedores
    """)
    return


@app.cell
def _(datos):
    datos["id_producto"].value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ¿Qué descubrimos?
    - Hay 10 productos identificados.
    - P08 es el que más aparece, con 278 movimientos.
    - P03 es el que menos aparece, con 233 movimientos.
    - Los 10 productos suman los 2575 registros.
    """)
    return


@app.cell
def _(datos):
    datos["id_movimiento"].duplicated().sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Se encontraron 75 identificadores repetidos y esos son unicos, no pueden repetirse
    """)
    return


@app.cell
def _(datos):
    datos.duplicated().sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    También hay 75 filas completamente duplicadas.
    """)
    return


@app.cell
def _():
    import duckdb
    conexion_duckdb = duckdb.connect("datos/stock.sqlite")
    return (conexion_duckdb,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Esto crea o abre nuestra base de datos DuckDB en la carpeta datos
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        CREATE OR REPLACE TABLE raw_movimientos AS
        SELECT * FROM datos
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Aca creamos la tabla raw_movimientos y copiamos todos los datos
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT COUNT(*) FROM raw_movimientos
    """).fetchall()
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        DESCRIBE raw_movimientos
    """).df()
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT COUNT(*)
        FROM raw_movimientos
        WHERE id_movimiento IS NULL
           OR TRIM(id_movimiento) = ''
    """).fetchall()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Estamos verificando que el id_movimiento no este vacio
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT COUNT(*) - COUNT(DISTINCT id_movimiento)
        FROM raw_movimientos
    """).fetchall()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Estan los 75 id_movimientos que se repiten
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT COUNT(*)
        FROM raw_movimientos
        WHERE TRY_STRPTIME(fecha, '%Y-%m-%d') IS NULL
    """).fetchall()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hay 260 fechas que no cumples el formato %Y-%m-%d
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT COUNT(*)
        FROM raw_movimientos
        WHERE id_producto IS NULL
           OR TRIM(id_producto) = ''
    """).fetchall()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    No hay ningun id_producto que este vacio
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT sucursal, COUNT(*)
        FROM raw_movimientos
        GROUP BY sucursal
        ORDER BY sucursal
    """).df()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Aca podemos ver devuelta que hay distintos nombres de sucursales, habra que corregirlos
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT COUNT(*)
        FROM raw_movimientos
        WHERE sucursal NOT IN (
            'Sucursal Norte',
            'Sucursal Sur',
            'Sucursal Centro'
        )
    """).fetchall()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hay 155 que tienen espacios adicionales o diferencias de escrituras de Sucursal Norte, Sucursal Sur, Sucursal Centro
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT COUNT(*)
        FROM raw_movimientos
        WHERE tipo_movimiento NOT IN (
            'venta',
            'ingreso',
            'merma'
        )
    """).fetchall()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hay 206 registros que su tipo de movimiento no coincide con venta, ingreso o merma
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT COUNT(*)
        FROM raw_movimientos
        WHERE cantidad <= 0
    """).fetchall()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hay 100 registros con cantidad menor o igual que 0
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT COUNT(*)
        FROM raw_movimientos
        WHERE costo_unitario IS NULL
       
    """).fetchall()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hay 130 registros que tienen un costo unitario nulo
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        CREATE OR REPLACE TEMP TABLE movimientos_clasificados AS

        WITH base AS (
            SELECT *,
                COUNT(*) OVER (
                    PARTITION BY id_movimiento
                ) AS repeticiones_id
            FROM raw_movimientos
        )

        SELECT *,
            CONCAT_WS(' | ',

                CASE
                    WHEN id_movimiento IS NULL
                      OR TRIM(id_movimiento) = ''
                    THEN 'ID vacío'
                END,

                CASE
                    WHEN TRIM(id_movimiento) <> ''
                      AND repeticiones_id > 1
                    THEN 'ID duplicado'
                END,

                CASE
                    WHEN fecha IS NULL
                      OR TRY_STRPTIME(fecha, '%Y-%m-%d') IS NULL
                    THEN 'Fecha inválida'
                END,

                CASE
                    WHEN id_producto IS NULL
                      OR TRIM(id_producto) = ''
                    THEN 'ID de producto vacío'
                END,

                CASE
                    WHEN sucursal IS NULL
                      OR sucursal NOT IN (
                        'Sucursal Norte',
                        'Sucursal Sur',
                        'Sucursal Centro'
                      )
                    THEN 'Sucursal inválida'
                END,

                CASE
                    WHEN tipo_movimiento IS NULL
                      OR tipo_movimiento NOT IN (
                        'venta', 'ingreso', 'merma'
                      )
                    THEN 'Tipo de movimiento inválido'
                END,

                CASE
                    WHEN cantidad IS NULL OR cantidad <= 0
                    THEN 'Cantidad inválida'
                END,

                CASE
                    WHEN costo_unitario IS NULL OR costo_unitario < 0
                    THEN 'Costo inválido'
                END

            ) AS motivo_rechazo

        FROM base
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Se creó una tabla temporal llamada movimientos_clasificados para aplicar las 8 reglas de validación a los registros originales. El proceso identifica los posibles errores, como identificadores duplicados, fechas incorrectas, sucursales no válidas, cantidades negativas y costos faltantes. Los problemas encontrados se registran en una nueva columna llamada motivo_rechazo, permitiendo identificar qué registros cumplen las condiciones y cuáles necesitan revisión.
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT
            COUNT(*) AS total,
            COUNT(*) FILTER (
                WHERE motivo_rechazo = ''
            ) AS validos,
            COUNT(*) FILTER (
                WHERE motivo_rechazo <> ''
            ) AS rechazados
        FROM movimientos_clasificados
    """).df()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Aca estamos mostrando los registros que fueron rechazados y los que fueron validos
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        CREATE OR REPLACE TABLE validos AS
        SELECT *
        FROM movimientos_clasificados
        WHERE motivo_rechazo = ''
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Creamos una tabla independiente donde estan los registros validos
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        CREATE OR REPLACE TABLE rechazados AS
        SELECT *
        FROM movimientos_clasificados
        WHERE motivo_rechazo <> ''
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Creamos esta otra tabla independiente donde estan los registros rechazados y el motivo del porque fueron rechazados
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT *
        FROM rechazados
        LIMIT 20
    """).df()
    return


if __name__ == "__main__":
    app.run()
