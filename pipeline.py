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

    conexion = sqlite3.connect("file:datos/stock.sqlite?mode=ro", uri=True)
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
    Estamos sumando las cantidades de valores nulos de cada columna. Ojo: hay 130 costos, 127 productos y 152 categorias nulas
    """)
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
    Categoria esta bien escrita, pero value_counts() no cuenta los nulos: hay 152 categorias vacias (NaN)
    """)
    return


@app.cell
def _(datos):
    datos["producto"].value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Los nombres de producto estan bien escritos, pero hay 127 productos vacios (NaN) que value_counts() no muestra
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
    Hay 260 fechas con / (formato dd/mm/yyyy) y el resto con - (yyyy-mm-dd)
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

    conexion_duckdb = duckdb.connect("datos/supermercado.duckdb")
    return (conexion_duckdb,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Creamos nuestra base DuckDB en `datos/supermercado.duckdb`. Es un archivo propio, distinto del SQLite original, asi que el original no se modifica
    """)
    return


@app.cell
def _(conexion_duckdb, datos):
    conexion_duckdb.register("datos_origen", datos)
    conexion_duckdb.execute("""
        CREATE OR REPLACE TABLE raw_movimientos AS
        SELECT * FROM datos_origen
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Creamos raw_movimientos con los datos tal cual vienen del SQLite (sin transformar nada). `datos` es el DataFrame que leimos mas arriba en modo lectura
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
        SELECT
            COUNT(*) FILTER (WHERE producto IS NULL OR TRIM(producto) = '') AS productos_vacios,
            COUNT(*) FILTER (WHERE categoria IS NULL OR TRIM(categoria) = '') AS categorias_vacias
        FROM raw_movimientos
    """).df()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hay 127 productos y 152 categorias vacias. Antes no las habiamos detectado porque value_counts() ignora los nulos. Vamos a agregar una regla nueva (la 9) para detectarlas
    """)
    return


