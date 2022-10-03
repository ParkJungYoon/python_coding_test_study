-- write your code in PostgreSQL 9.4
SELECT count(*)  
FROM (SELECT rn, p1, p2, DECODE(COUNT(*), 1, '', '*'||COUNT(*)) p3,COUNT(*) cnt MIN(lv) lv
        FROM (SELECT rn, lv, REGEXP_SUBSTR(p1, '[^+]+', 1, lv) p1, REGEXP_SUBSTR(p2, '[^+]+', 1, lv) p2
        FROM ( SELECT ROWNUM rn
                    , lv lvl
                    , SYS_CONNECT_BY_PATH(name,'+') p1
                    , SYS_CONNECT_BY_PATH(price,'+') p2
                FROM t
            CROSS JOIN
                (SELECT lv  
                    FROM (SELECT LEVEL lv FROM products CONNECT BY LEVEL <= 
                        WHERE lv <= 100 / (SELECT MIN(price) FROM t)
                        )
            START WITH lv = 1
            CONNECT BY PRIOR lv + 1 = lv
            ORDER SIBILINGS BY name
            )
            WHERE lv <= lvl
        )
    GROUP BY rn, p1, p2
    )
GROPU BY rn
HAVING SUM(p2*cnt) < 101
);