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