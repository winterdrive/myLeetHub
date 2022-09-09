# Write your MySQL query statement below
select 
    score, 
    dense_RANK()
    over
    (order by score desc)
    as 'rank'
    from scores