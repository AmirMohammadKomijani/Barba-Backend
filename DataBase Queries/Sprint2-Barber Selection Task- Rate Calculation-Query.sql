use tahlil_project;


-- this query is implemented for barber tables.
insert into barber_barber(id, BarberShop, Owner, Parvaneh, phone_Number, email, address)
select id,BarberShop, Owner, Parvaneh, phone_Number, email, address
from auth_barber;


-- this query is designed for calculating rate of each barbershop

SET SQL_SAFE_UPDATES=0;
UPDATE barber_barber
JOIN (
    SELECT barber_rate.barbershop_id, AVG(barber_rate.stars) AS avg_stars
    FROM barber_rate
    GROUP BY barber_rate.barbershop_id
) AS subquery
ON barber_barber.id = subquery.barbershop_id
SET barber_barber.rate = ROUND(FORMAT(subquery.avg_stars,2));
SET SQL_SAFE_UPDATES=1;
/*select * from barber_barber*/
