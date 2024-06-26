-- 코드를 입력하세요
SELECT T1.PRODUCT_ID, T1.PRODUCT_NAME, T1.PRICE * T2.AMOUNT AS TOTAL_SALES
FROM FOOD_PRODUCT T1
   , (SELECT SUM(AMOUNT) AS AMOUNT, PRODUCT_ID
      FROM FOOD_ORDER
      WHERE TO_CHAR(PRODUCE_DATE, 'YYYYMM') = '202205'
      GROUP BY PRODUCT_ID
     ) T2
WHERE T1.PRODUCT_ID = T2.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID;