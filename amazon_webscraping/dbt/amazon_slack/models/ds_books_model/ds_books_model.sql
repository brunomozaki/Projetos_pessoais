WITH BASE AS (SELECT 
	*,
	CASE WHEN REVIEW_COUNT > 250 -- Random number
		THEN 'POPULAR'
		ELSE 'NOT POPULAR'
		END POPULARITY,
	REPLACE(SPLIT_PART(RATING,'de', 1 ), ',', '.')::NUMERIC		    RATING_NUM,  -- extracting only the rating as numeric value
    REPLACE(SUBSTRING(PRICE,4,6), ',', '.')::NUMERIC                PRICE_NUM    -- extracting only the price as numeric value
			  
    
	
FROM {{ ref('stg_ds_books_model') }}
WHERE DESCRIPTION 
NOT IN ('Homo Deus', '21 lições para o século 21', 'Breve história de quase tudo', 'Raízes do Brasil') --REMOVING ADS FROM AMAZON SEARCH
)


SELECT *  	
FROM BASE 