SELECT CHAR_LENGTH('HELLO')
	 , LENGTH('HELLO')
     , CHAR_LENGTH('안녕')
     , LENGTH('안녕');
    
SELECT CONCAT('DREAMS', 'COME', 'TRUE')
	 , CONCAT_WS('-', '2023', '01', '29');

SELECT LEFT('SQL 완전정복', 3)
	 , RIGHT('SQL 완전정복', 4)
     , SUBSTR('SQL 완전정복', 2, 5)
     , SUBSTR('SQL 완전정복', 2);

SELECT SUBSTRING_INDEX('서울시 동작구 흑석로', ' ', 2)
	 , SUBSTRING_INDEX('서울시 동작구 흑석로', ' ', -2);
     
SELECT LPAD('SQL', 10, '#')
	 , RPAD('SQL', 5, '*');

SELECT LENGTH(LTRIM(' SQL ' ))
	 , LENGTH(RTRIM(' SQL ' ))
     , LENGTH(TRIM(' SQL ' ));

SELECT TRIM(BOTH 'abc' FROM 'abcSQLabcabc')
	 , TRIM(LEADING 'abc' FROM 'abcSQLabcabc')
     , TRIM(TRAILING 'abc' FROM 'abcSQLabcabc');