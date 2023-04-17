use testtahlil;

insert into testtahlil.auth_user (email,password,username,date_joined)
select email,password,Owner,now() from tahlil_project.auth_barber where id > 6;

alter table auth_user alter is_superuser set default '0';
alter table auth_user alter is_staff set default '0';
alter table auth_user alter is_active set default '1';
alter table auth_user alter first_name set default '';
alter table auth_user alter last_name set default '';
/*alter table auth_user alter username set default 'user';*/

alter table barber_barber alter area set default 'areax';
alter table barber_barber alter background set default 'default_profile.png';
alter table barber_barber alter logo set default 'default_profile.png';
   
insert into testtahlil.barber_barber
 (BarberShop,Owner,Parvaneh,phone_Number,address,rate,user_id)
select BarberShop,Owner,Parvaneh,phone_Number,address,rate,id
from tahlil_project.barber_barber where id > 6;