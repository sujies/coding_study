-- link:https://school.programmers.co.kr/learn/courses/30/lessons/299310

WITH EXAMPLE1 AS (
    SELECT 
        ID,
        SIZE_OF_COLONY,
        MAX(SIZE_OF_COLONY) OVER (PARTITION BY YEAR(DIFFERENTIATION_DATE)) AS MAX_SIZE,
        YEAR(DIFFERENTIATION_DATE) AS YEAR
    FROM 
        ECOLI_DATA
)

SELECT  
    YEAR,
    (MAX_SIZE - SIZE_OF_COLONY) AS YEAR_DEV,
    ID    
FROM EXAMPLE1
ORDER BY YEAR, YEAR_DEV;
