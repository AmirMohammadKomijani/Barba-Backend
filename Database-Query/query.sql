
alter table auth_user add role varchar(8);

INSERT INTO `auth_user`(id,password,last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined,role)
 VALUES (1,'pbkdf2_sha256$600000$YT8fd2Qfa0j5oCqvMAXSux$epKOhMueIvQEXMuZZYOMNXSdv80qeLsQPfgcgdEoMRQ=',NULL,0,'barber1','barberFname','barberLname','barb1@domain.com',0,1,'2023-04-15 19:48:34.887894','barber'),(3,'pbkdf2_sha256$600000$fzRJth18CwQCpEstythjlt$PSntWArB2ZjvmPSR2SjtrTU5b/liz66Wjz8BHEXMdnc=',NULL,0,'barber2-1','','','barb2@domain.com',0,1,'2023-04-15 19:49:53.626841','barber'),(4,'pbkdf2_sha256$600000$e4FadfkKwrquSCTFjK4mJZ$o/nslJgTxa5oHP1g0nRA/rGvdEvSIbtjnrHa5YNlpgk=',NULL,0,'user2','','','barb3@domain.com',0,1,'2023-04-16 06:28:14.466366','customer'),(5,'pbkdf2_sha256$600000$AZznqSvrrAWzTbKPgtNwa5$TrwuM6oP+hrOLVkbU6+MfL0Q3kSnBaqdCi9MWMJ/vPc=',NULL,0,'user4','','','customer1@domain.com',0,1,'2023-04-16 06:36:46.024209','barber'),(6,'pbkdf2_sha256$600000$riXmogPvOUvj7ZZdyMPY8L$9EBSZhqWeO+6CuHUSOJ5XLO0UdsVL7QGJQKV6YDiS14=',NULL,0,'user5','','','customer2@domain.com',0,1,'2023-04-16 06:48:27.896656','customer'),(7,'barb7',NULL,0,'Hill Gummer','','','hgummer6@4shared.com',0,1,'2023-04-17 15:59:52.000000','barber'),(8,'barb8',NULL,0,'Brade Bowra','','','bbowra7@ycombinator.com',0,1,'2023-04-17 15:59:52.000000','barber'),(9,'barb9',NULL,0,'Peri Tollet','','','ptollet8@furl.net',0,1,'2023-04-17 15:59:52.000000','barber'),(10,'barb10',NULL,0,'Carlee Flescher','','','cflescher9@trellian.com',0,1,'2023-04-17 15:59:52.000000','barber'),(11,'barb11',NULL,0,'Kristy Andreaccio','','','kandreaccioa@lycos.com',0,1,'2023-04-17 15:59:52.000000','barber'),(12,'barb12',NULL,0,'Lamar Applebee','','','lapplebeeb@fastcompany.com',0,1,'2023-04-17 15:59:52.000000','barber'),(13,'barb13',NULL,0,'Keeley Meas','','','kmeasc@ox.ac.uk',0,1,'2023-04-17 15:59:52.000000','barber'),(14,'barb14',NULL,0,'Charmian Ropkes','','','cropkesd@canalblog.com',0,1,'2023-04-17 15:59:52.000000','barber'),(15,'barb15',NULL,0,'Cathrin Duran','','','cdurane@histats.com',0,1,'2023-04-17 15:59:52.000000','barber'),(16,'barb16',NULL,0,'Ray Whissell','','','rwhissellf@github.io',0,1,'2023-04-17 15:59:52.000000','barber'),(17,'barb17',NULL,0,'Monica Holborn','','','mholborng@yellowpages.com',0,1,'2023-04-17 15:59:52.000000','barber'),(18,'barb18',NULL,0,'Elwira Reddle','','','ereddleh@google.com.br',0,1,'2023-04-17 15:59:52.000000','barber'),(19,'barb19',NULL,0,'Halie Aguilar','','','haguilari@github.io',0,1,'2023-04-17 15:59:52.000000','barber'),(20,'barb20',NULL,0,'Bartie Barlthrop','','','bbarlthropj@simplemachines.org',0,1,'2023-04-17 15:59:52.000000','barber'),(21,'barb21',NULL,0,'Lonnard Daniells','','','ldaniellsk@tiny.cc',0,1,'2023-04-17 15:59:52.000000','barber'),(22,'barb22',NULL,0,'Forrest Redemile','','','fredemilel@google.pl',0,1,'2023-04-17 15:59:52.000000','barber'),(23,'barb23',NULL,0,'Finlay McGaughey','','','fmcgaugheym@bbc.co.uk',0,1,'2023-04-17 15:59:52.000000','barber'),(24,'barb24',NULL,0,'Dunn Duffield','','','dduffieldn@sphinn.com',0,1,'2023-04-17 15:59:52.000000','barber'),(25,'barb25',NULL,0,'Grenville Turgoose','','','gturgooseo@virginia.edu',0,1,'2023-04-17 15:59:52.000000','barber'),(26,'barb26',NULL,0,'Hershel Lonsdale','','','hlonsdalep@unicef.org',0,1,'2023-04-17 15:59:52.000000','barber'),(27,'barb27',NULL,0,'Klarika McLafferty','','','kmclaffertyq@hugedomains.com',0,1,'2023-04-17 15:59:52.000000','barber'),(28,'barb28',NULL,0,'Hilliary Cowern','','','hcowernr@ucla.edu',0,1,'2023-04-17 15:59:52.000000','barber'),(29,'barb29',NULL,0,'Lissi Poley','','','lpoleys@ucsd.edu',0,1,'2023-04-17 15:59:52.000000','barber'),(30,'barb30',NULL,0,'Stearne Jaukovic','','','sjaukovict@topsy.com',0,1,'2023-04-17 15:59:52.000000','barber');
DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `role` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE (`username`)
);

alter table auth_user
add expire_date datetime(6);

UPDATE auth_user
SET expire_date = strftime('%Y-%m-%d', date_joined, '+2 months')
WHERE id > 0;
---------------------------------------------------------------

INSERT INTO `barber_barber` (id,BarberShop,Owner,Parvaneh,phone_Number,address,rate,user_id,area,background,logo)
VALUES (1,'barbershop1','owner1','123','09912240419','address1',1,1,'Tehranpars','default_profile.png','default_profile.png'),(2,'barbershop2','owner2','12345','09912240404','address3',1,3,'Nazi Abad','default_profile.png','default_profile.png'),(3,'barb3','owner3','3143413','09912240403','address3',1,4,'Narmak','default_profile.png','default_profile.png'),(4,'Ullrich-Wiegand','Hill Gummer','3436078620','4083970991','579 Acker Junction',3,7,'Tajrish','default_profile.png','default_profile.png'),(5,'Ziemann and Sons','Brade Bowra','5189621122','8347193490','42169 Havey Place',3,8,'Gheytariye','default_profile.png','default_profile.png'),(6,'Conn LLC','Peri Tollet','9544322949','7555992001','52 International Crossing',4,9,'Marzdaran','default_profile.png','default_profile.png'),(7,'Batz-Predovic','Carlee Flescher','6081769281','9049445489','1 Declaration Park',1,10,'Janat Abad','default_profile.png','default_profile.png'),(8,'Kunze-Feest','Kristy Andreaccio','9018408487','8255323543','72623 Sunnyside Court',1.5,11,'Vanak','default_profile.png','default_profile.png'),(9,'Block-Turcotte','Lamar Applebee','7585340026','6132770535','5 Bluestem Park',3.5,12,'Enghelab','default_profile.png','default_profile.png'),(10,'Crooks, Jenkins and Willms','Keeley Meas','3064981726','4783897994','59 Kennedy Lane',5,13,'Valiasr','default_profile.png','default_profile.png'),(11,'Murazik LLC','Charmian Ropkes','1155804669','8889659610','59182 Declaration Center',4,14,'Saadat Abad','default_profile.png','default_profile.png'),(12,'Graham, Schneider and Vandervort','Cathrin Duran','5127806933','7804619855','1 Hazelcrest Alley',2.8,15,'Piroozi','default_profile.png','default_profile.png'),(13,'Hoeger and Sons','Ray Whissell','9632359734','7599238569','06 Steensland Junction',4,16,'Jordan','default_profile.png','default_profile.png'),(14,'Little Inc','Monica Holborn','9063448627','3923859485','3367 Burning Wood Park',4,17,'Tehranpars','default_profile.png','default_profile.png'),(15,'Stoltenberg Inc','Elwira Reddle','5928688296','6712490570','25 Cottonwood Hill',3.3,18,'Nazi Abad','default_profile.png','default_profile.png'),(16,'Reilly LLC','Halie Aguilar','9841001610','7196966546','9394 Hudson Trail',3.8,19,'Narmak','default_profile.png','default_profile.png'),(17,'Nienow, Lowe and Veum','Bartie Barlthrop','2921442735','1662429939','90 Jackson Park',1.5,20,'Tajrish','default_profile.png','default_profile.png'),(18,'Schaefer-Legros','Lonnard Daniells','1163072205','4177714393','7 Luster Terrace',1,21,'Gheytariye','default_profile.png','default_profile.png'),(19,'Borer, Price and Mueller','Forrest Redemile','9219221548','5513829808','4 Heffernan Drive',2,22,'Marzdaran','default_profile.png','default_profile.png'),(20,'Paucek and Sons','Finlay McGaughey','1174494826','9045055018','6 Kensington Crossing',1,23,'Janat Abad','default_profile.png','default_profile.png'),(21,'Hamill, Cronin and Macejkovic','Dunn Duffield','3112322586','5331448364','764 Swallow Lane',3.2,24,'Vanak','default_profile.png','default_profile.png'),(22,'Beahan-Mueller','Grenville Turgoose','4165357701','1476994163','34 Forest Dale Avenue',3,25,'Enghelab','default_profile.png','default_profile.png'),(23,'Reichert-Robel','Hershel Lonsdale','7067563417','2344804927','07720 Shoshone Park',1,26,'Valiasr','default_profile.png','default_profile.png'),(24,'Reilly-Harvey','Klarika McLafferty','2904671601','8104140221','009 Troy Park',1,27,'Saadat Abad','default_profile.png','default_profile.png'),(25,'Johns and Sons','Hilliary Cowern','1618080889','5202357679','71 Claremont Point',3,28,'Piroozi','default_profile.png','default_profile.png'),(26,'Ernser Inc','Lissi Poley','4933370106','8766396303','3 Fieldstone Circle',4,29,'Jordan','default_profile.png','default_profile.png'),(27,'Hegmann-Raynor','Stearne Jaukovic','6993672968','9871536831','113 Hayes Alley',4,30,'Tehranpars','default_profile.png','default_profile.png'),(28,'','','','','',1,31,'','default_profile.png','default_profile.png');
delete from Barber_barber where id > 0;
--------------------------------------------------------------



