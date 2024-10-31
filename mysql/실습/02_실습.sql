USE 한빛무역;
SELECT * FROM 고객;
SELECT 고객회사명 FROM 고객;

SELECT 고객번호,
	담당자명,
    고객회사명,
    마일리지 AS 포인트,
    마일리지 * 1.1 AS "10%인상된 마일리지"
FROM 고객;

SELECT 고객번호, 담당자명, 마일리지 FROM 고객
WHERE 마일리지 >= 100000;

SELECT 고객번호, 담당자명, 도시, 마일리지 AS 포인트 FROM 고객
WHERE 도시 = '서울특별시'
ORDER BY 마일리지 DESC;
    
SELECT 고객번호, 담당자명, 도시, 마일리지 AS 포인트 FROM 고객
WHERE 도시 = '서울특별시'
ORDER BY 마일리지 DESC;
    
SELECT * FROM 고객
LIMIT 3;
    
SELECT * FROM 고객
ORDER BY 마일리지 DESC
LIMIT 3;
    
SELECT DISTINCT 도시 FROM 고객;

SELECT 
	  23 + 5 AS 더하기
	, 23 - 5 AS 빼기
	, 23 * 5 AS 곱하기
	, 23 / 5 AS 실수나누기
	, 23 DIV 5 AS 정수나누기
	, 23 % 5 AS 나머지1
	, 23 MOD 5 AS 나머지2;
       
SELECT 
	  23 >= 5
	, 23 <= 5 
	, 23 > 23 
	, 23 < 23 
	, 23 = 23 
	, 23 != 23 
	, 23 <> 23;

SELECT * FROM 고객
WHERE 담당자직위 <> '대표이사';
    
SELECT * FROM 고객
WHERE 도시 = '부산광역시'
AND 마일리지 < 1000;

SELECT 고객번호, 담당자명, 마일리지, 도시 FROM 고객
WHERE 도시 = '부산광역시'
OR 마일리지 < 1000;
    
SELECT 고객번호, 담당자명, 마일리지, 도시 FROM 고객
WHERE 도시 = '부산광역시'
UNION
SELECT 고객번호, 담당자명, 마일리지, 도시 FROM 고객
WHERE 마일리지 < 1000
ORDER BY 고객번호;

SELECT * FROM 고객
WHERE 지역 
IS NULL;

SELECT * FROM 고객
WHERE 지역 = '';

UPDATE 고객 
SET 지역 = NULL
WHERE 지역 = '';

SELECT * FROM 고객;

SELECT 고객번호, 담당자명, 담당자직위 FROM 고객
WHERE 담당자직위 = '영업 과장'
OR 담당자직위 = '마케팅 과장';

SELECT 고객번호, 담당자명, 담당자직위 FROM 고객
WHERE 담당자직위
IN ('영업 과장', '마케팅 과장');

SELECT 담당자명, 마일리지 FROM 고객
WHERE 마일리지 >= 100000
AND 마일리지 <= 200000;

SELECT 담당자명, 마일리지 FROM 고객
WHERE 마일리지 BETWEEN 100000 AND 200000;

SELECT * FROM 고객
WHERE 도시 LIKE '%광역시'
AND (고객번호 LIKE '_C%' OR 고객번호 LIKE '__C%');

SELECT * FROM 고객
WHERE 고객번호 LIKE 'A%';
