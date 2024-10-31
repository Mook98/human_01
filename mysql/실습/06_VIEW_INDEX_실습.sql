CREATE VIEW V1_고학년학생(학생이름, 나이, 성, 학년)
AS SELECT 이름, 나이, 성별, 학년 
   FROM 학생
   WHERE 학년 BETWEEN 3 AND 4;

SELECT * FROM V1_고학년학생;

CREATE VIEW V2_과목수강현황(과목번호, 강의실, 수강인원수)
AS SELECT 과목.과목번호, 강의실, COUNT(과목.과목번호) 
   FROM 과목 JOIN 수강 ON 과목.과목번호 = 수강.과목번호
   GROUP BY 과목.과목번호;

SELECT * FROM V2_과목수강현황;   

CREATE VIEW V3_고학년여학생
AS SELECT * 
   FROM V1_고학년학생
   WHERE 성 = '여';

SELECT * FROM V3_고학년여학생;

SELECT * FROM V2_과목수강현황
WHERE 수강인원수 = (SELECT MAX(수강인원수) FROM V2_과목수강현황) OR
	  수강인원수 = (SELECT MIN(수강인원수) FROM V2_과목수강현황);

DROP VIEW V1_고학년학생;

CREATE INDEX idx_수강
ON 수강(학번,과목번호);

SHOW INDEX FROM 수강;

CREATE UNIQUE INDEX idx_과목
ON 과목(이름 ASC);

SHOW INDEX FROM 과목;

DROP INDEX idx_수강 ON 수강;
ALTER TABLE 과목 DROP INDEX idx_과목;