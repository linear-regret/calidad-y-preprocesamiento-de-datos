CREATE DATABASE IF NOT EXISTS demo;

CREATE OR REPLACE TABLE demo.clientes (
  id INT,
  nombre STRING
) USING DELTA;

INSERT INTO demo.clientes VALUES
  (1,'Ana'),
  (2,'Luis');

CREATE OR REPLACE TABLE demo.tx (
  tx INT,
  cliente_id INT,
  monto DOUBLE
) USING DELTA;

INSERT INTO demo.tx VALUES
  (101,1,250.0),
  (102,1,120.5),
  (103,2,999.9);
