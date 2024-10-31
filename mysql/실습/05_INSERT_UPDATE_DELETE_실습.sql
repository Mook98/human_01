CREATE TABLE 학생1 AS (SELECT * FROM 학생) ;
CREATE TABLE 수강1 AS (SELECT * FROM 수강) ;
CREATE TABLE 과목1 AS (SELECT * FROM 과목) ;

INSERT INTO 학생1
VALUES ('g001', '김연아', '서울 서초', 4, 23, '여', '010-1111-2222', '컴퓨터');

INSERT INTO 학생1(학번, 이름, 주소, 학년, 나이, 성별, 휴대폰번호, 소속학과)
VALUES ('g002', '홍길동2', DEFAULT, 1, 26, '남', NULL, '통계');

INSERT INTO 학생1(학번, 이름, 학년, 나이, 성별, 소속학과)
VALUES ('g002', '홍길동2', 1, 26, '남', '통계');

INSERT INTO 학생1(학번, 이름, 주소, 학년, 나이, 성별, 휴대폰번호, 소속학과)
VALUES ('g003', '이승엽2', DEFAULT, 3, 30, '남', NULL, '정보통신');

SELECT * FROM 학생1
WHERE 학번 LIKE 'g%';

UPDATE 학생1 
SET 학년 = 3
WHERE 이름 = '이은진';

SELECT * FROM 학생1
WHERE 이름 = '이은진';

UPDATE 학생1
SET 학년 = 학년 + 1, 소속학과 = '자유전공학부'
WHERE 학년 = 4;

SELECT * FROM 학생1;

UPDATE 학생1
SET 소속학과 = NULL
WHERE 학번 NOT IN(SELECT 학번 FROM 수강1);

SELECT * FROM 학생1;

UPDATE 수강1
SET 학번 = (SELECT 학번 FROM 학생1
		   WHERE 이름 = '이은진')
WHERE 학번 = 's003';

SELECT * FROM 수강1
WHERE 학번 = 's003' OR 학번 = (SELECT 학번 FROM 학생1
							 WHERE 이름 = '이은진');
                             
DELETE FROM 학생1
WHERE 이름 = '송윤아';

SELECT * FROM 학생1;

DELETE FROM 학생1
WHERE 학년 = 3;

SELECT * FROM 학생;

DELETE FROM 과목1
WHERE 과목번호 IN (SELECT 과목번호 FROM 수강1
				 GROUP BY 과목번호
				 HAVING COUNT(*) < 2);
                 
SELECT * FROM 과목1;

DELETE FROM 학생1;

SELECT * FROM 학생1;


