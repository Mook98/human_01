USE univdb;
SHOW TABLES;

SELECT * FROM 과목;
SELECT * FROM 학생;

SELECT 이름, 주소 FROM 학생;

SELECT 학번, 이름, 주소, 학년, 나이, 성별, 휴대폰번호, 소속학과 FROM 학생;

SELECT DISTINCT 소속학과 FROM 학생;

SELECT 소속학과 FROM 학생;
SELECT ALL 소속학과 FROM 학생;

SELECT 이름, 학년, 소속학과, 휴대폰번호 FROM 학생
WHERE 학년 >= 2 And 소속학과 = '컴퓨터';

SELECT 이름, 학년, 소속학과, 휴대폰번호 FROM 학생
WHERE (학년 >= 1 AND 학년 <= 3) OR NOT(소속학과 = '컴퓨터');

SELECT 이름, 학년, 소속학과, 휴대폰번호 FROM 학생
WHERE (학년 BETWEEN 1 AND 3) OR NOT(소속학과 = '컴퓨터');

SELECT 이름, 학년, 소속학과, 휴대폰번호 FROM 학생
WHERE (학년 BETWEEN 1 AND 3) OR (소속학과 <> '컴퓨터'); 

SELECT 이름, 학년, 소속학과 FROM 학생
WHERE (소속학과 = '컴퓨터') OR (소속학과 = '정보통신')
ORDER BY 학년;

SELECT * FROM 학생
ORDER BY 학년 ASC, 이름 DESC;

SELECT * FROM 수강
ORDER BY 중간성적 DESC
LIMIT 3;

SELECT * FROM 수강
ORDER BY 중간성적 DESC
LIMIT 5, 3;

SELECT COUNT(*) FROM 학생;

SELECT COUNT(학번) FROM 학생;

SELECT COUNT(*) AS 학생수1
	 , COUNT(주소) AS 학생수2
     , COUNT(DISTINCT 주소) AS 학생수3 
FROM 학생; 

SELECT * FROM 학생;

SELECT AVG(나이) FROM 학생
WHERE 성별 = '여';

SELECT 성별, MAX(나이) AS '최고 나이', MIN(나이) AS '최저 나이' FROM 학생
GROUP BY 성별;

SELECT 나이, COUNT(*) AS '나이별 학생수' FROM 학생
WHERE 나이 >= 20 AND 나이 < 30
GROUP BY 나이;

SELECT 학년, COUNT(*) AS '학년별 학생수' FROM 학생
GROUP BY 학년
HAVING COUNT(*) >= 2;

SELECT 학번, 이름 FROM 학생
WHERE 이름 LIKE '이%';

SELECT 이름, 주소, 학년 FROM 학생
WHERE 주소 LIKE '%서울%'
ORDER BY 학년 DESC;

SELECT 이름, 휴대폰번호 FROM 학생
WHERE 휴대폰번호 IS NULL;

SELECT 학번 FROM 학생
WHERE 성별 = '여'
UNION
SELECT 학번 FROM 수강
WHERE 평가학점 = 'A';

SELECT 이름 FROM 학생
WHERE 학번 IN (SELECT 학번 FROM 수강
			  WHERE 과목번호 = 'c002');
              
SELECT 이름 FROM 학생
WHERE 학번 IN (SELECT 학번 FROM 수강
			  WHERE 과목번호 = (SELECT 과목번호 FROM 과목
							  WHERE 이름 = '정보보호'));
                              
SELECT 이름 FROM 학생
WHERE EXISTS (SELECT * FROM 수강
			  WHERE 수강.학번 = 학생.학번 AND 과목번호 = 'c002');
              
SELECT 이름 FROM 학생
WHERE NOT EXISTS (SELECT * FROM 수강
				  WHERE 수강.학번 = 학생.학번);
                  
SELECT * FROM 학생, 수강;

SELECT * FROM 학생 CROSS JOIN 수강;

SELECT * FROM 학생, 수강
WHERE 학생.학번 = 수강.학번 ;

SELECT * FROM 학생 JOIN 수강 ON 학생.학번=수강.학번;

SELECT 학생.학번, 이름, 과목번호, 중간성적 + (중간성적 * 0.1) AS 변환중간성적 
FROM 학생, 수강
WHERE 학생.학번 = 수강.학번 AND 과목번호 > 'c0002';

SELECT 학생.학번, 이름, 과목번호, 중간성적 + (중간성적 * 0.1) AS 변환중간성적 
FROM 학생 JOIN 수강 ON 학생.학번 = 수강.학번
WHERE 과목번호 = 'c002';

SELECT 학생.학번, 학생.이름, 수강.과목번호 FROM 학생, 수강, 과목
WHERE 학생.학번 = 수강.학번 AND 수강.과목번호 = 과목.과목번호 AND 과목.이름 = '정보보호';

SELECT 학생.학번, 학생.이름, 수강.과목번호 
FROM (학생 JOIN 수강 ON 학생.학번 = 수강.학번) JOIN 과목 ON 수강.과목번호 = 과목.과목번호
WHERE 과목.이름 = '정보보호';

SELECT 이름, 과목번호 FROM 학생 AS S, 수강 AS E
WHERE S.학번 = E.학번 AND 과목번호 = 'c002';

SELECT S1.이름, S2.이름
FROM 학생 S1 JOIN 학생 S2 ON S1.주소 = S2.주소
WHERE S1.학년 > S2.학년;

SELECT 학생.학번, 이름, 평가학점
FROM 학생 LEFT OUTER JOIN 수강 ON 학생.학번 = 수강.학번;

