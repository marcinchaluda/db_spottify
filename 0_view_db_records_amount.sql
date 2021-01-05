CREATE VIEW records_amount AS
    SELECT
      SUM(reltuples) records_db
    FROM pg_class C
    LEFT JOIN pg_namespace N ON (N.oid = C.relnamespace)
    WHERE
      nspname NOT IN ('pg_catalog', 'information_schema') AND
      relkind='r';