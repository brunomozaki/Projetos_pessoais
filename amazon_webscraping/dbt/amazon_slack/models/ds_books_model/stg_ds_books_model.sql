with ds_books_model as(
select * from 
{{ source('stg_ds_books_model', 'ds_books') }}

)
select * from ds_books_model

