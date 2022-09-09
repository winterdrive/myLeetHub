select
    a.product_id,
    c.product_name
from
    (
        select
            *
        from
            sales
        where
            sale_date between "2019-01-01"
            and "2019-03-31"
    ) a
    left join (
        select
            *
        from
            sales
        where
            sale_date not between "2019-01-01"
            and "2019-03-31"
    ) b on a.product_id = b.product_id
    left join (
        select
            *
        from
            product
    ) c on c.product_id = a.product_id
where
    b.product_id IS NULL
group by a.product_id