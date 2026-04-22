CREATE OR REPLACE VIEW demo.vw_tx_enriq AS
SELECT t.tx, c.nombre, 2* t.monto as doble_monto
FROM demo.tx t
JOIN demo.clientes c
ON t.cliente_id = c.id;

select * from demo.vw_tx_enriq;

-- Se hace el update de una de las tablas origen del join
-- No se refleja en la tabla materializada, pero sí en la vista virtual
UPDATE demo.tx
SET monto = monto + 1000;

select *, monto*2 as doble_monto from demo.tx_enriq;
select * from demo.vw_tx_enriq;