@app.cell
def _():
    def clasificar(origen):
        """Devuelve un SELECT que agrega motivo_rechazo aplicando las 9 reglas.
        Se usa dos veces: sobre raw_movimientos (punto 3) y sobre los
        rechazados ya limpios (para revalidar todo en el punto 5)."""
        return f"""
        WITH base AS (
            SELECT *,
                COUNT(*) OVER (PARTITION BY id_movimiento) AS repeticiones_id
            FROM {origen}
        )
        SELECT * EXCLUDE (repeticiones_id),
            CONCAT_WS(' | ',
                CASE WHEN id_movimiento IS NULL OR TRIM(id_movimiento) = ''
                     THEN 'ID vacío' END,
                CASE WHEN TRIM(id_movimiento) <> '' AND repeticiones_id > 1
                     THEN 'ID duplicado' END,
                CASE WHEN fecha IS NULL OR TRY_STRPTIME(fecha, '%Y-%m-%d') IS NULL
                     THEN 'Fecha inválida' END,
                CASE WHEN id_producto IS NULL OR TRIM(id_producto) = ''
                     THEN 'ID de producto vacío' END,
                CASE WHEN producto IS NULL OR TRIM(producto) = ''
                       OR categoria IS NULL OR TRIM(categoria) = ''
                     THEN 'Producto o categoría vacío' END,
                CASE WHEN sucursal IS NULL
                       OR sucursal NOT IN ('Sucursal Norte', 'Sucursal Sur', 'Sucursal Centro')
                     THEN 'Sucursal inválida' END,
                CASE WHEN tipo_movimiento IS NULL
                       OR tipo_movimiento NOT IN ('venta', 'ingreso', 'merma')
                     THEN 'Tipo de movimiento inválido' END,
                CASE WHEN cantidad IS NULL OR cantidad <= 0
                     THEN 'Cantidad inválida' END,
                CASE WHEN costo_unitario IS NULL OR costo_unitario < 0
                     THEN 'Costo inválido' END
            ) AS motivo_rechazo
        FROM base
        """

    return (clasificar,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Guardamos las 9 reglas en una funcion `clasificar()` para poder aplicar exactamente las mismas reglas dos veces: primero sobre los datos crudos y despues sobre los datos ya limpios (revalidacion)
    """)
    return


@app.cell
def _(clasificar, conexion_duckdb):
    conexion_duckdb.execute(f"""
        CREATE OR REPLACE TEMP TABLE movimientos_clasificados AS
        {clasificar("raw_movimientos")}
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT
            COUNT(*) AS total,
            COUNT(*) FILTER (WHERE motivo_rechazo = '') AS validos,
            COUNT(*) FILTER (WHERE motivo_rechazo <> '') AS rechazados
        FROM movimientos_clasificados
    """).df()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Total de registros, cuantos son validos y cuantos rechazados con las 9 reglas
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        CREATE OR REPLACE TABLE validos AS
        SELECT * EXCLUDE (motivo_rechazo)
        FROM movimientos_clasificados
        WHERE motivo_rechazo = ''
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Tabla `validos`: los registros que pasaron las 9 reglas
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
    Tabla `rechazados`: los registros que fallaron al menos una regla, con `motivo_rechazo`
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT regla, COUNT(*) AS cantidad
        FROM (
            SELECT UNNEST(STRING_SPLIT(motivo_rechazo, ' | ')) AS regla
            FROM rechazados
        )
        GROUP BY regla
        ORDER BY cantidad DESC
    """).df()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Cantidad de registros rechazados por CADA regla (un registro puede fallar mas de una, por eso la suma supera el total de rechazados). Esto sirve para el informe
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT
            id_producto,
            COUNT(DISTINCT producto) AS nombres,
            COUNT(DISTINCT categoria) AS categorias,
            COUNT(DISTINCT costo_unitario) AS costos
        FROM raw_movimientos
        GROUP BY id_producto
        ORDER BY id_producto
    """).df()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Cada id_producto tiene un unico nombre, una unica categoria y un unico costo. Entonces podemos recuperar los valores vacios sin inventar nada: se completan con los del mismo id_producto
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        CREATE OR REPLACE TEMP TABLE catalogo_productos AS
        SELECT
            id_producto,
            MAX(producto) AS producto,
            MAX(categoria) AS categoria,
            MAX(costo_unitario) AS costo_unitario
        FROM raw_movimientos
        GROUP BY id_producto
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Armamos un catalogo con un solo producto, categoria y costo por id_producto (MAX ignora los nulos, asi que toma el valor que si existe)
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        CREATE OR REPLACE TEMP TABLE rechazados_normalizados AS
        SELECT DISTINCT
            r.id_movimiento,
            COALESCE(
                STRFTIME(TRY_STRPTIME(r.fecha, '%d/%m/%Y'), '%Y-%m-%d'),
                r.fecha
            ) AS fecha,
            r.id_producto,
            COALESCE(r.producto, c.producto) AS producto,
            COALESCE(r.categoria, c.categoria) AS categoria,
            TRIM(r.sucursal) AS sucursal,
            LOWER(TRIM(r.tipo_movimiento)) AS tipo_movimiento,
            ABS(r.cantidad) AS cantidad,
            COALESCE(r.costo_unitario, c.costo_unitario) AS costo_unitario,
            r.proveedor,
            CONCAT_WS(', ',
                CASE WHEN r.fecha LIKE '%/%' THEN 'fecha' END,
                CASE WHEN r.sucursal <> TRIM(r.sucursal) THEN 'sucursal' END,
                CASE WHEN r.tipo_movimiento <> LOWER(TRIM(r.tipo_movimiento)) THEN 'tipo' END,
                CASE WHEN r.cantidad < 0 THEN 'cantidad (signo)' END,
                CASE WHEN r.costo_unitario IS NULL AND c.costo_unitario IS NOT NULL THEN 'costo' END,
                CASE WHEN r.producto IS NULL AND c.producto IS NOT NULL THEN 'producto' END,
                CASE WHEN r.categoria IS NULL AND c.categoria IS NOT NULL THEN 'categoria' END
            ) AS correcciones
        FROM rechazados r
        LEFT JOIN catalogo_productos c USING (id_producto)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Limpieza de los rechazados en un solo paso:
    - fecha: pasa de dd/mm/yyyy a yyyy-mm-dd
    - sucursal: TRIM (solo tenia espacios de mas)
    - tipo_movimiento: LOWER + TRIM (venian en mayuscula o con espacios)
    - cantidad: ABS (los negativos son un error de signo; es un supuesto, queda registrado en `correcciones`)
    - costo, producto y categoria vacios: se completan desde el catalogo por id_producto
    - SELECT DISTINCT elimina las copias repetidas de los ID duplicados (eran filas identicas)
    La columna `correcciones` deja constancia de que se le arreglo a cada registro
    """)
    return


