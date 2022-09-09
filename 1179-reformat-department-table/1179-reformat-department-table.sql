# Write your MySQL query statement below
select
    zero.id,
    a.Jan_Revenue,
    b.Feb_Revenue,
    c.Mar_Revenue,
    d.Apr_Revenue,
    e.May_Revenue,
    f.Jun_Revenue,
    g.Jul_Revenue,
    h.Aug_Revenue,
    i.Sep_Revenue,
    j.Oct_Revenue,
    k.Nov_Revenue,
    l.Dec_Revenue
from
    (
        (
            (
                (
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                (
                                                    (
                                                        select
                                                            distinct(id)
                                                        from
                                                            department
                                                    ) as zero
                                                    left join (
                                                        select
                                                            Department.id as id,
                                                            revenue as Jan_Revenue
                                                        from
                                                            department
                                                        where
                                                            month = 'Jan'
                                                    ) as a on zero.id = a.id
                                                )
                                                left join (
                                                    select
                                                        Department.id as id,
                                                        revenue as Feb_Revenue
                                                    from
                                                        department
                                                    where
                                                        month = 'Feb'
                                                ) as b on zero.id = b.id
                                            )
                                            left join (
                                                select
                                                    Department.id as id,
                                                    revenue as Mar_Revenue
                                                from
                                                    department
                                                where
                                                    month = 'Mar'
                                            ) as c on zero.id = c.id
                                        )
                                        left join (
                                            select
                                                Department.id as id,
                                                revenue as Apr_Revenue
                                            from
                                                department
                                            where
                                                month = 'Apr'
                                        ) as d on zero.id = d.id
                                    )
                                    left join (
                                        select
                                            Department.id as id,
                                            revenue as May_Revenue
                                        from
                                            department
                                        where
                                            month = 'May'
                                    ) as e on zero.id = e.id
                                )
                                left join (
                                    select
                                        Department.id as id,
                                        revenue as Jun_Revenue
                                    from
                                        department
                                    where
                                        month = 'Jun'
                                ) as f on zero.id = f.id
                            )
                            left join (
                                select
                                    Department.id as id,
                                    revenue as Jul_Revenue
                                from
                                    department
                                where
                                    month = 'Jul'
                            ) as g on zero.id = g.id
                        )
                        left join (
                            select
                                Department.id as id,
                                revenue as Aug_Revenue
                            from
                                department
                            where
                                month = 'Aug'
                        ) as h on zero.id = h.id
                    )
                    left join (
                        select
                            Department.id as id,
                            revenue as Sep_Revenue
                        from
                            department
                        where
                            month = 'Sep'
                    ) as i on zero.id = i.id
                )
                left join (
                    select
                        Department.id as id,
                        revenue as Oct_Revenue
                    from
                        department
                    where
                        month = 'Oct'
                ) as j on zero.id = j.id
            )
            left join (
                select
                    Department.id as id,
                    revenue as Nov_Revenue
                from
                    department
                where
                    month = 'Nov'
            ) as k on zero.id = k.id
        )
        left join (
            select
                Department.id as id,
                revenue as Dec_Revenue
            from
                department
            where
                month = 'Dec'
        ) as l on zero.id = l.id
    )