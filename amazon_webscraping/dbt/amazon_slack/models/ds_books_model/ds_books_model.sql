WITH BASE AS (SELECT 
	*,
	CASE WHEN REVIEW_COUNT > 250 -- RANDOM NUMBER
		THEN 'POPULAR'
		ELSE 'NOT POPULAR'
		END POPULARITY,
	REPLACE(SPLIT_PART(RATING,'de', 1 ), ',', '.')::NUMERIC		                    RATING_NUM,
    REPLACE(SPLIT_PART(SUBSTRING(PRICE,4,6), 'R$ ', 1), ',', '.')::NUMERIC          PRICE_NUM
			  
    
	
FROM {{ ref('stg_ds_books_model') }}
WHERE DESCRIPTION 
NOT IN ('Homo Deus', '21 lições para o século 21', 'Breve história de quase tudo', 'Raízes do Brasil') --REMOVING ADS FROM AMAZON SEARCH
)


SELECT *  	
FROM BASE 