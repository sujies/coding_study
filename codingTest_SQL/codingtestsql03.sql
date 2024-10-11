--LINK: https://school.programmers.co.kr/learn/courses/30/lessons/276034
-- 코드를 작성해주세요
SELECT DISTINCT(D.id), D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS D
JOIN SKILLCODES S
  ON (D.SKILL_CODE & S.CODE) = S.CODE
WHERE S.NAME = "Python"
OR S.NAME = "C#"
ORDER BY ID;