CREATE TABLE t01prefecture
(
  pref_cd integer NOT NULL,
  pref_name character varying(10),
  CONSTRAINT t01prefecture_pkey PRIMARY KEY (pref_cd)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE t01prefecture
  OWNER TO postgres;


CREATE OR REPLACE FUNCTION test_sp(IN from_cd integer, IN to_cd integer)
  RETURNS TABLE(code integer, name varchar) AS
$$
DECLARE
BEGIN
    RETURN QUERY SELECT PREF_CD,PREF_NAME FROM t01Prefecture
            WHERE PREF_CD BETWEEN from_cd AND to_cd;
END;
$$ LANGUAGE plpgsql;