INSERT INTO `Customer_customer`(id,area,phone_Number,user_id,first_name,last_name,profile_pic,credit)
VALUES (1,'area1','09912240403',5,'cust1name','cust2name','default_profile.png',0.00),(2,'area2','09912240401',6,'cust2named','custlname','default_profile.png',0.00);


alter table Customer_customer
alter Customer_customer.credit set default 0.00;

delete from Customer_customer where id >= 1;

------------------------------------------------------



INSERT INTO `barber_service` VALUES (1,'hair dress',10,NULL,'hair',1),(17,'nail service',25,'','nail',1),(19,'make up',14,'','makeup',1);
--------------------------
INSERT INTO `barber_orderservices` VALUES (8,'14:40:00',1,2,1);
delete from barber_orderservices where id > 0;


-------------------------

delete from barber_category where id > 0;
delete from Barber_categoryservice where id > 0;
delete from Barber_barber where id = 29;
delete from Barber_service where id > 0;
delete from Barber_orderservices where Barber_orderservices.customer_id = 4;
delete from barber_categoryservice where id > 19;
delete from barber_category where id > 0;
delete from Barber_orderservices where id > 0;
update Barber_orderservices set status='ordering' where id>0;
delete from Customer_customer where id > 3;
delete from barber_barber where id = 29;
drop table barber_totalprice;
delete from barber_barberdescription where id > 0;