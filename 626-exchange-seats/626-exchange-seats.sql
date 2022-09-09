# Write your MySQL query statement below
select
    *
from
    (
        (
            select
                id -1 as id,
                student
            from
                seat
            where
                id % 2 = 0
        )
        union
        (
            select
                id + 1 as id,
                student
            from
                seat
            where
                id % 2 = 1
                and id <(
                    select
                        max(id)
                    from
                        seat
                )
        )
        union
        (
            select * from (
            select
                id as id,
                student
            from
                seat order by id desc
            limit
                1
            ) result1 where id%2!=0
        )
    ) result
order by
    id asc