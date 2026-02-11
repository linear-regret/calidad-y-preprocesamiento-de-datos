CREATE OR REPLACE TABLE demo.tx_enriq
USING DELTA
AS
SELECT t.tx, c.nombre, t.monto
FROM demo.tx t
JOIN demo.clientes c
ON t.cliente_id = c.id;

select * from demo.tx_enriq;