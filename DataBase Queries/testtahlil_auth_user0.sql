-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: testtahlil
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
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
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
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$YT8fd2Qfa0j5oCqvMAXSux$epKOhMueIvQEXMuZZYOMNXSdv80qeLsQPfgcgdEoMRQ=',NULL,0,'barber1','barberFname','barberLname','barb1@domain.com',0,1,'2023-04-15 19:48:34.887894','barber'),(3,'pbkdf2_sha256$600000$fzRJth18CwQCpEstythjlt$PSntWArB2ZjvmPSR2SjtrTU5b/liz66Wjz8BHEXMdnc=',NULL,0,'barber2-1','','','barb2@domain.com',0,1,'2023-04-15 19:49:53.626841','barber'),(4,'pbkdf2_sha256$600000$e4FadfkKwrquSCTFjK4mJZ$o/nslJgTxa5oHP1g0nRA/rGvdEvSIbtjnrHa5YNlpgk=',NULL,0,'user2','','','barb3@domain.com',0,1,'2023-04-16 06:28:14.466366','customer'),(5,'pbkdf2_sha256$600000$AZznqSvrrAWzTbKPgtNwa5$TrwuM6oP+hrOLVkbU6+MfL0Q3kSnBaqdCi9MWMJ/vPc=',NULL,0,'user4','','','customer1@domain.com',0,1,'2023-04-16 06:36:46.024209','barber'),(6,'pbkdf2_sha256$600000$riXmogPvOUvj7ZZdyMPY8L$9EBSZhqWeO+6CuHUSOJ5XLO0UdsVL7QGJQKV6YDiS14=',NULL,0,'user5','','','customer2@domain.com',0,1,'2023-04-16 06:48:27.896656','customer'),(7,'barb7',NULL,0,'Hill Gummer','','','hgummer6@4shared.com',0,1,'2023-04-17 15:59:52.000000','barber'),(8,'barb8',NULL,0,'Brade Bowra','','','bbowra7@ycombinator.com',0,1,'2023-04-17 15:59:52.000000','barber'),(9,'barb9',NULL,0,'Peri Tollet','','','ptollet8@furl.net',0,1,'2023-04-17 15:59:52.000000','barber'),(10,'barb10',NULL,0,'Carlee Flescher','','','cflescher9@trellian.com',0,1,'2023-04-17 15:59:52.000000','barber'),(11,'barb11',NULL,0,'Kristy Andreaccio','','','kandreaccioa@lycos.com',0,1,'2023-04-17 15:59:52.000000','barber'),(12,'barb12',NULL,0,'Lamar Applebee','','','lapplebeeb@fastcompany.com',0,1,'2023-04-17 15:59:52.000000','barber'),(13,'barb13',NULL,0,'Keeley Meas','','','kmeasc@ox.ac.uk',0,1,'2023-04-17 15:59:52.000000','barber'),(14,'barb14',NULL,0,'Charmian Ropkes','','','cropkesd@canalblog.com',0,1,'2023-04-17 15:59:52.000000','barber'),(15,'barb15',NULL,0,'Cathrin Duran','','','cdurane@histats.com',0,1,'2023-04-17 15:59:52.000000','barber'),(16,'barb16',NULL,0,'Ray Whissell','','','rwhissellf@github.io',0,1,'2023-04-17 15:59:52.000000','barber'),(17,'barb17',NULL,0,'Monica Holborn','','','mholborng@yellowpages.com',0,1,'2023-04-17 15:59:52.000000','barber'),(18,'barb18',NULL,0,'Elwira Reddle','','','ereddleh@google.com.br',0,1,'2023-04-17 15:59:52.000000','barber'),(19,'barb19',NULL,0,'Halie Aguilar','','','haguilari@github.io',0,1,'2023-04-17 15:59:52.000000','barber'),(20,'barb20',NULL,0,'Bartie Barlthrop','','','bbarlthropj@simplemachines.org',0,1,'2023-04-17 15:59:52.000000','barber'),(21,'barb21',NULL,0,'Lonnard Daniells','','','ldaniellsk@tiny.cc',0,1,'2023-04-17 15:59:52.000000','barber'),(22,'barb22',NULL,0,'Forrest Redemile','','','fredemilel@google.pl',0,1,'2023-04-17 15:59:52.000000','barber'),(23,'barb23',NULL,0,'Finlay McGaughey','','','fmcgaugheym@bbc.co.uk',0,1,'2023-04-17 15:59:52.000000','barber'),(24,'barb24',NULL,0,'Dunn Duffield','','','dduffieldn@sphinn.com',0,1,'2023-04-17 15:59:52.000000','barber'),(25,'barb25',NULL,0,'Grenville Turgoose','','','gturgooseo@virginia.edu',0,1,'2023-04-17 15:59:52.000000','barber'),(26,'barb26',NULL,0,'Hershel Lonsdale','','','hlonsdalep@unicef.org',0,1,'2023-04-17 15:59:52.000000','barber'),(27,'barb27',NULL,0,'Klarika McLafferty','','','kmclaffertyq@hugedomains.com',0,1,'2023-04-17 15:59:52.000000','barber'),(28,'barb28',NULL,0,'Hilliary Cowern','','','hcowernr@ucla.edu',0,1,'2023-04-17 15:59:52.000000','barber'),(29,'barb29',NULL,0,'Lissi Poley','','','lpoleys@ucsd.edu',0,1,'2023-04-17 15:59:52.000000','barber'),(30,'barb30',NULL,0,'Stearne Jaukovic','','','sjaukovict@topsy.com',0,1,'2023-04-17 15:59:52.000000','barber');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-25 14:11:19
