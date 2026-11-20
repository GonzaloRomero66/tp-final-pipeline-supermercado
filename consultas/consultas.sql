-- 1. Unidades vendidas por categoria
SELECT
    categoria,
    SUM(cantidad) AS unidades_vendidas
FROM tabla_final
WHERE tipo_movimiento = 'venta'
GROUP BY categoria
ORDER BY unidades_vendidas DESC, categoria;

-- 2. Unidades de merma por sucursal
SELECT
    sucursal,
    SUM(cantidad) AS unidades_merma
FROM tabla_final
WHERE tipo_movimiento = 'merma'
GROUP BY sucursal
ORDER BY unidades_merma DESC, sucursal;

-- 3. Gasto en ingresos de mercaderia por proveedor
SELECT
    proveedor,
    SUM(cantidad * costo_unitario) AS gasto_total
FROM tabla_final
WHERE tipo_movimiento = 'ingreso'
GROUP BY proveedor
ORDER BY gasto_total DESC, proveedor;

-- 4. Producto mas vendido en unidades
SELECT
    producto,
    SUM(cantidad) AS unidades_vendidas
FROM tabla_final
WHERE tipo_movimiento = 'venta'
GROUP BY producto
ORDER BY unidades_vendidas DESC, producto
LIMIT 1;

-- 5. Movimientos por mes: primeros 6 meses con movimientos
WITH meses AS (
    SELECT DISTINCT
        STRFTIME(fecha, '%Y-%m') AS mes
    FROM tabla_final
    WHERE fecha IS NOT NULL
),
primeros_meses AS (
    SELECT mes
    FROM meses
    ORDER BY mes
    LIMIT 6
)
SELECT
    STRFTIME(fecha, '%Y-%m') AS mes,
    COUNT(*) AS movimientos
FROM tabla_final
WHERE STRFTIME(fecha, '%Y-%m') IN (SELECT mes FROM primeros_meses)
GROUP BY mes
ORDER BY mes;