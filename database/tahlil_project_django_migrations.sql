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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-04-07 17:16:19.380510'),(2,'contenttypes','0002_remove_content_type_name','2023-04-07 17:16:19.443702'),(3,'auth','0001_initial','2023-04-07 17:16:19.807429'),(4,'auth','0002_alter_permission_name_max_length','2023-04-07 17:16:19.854912'),(5,'auth','0003_alter_user_email_max_length','2023-04-07 17:16:19.873856'),(6,'auth','0004_alter_user_username_opts','2023-04-07 17:16:19.882380'),(7,'auth','0005_alter_user_last_login_null','2023-04-07 17:16:19.942909'),(8,'auth','0006_require_contenttypes_0002','2023-04-07 17:16:19.946585'),(9,'auth','0007_alter_validators_add_error_messages','2023-04-07 17:16:19.955521'),(10,'auth','0008_alter_user_username_max_length','2023-04-07 17:16:20.002782'),(11,'auth','0009_alter_user_last_name_max_length','2023-04-07 17:16:20.061780'),(12,'auth','0010_alter_group_name_max_length','2023-04-07 17:16:20.083819'),(13,'auth','0011_update_proxy_permissions','2023-04-07 17:16:20.096620'),(14,'auth','0012_alter_user_first_name_max_length','2023-04-07 17:16:20.156125'),(15,'Auth','0001_initial','2023-04-07 17:16:20.551775'),(16,'Auth','0002_remove_barber_region_remove_customer_region','2023-04-07 17:16:20.603912'),(17,'Auth','0003_alter_barber_owner','2023-04-07 17:16:20.616428'),(18,'admin','0001_initial','2023-04-07 17:16:20.750156'),(19,'admin','0002_logentry_remove_auto_add','2023-04-07 17:16:20.758787'),(20,'admin','0003_logentry_add_action_flag_choices','2023-04-07 17:16:20.769828'),(21,'sessions','0001_initial','2023-04-07 17:16:20.806478'),(22,'Barber','0001_initial','2023-04-07 17:20:55.021043'),(23,'Barber','0002_alter_barber_barbershop_rate','2023-04-07 17:20:55.086732'),(24,'Barber','0003_alter_rate_barbershop','2023-04-07 17:20:55.091645'),(25,'Barber','0004_alter_rate_barbershop','2023-04-07 17:20:55.175543'),(26,'Barber','0005_barber_rate','2023-04-07 17:20:55.202517'),(27,'Barber','0006_alter_barber_rate','2023-04-07 17:20:55.210303'),(28,'Barber','0007_remove_barber_rate','2023-04-07 17:20:55.234041'),(29,'Barber','0008_barber_rate','2023-04-07 17:20:55.251801'),(30,'Barber','0009_remove_barber_rate','2023-04-07 17:20:55.271619'),(31,'Barber','0010_barber_rate','2023-04-07 17:20:55.292612'),(32,'Barber','0011_alter_barber_rate','2023-04-07 17:20:55.367504'),(33,'Barber','0012_remove_barber_rate','2023-04-07 17:20:55.384567'),(34,'Barber','0013_barber_rate','2023-04-07 17:20:55.416156'),(35,'Barber','0014_remove_barber_rate','2023-04-07 17:20:55.437754'),(36,'Barber','0015_barber_rate','2023-04-07 17:20:55.475958'),(37,'Barber','0016_remove_barber_rate','2023-04-07 17:20:55.493866'),(38,'Barber','0017_barber_rate','2023-04-07 17:20:55.522831'),(39,'Barber','0018_remove_barber_rate','2023-04-07 17:20:55.544049'),(40,'Barber','0019_barber_rate','2023-04-07 17:20:55.576235'),(41,'Barber','0020_alter_barber_rate','2023-04-07 17:20:55.584747'),(42,'Barber','0021_alter_barber_rate','2023-04-07 17:27:34.707644'),(43,'Barber','0022_remove_barber_rate','2023-04-07 17:28:28.561301'),(44,'Barber','0023_barber_rate','2023-04-07 17:28:50.930466'),(45,'Barber','0024_alter_rate_stars','2023-04-07 17:31:51.572649'),(46,'Barber','0021_alter_barber_rate_alter_rate_stars_barbershopimages','2023-04-08 12:09:51.926960'),(47,'Auth','0003_alter_customer_password','2023-04-09 19:27:16.775675'),(48,'Auth','0004_alter_customer_password','2023-04-09 19:37:53.080882');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
