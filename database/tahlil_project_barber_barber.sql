-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: tahlil_project
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `barber_barber`
--

DROP TABLE IF EXISTS `barber_barber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `barber_barber` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `BarberShop` varchar(255) NOT NULL,
  `Owner` varchar(255) NOT NULL,
  `Parvaneh` varchar(10) NOT NULL,
  `phone_Number` varchar(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` varchar(255) NOT NULL,
  `rate` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Parvaneh` (`Parvaneh`),
  UNIQUE KEY `phone_Number` (`phone_Number`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `Barber_barber_BarberShop_db673b7d_uniq` (`BarberShop`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `barber_barber`
--

LOCK TABLES `barber_barber` WRITE;
/*!40000 ALTER TABLE `barber_barber` DISABLE KEYS */;
INSERT INTO `barber_barber` VALUES (1,'barb1','owner1','12345','09912240401','barb1@domain.com','address1',3.7),(2,'barb2','owner2','123456','09912240402','barb2@domain.com','address2',3.3),(3,'barb3','owner3','1234567','09912240403','barb3@domain.com','address3',2.8),(4,'McCullough-Beier','Gasparo Stichall','','9761594106','gstichall3@mozilla.org','9247 Loftsgordon Alley',3.5),(5,'Jenkins Inc','Bamby Fear','7841321583','3391328573','bfear4@mtv.com','0 Utah Alley',4),(6,'Runolfsson, Johnson and Herzog','Bibi Gilderoy','4329137402','6051355536','bgilderoy5@nature.com','04667 Pine View Junction',3),(7,'Ullrich-Wiegand','Hill Gummer','3436078620','4083970991','hgummer6@4shared.com','579 Acker Junction',3),(8,'Ziemann and Sons','Brade Bowra','5189621122','8347193490','bbowra7@ycombinator.com','42169 Havey Place',3),(9,'Conn LLC','Peri Tollet','9544322949','7555992001','ptollet8@furl.net','52 International Crossing',4),(10,'Batz-Predovic','Carlee Flescher','6081769281','9049445489','cflescher9@trellian.com','1 Declaration Park',1),(11,'Kunze-Feest','Kristy Andreaccio','9018408487','8255323543','kandreaccioa@lycos.com','72623 Sunnyside Court',1.5),(12,'Block-Turcotte','Lamar Applebee','7585340026','6132770535','lapplebeeb@fastcompany.com','5 Bluestem Park',3.5),(13,'Crooks, Jenkins and Willms','Keeley Meas','3064981726','4783897994','kmeasc@ox.ac.uk','59 Kennedy Lane',5),(14,'Murazik LLC','Charmian Ropkes','1155804669','8889659610','cropkesd@canalblog.com','59182 Declaration Center',4),(15,'Graham, Schneider and Vandervort','Cathrin Duran','5127806933','7804619855','cdurane@histats.com','1 Hazelcrest Alley',2.8),(16,'Hoeger and Sons','Ray Whissell','9632359734','7599238569','rwhissellf@github.io','06 Steensland Junction',4),(17,'Little Inc','Monica Holborn','9063448627','3923859485','mholborng@yellowpages.com','3367 Burning Wood Park',4),(18,'Stoltenberg Inc','Elwira Reddle','5928688296','6712490570','ereddleh@google.com.br','25 Cottonwood Hill',3.3),(19,'Reilly LLC','Halie Aguilar','9841001610','7196966546','haguilari@github.io','9394 Hudson Trail',3.8),(20,'Nienow, Lowe and Veum','Bartie Barlthrop','2921442735','1662429939','bbarlthropj@simplemachines.org','90 Jackson Park',1.5),(21,'Schaefer-Legros','Lonnard Daniells','1163072205','4177714393','ldaniellsk@tiny.cc','7 Luster Terrace',1),(22,'Borer, Price and Mueller','Forrest Redemile','9219221548','5513829808','fredemilel@google.pl','4 Heffernan Drive',2),(23,'Paucek and Sons','Finlay McGaughey','1174494826','9045055018','fmcgaugheym@bbc.co.uk','6 Kensington Crossing',1),(24,'Hamill, Cronin and Macejkovic','Dunn Duffield','3112322586','5331448364','dduffieldn@sphinn.com','764 Swallow Lane',3.2),(25,'Beahan-Mueller','Grenville Turgoose','4165357701','1476994163','gturgooseo@virginia.edu','34 Forest Dale Avenue',3),(26,'Reichert-Robel','Hershel Lonsdale','7067563417','2344804927','hlonsdalep@unicef.org','07720 Shoshone Park',1),(27,'O\'Reilly-Harvey','Klarika McLafferty','2904671601','8104140221','kmclaffertyq@hugedomains.com','009 Troy Park',1),(28,'Johns and Sons','Hilliary Cowern','1618080889','5202357679','hcowernr@ucla.edu','71 Claremont Point',3),(29,'Ernser Inc','Lissi Poley','4933370106','8766396303','lpoleys@ucsd.edu','3 Fieldstone Circle',4),(30,'Hegmann-Raynor','Stearne Jaukovic','6993672968','9871536831','sjaukovict@topsy.com','113 Hayes Alley',4);
/*!40000 ALTER TABLE `barber_barber` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-10 23:39:48
