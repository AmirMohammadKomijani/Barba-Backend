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
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-04-15 20:38:11.967303'),(2,'auth','0001_initial','2023-04-15 20:38:12.137541'),(3,'Barber','0001_initial','2023-04-15 20:38:12.149436'),(4,'Barber','0002_alter_barber_barbershop_rate','2023-04-15 20:38:12.179176'),(5,'Barber','0003_alter_rate_barbershop','2023-04-15 20:38:12.183627'),(6,'Barber','0004_alter_rate_barbershop','2023-04-15 20:38:12.229099'),(7,'Barber','0005_barber_rate','2023-04-15 20:38:12.246539'),(8,'Barber','0006_alter_barber_rate','2023-04-15 20:38:12.250567'),(9,'Barber','0007_remove_barber_rate','2023-04-15 20:38:12.262583'),(10,'Barber','0008_barber_rate','2023-04-15 20:38:12.274675'),(11,'Barber','0009_remove_barber_rate','2023-04-15 20:38:12.287878'),(12,'Barber','0010_barber_rate','2023-04-15 20:38:12.300768'),(13,'Barber','0011_alter_barber_rate','2023-04-15 20:38:12.336415'),(14,'Barber','0012_remove_barber_rate','2023-04-15 20:38:12.347438'),(15,'Barber','0013_barber_rate','2023-04-15 20:38:12.368266'),(16,'Barber','0014_remove_barber_rate','2023-04-15 20:38:12.381939'),(17,'Barber','0015_barber_rate','2023-04-15 20:38:12.403077'),(18,'Barber','0016_remove_barber_rate','2023-04-15 20:38:12.416299'),(19,'Barber','0017_barber_rate','2023-04-15 20:38:12.435490'),(20,'Barber','0018_remove_barber_rate','2023-04-15 20:38:12.448276'),(21,'Barber','0019_barber_rate','2023-04-15 20:38:12.469312'),(22,'Barber','0020_alter_barber_rate','2023-04-15 20:38:12.472901'),(23,'Barber','0021_alter_barber_rate_alter_rate_stars_barbershopimages','2023-04-15 20:38:12.517304'),(24,'Barber','0022_barber_user','2023-04-15 20:38:12.558785'),(25,'Barber','0023_barber_area_barber_background_barber_logo','2023-04-15 20:38:12.630560'),(26,'Barber','0024_delete_barbershopimages','2023-04-15 20:38:12.639658'),(27,'Customer','0001_initial','2023-04-15 20:38:12.652440'),(28,'Customer','0002_customer_delete_customerprofile','2023-04-15 20:38:12.686681'),(29,'admin','0001_initial','2023-04-15 20:38:12.737197'),(30,'admin','0002_logentry_remove_auto_add','2023-04-15 20:38:12.743625'),(31,'admin','0003_logentry_add_action_flag_choices','2023-04-15 20:38:12.751587'),(32,'contenttypes','0002_remove_content_type_name','2023-04-15 20:38:12.790287'),(33,'auth','0002_alter_permission_name_max_length','2023-04-15 20:38:12.818396'),(34,'auth','0003_alter_user_email_max_length','2023-04-15 20:38:12.840913'),(35,'auth','0004_alter_user_username_opts','2023-04-15 20:38:12.849017'),(36,'auth','0005_alter_user_last_login_null','2023-04-15 20:38:12.879020'),(37,'auth','0006_require_contenttypes_0002','2023-04-15 20:38:12.881873'),(38,'auth','0007_alter_validators_add_error_messages','2023-04-15 20:38:12.890335'),(39,'auth','0008_alter_user_username_max_length','2023-04-15 20:38:12.921672'),(40,'auth','0009_alter_user_last_name_max_length','2023-04-15 20:38:12.952810'),(41,'auth','0010_alter_group_name_max_length','2023-04-15 20:38:12.968939'),(42,'auth','0011_update_proxy_permissions','2023-04-15 20:38:12.977281'),(43,'auth','0012_alter_user_first_name_max_length','2023-04-15 20:38:13.008608'),(44,'sessions','0001_initial','2023-04-15 20:38:13.026292'),(45,'Barber','0025_remove_barber_email','2023-04-15 21:11:31.733272'),(46,'Barber','0026_alter_barber_background_alter_barber_logo','2023-04-16 06:42:25.474029'),(47,'Customer','0003_customer_first_name_customer_last_name_and_more','2023-04-16 06:42:25.516596'),(48,'Customer','0004_alter_customer_profile_pic','2023-04-16 07:06:51.635045'),(49,'Barber','0027_alter_barber_user','2023-04-16 12:08:29.176260'),(50,'Barber','0028_alter_barber_user','2023-04-16 12:10:01.644027'),(51,'Barber','0029_alter_barber_user','2023-04-16 12:12:31.188760'),(52,'Barber','0030_alter_barber_background_alter_barber_logo','2023-04-16 17:11:53.816396'),(53,'Barber','0031_alter_barber_background_alter_barber_logo','2023-04-16 17:26:04.100337'),(54,'Barber','0032_alter_barber_user','2023-04-16 17:48:36.841809'),(55,'Barber','0033_alter_barber_user','2023-04-16 17:56:57.160869'),(56,'Barber','0034_alter_barber_area','2023-04-16 18:59:44.051221'),(57,'Barber','0035_alter_barber_barbershop_alter_barber_owner_and_more','2023-04-16 19:44:25.433591'),(58,'Barber','0036_alter_barber_barbershop_alter_barber_owner_and_more','2023-04-16 20:49:06.223996');
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

-- Dump completed on 2023-04-17 16:34:16
