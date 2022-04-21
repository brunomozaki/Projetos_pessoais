with ds_books_model as(
select * from 
{{ source('ds_books_model_scr', 'ds_books') }}

)
select * from ds_books_model

