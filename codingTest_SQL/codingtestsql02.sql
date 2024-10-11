LINK: https://school.programmers.co.kr/learn/courses/30/lessons/301646
SELECT COUNT(*) as COUNT
FROM ECOLI_DATA
WHERE -- 2번 형질이 없는 개체 (2번째 비트가 0)
  (GENOTYPE & 2) <> 2
AND -- 1번 형질(첫 번째 비트) 또는 3번 형질(세 번째 비트)을 보유한 개체
  (GENOTYPE & 1 = 1 OR GENOTYPE & 4 = 4);