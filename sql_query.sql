select 
    -- aux columns
    l.loan_id,
    l.date as loan_date,
    acc.date as acc_date,

    -- loean features
    l.amount as loan_amount,
    l.duration as loan_duration,

    -- account and client features
    TIMESTAMPDIFF(year, acc.date, now()) as acc_age,
    TIMESTAMPDIFF(year, c.birth_date, now()) as client_age,
    c.gender as client_gender,

    -- district features
    d.A2 as district_name,
    d.A3 as district_region,
    d.A4 as district_inhabitants,
    d.A11 as district_avg_salary,

    -- target
    case 
        when l.status in ('A', 'C') then 0 
        when l.status in ('B', 'D') then 1 
    end as bad_payer
from 
    loan l 
    left join account acc on l.account_id = acc.account_id
    left join disp on (acc.account_id = disp.account_id and disp.type = 'owner')
    left join client c on disp.client_id = c.client_id
    left join district d on acc.district_id = d.district_id