@app.cell
def _(clasificar, conexion_duckdb):
    conexion_duckdb.execute(f"""
        CREATE OR REPLACE TABLE rechazados_limpios AS
        {clasificar("rechazados_normalizados")}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Creamos `rechazados_limpios` volviendo a aplicar las 9 reglas completas sobre los datos ya limpios. Si `motivo_rechazo` queda vacio, el registro quedo recuperado
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT
            COUNT(*) AS total,
            COUNT(*) FILTER (WHERE motivo_rechazo = '') AS recuperados,
            COUNT(*) FILTER (WHERE motivo_rechazo <> '') AS pendientes
        FROM rechazados_limpios
    """).df()
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT motivo_rechazo, COUNT(*) AS cantidad
        FROM rechazados_limpios
        WHERE motivo_rechazo <> ''
        GROUP BY motivo_rechazo
        ORDER BY cantidad DESC
    """).df()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Resultado de la limpieza: cuantos se recuperaron y, si quedo alguno pendiente, por que regla sigue fallando
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT id_movimiento, COUNT(*) AS cantidad
        FROM rechazados_limpios
        GROUP BY id_movimiento
        HAVING COUNT(*) > 1
    """).df()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Control: no debe devolver ninguna fila (ningun id_movimiento repetido)
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT *
        FROM rechazados_limpios
        WHERE correcciones <> ''
        LIMIT 10
    """).df()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ejemplos de registros recuperados. La columna `correcciones` dice que se le arreglo a cada uno
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Punto 6: tabla final

    Unimos los registros que ya eran validos con los rechazados que pudieron recuperarse,
    descartamos los que aun fallan alguna regla y dejamos una sola fila por `id_movimiento`.
    Las fechas y los datos numericos quedan en tipos utiles para las consultas de negocio.
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        CREATE OR REPLACE TABLE tabla_final AS
        WITH unificados AS (
            SELECT
                1 AS prioridad,
                CAST(id_movimiento AS VARCHAR) AS id_movimiento,
                TRY_CAST(fecha AS DATE) AS fecha,
                CAST(id_producto AS VARCHAR) AS id_producto,
                CAST(producto AS VARCHAR) AS producto,
                CAST(categoria AS VARCHAR) AS categoria,
                CAST(sucursal AS VARCHAR) AS sucursal,
                CAST(tipo_movimiento AS VARCHAR) AS tipo_movimiento,
                TRY_CAST(cantidad AS INTEGER) AS cantidad,
                TRY_CAST(costo_unitario AS DECIMAL(18, 2)) AS costo_unitario,
                CAST(proveedor AS VARCHAR) AS proveedor
            FROM validos

            UNION ALL

            SELECT
                2 AS prioridad,
                CAST(id_movimiento AS VARCHAR) AS id_movimiento,
                TRY_CAST(fecha AS DATE) AS fecha,
                CAST(id_producto AS VARCHAR) AS id_producto,
                CAST(producto AS VARCHAR) AS producto,
                CAST(categoria AS VARCHAR) AS categoria,
                CAST(sucursal AS VARCHAR) AS sucursal,
                CAST(tipo_movimiento AS VARCHAR) AS tipo_movimiento,
                TRY_CAST(cantidad AS INTEGER) AS cantidad,
                TRY_CAST(costo_unitario AS DECIMAL(18, 2)) AS costo_unitario,
                CAST(proveedor AS VARCHAR) AS proveedor
            FROM rechazados_limpios
            WHERE motivo_rechazo = ''
        ),
        ordenados AS (
            SELECT
                *,
                ROW_NUMBER() OVER (
                    PARTITION BY id_movimiento
                    ORDER BY prioridad
                ) AS nro_dup
            FROM unificados
        )
        SELECT
            id_movimiento,
            fecha,
            id_producto,
            producto,
            categoria,
            sucursal,
            tipo_movimiento,
            cantidad,
            costo_unitario,
            proveedor
        FROM ordenados
        WHERE nro_dup = 1
          AND fecha IS NOT NULL
          AND cantidad IS NOT NULL
          AND cantidad > 0
          AND costo_unitario IS NOT NULL
          AND costo_unitario >= 0
    """)
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("DESCRIBE tabla_final").df()
    return


@app.cell
def _(conexion_duckdb):
    conexion_duckdb.execute("""
        SELECT
            COUNT(*) AS total_final,
            COUNT(DISTINCT id_movimiento) AS ids_unicos,
            COUNT(*) FILTER (WHERE fecha IS NULL) AS fechas_nulas,
            COUNT(*) FILTER (WHERE cantidad IS NULL OR cantidad <= 0) AS cantidades_invalidas,
            COUNT(*) FILTER (WHERE costo_unitario IS NULL OR costo_unitario < 0) AS costos_invalidos
        FROM tabla_final
    """).df()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Controles finales del punto 6:
    - `total_final` debe coincidir con `ids_unicos`;
    - las columnas de fecha y los numericos deben tener el tipo correspondiente;
    - no deben quedar fechas, cantidades o costos invalidos.
    """)
    return


if __name__ == "__main__":
    app.run()
