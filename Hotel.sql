-- MariaDB dump 10.17  Distrib 10.4.11-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: Hotel
-- ------------------------------------------------------
-- Server version	10.4.11-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Admin`
--

DROP TABLE IF EXISTS `Admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin` (
  `id_admin` int(11) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`id_admin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin`
--

LOCK TABLES `Admin` WRITE;
/*!40000 ALTER TABLE `Admin` DISABLE KEYS */;
INSERT INTO `Admin` VALUES (101,'admin','admin123'),(102,'andika','andika1999');
/*!40000 ALTER TABLE `Admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Kamar`
--

DROP TABLE IF EXISTS `Kamar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Kamar` (
  `no_kamar` int(11) NOT NULL,
  `id_tamuFK` int(11) DEFAULT NULL,
  `jenis_kamar` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`no_kamar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Kamar`
--

LOCK TABLES `Kamar` WRITE;
/*!40000 ALTER TABLE `Kamar` DISABLE KEYS */;
INSERT INTO `Kamar` VALUES (201,108,'Ekonomi'),(202,109,'VVIP'),(203,110,'Ekonomi');
/*!40000 ALTER TABLE `Kamar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tamu`
--

DROP TABLE IF EXISTS `Tamu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Tamu` (
  `id_tamu` int(11) NOT NULL,
  `nama_tamu` varchar(45) NOT NULL,
  `alamat` varchar(255) NOT NULL,
  PRIMARY KEY (`id_tamu`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tamu`
--

LOCK TABLES `Tamu` WRITE;
/*!40000 ALTER TABLE `Tamu` DISABLE KEYS */;
INSERT INTO `Tamu` VALUES (101,'Herman Agus','Jl. Diponegoro No.23 Surakarta'),(103,'Rahmat Khorimudin','Jl. Majapahit No.15 Jakarta'),(105,'Arga Ardinata','Jl. Yani No.25'),(106,'Khamar Rudin','Jl. Diponegoro No.23 Jakarta'),(107,'Bukamin','Jl. Arjuno No.48 Bekasi'),(108,'Agus Triono','Jl. Kelapa Sawit No.25 Bekasi'),(109,'Nurhadi','Jl. Diponegoro No.4 Palangkaraya'),(110,'Qodir','Jl. Ahmad Yani No.25 Surakarta');
/*!40000 ALTER TABLE `Tamu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transaksi`
--

DROP TABLE IF EXISTS `Transaksi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Transaksi` (
  `id_transaksi` int(11) NOT NULL,
  `id_tamuFK` int(11) DEFAULT NULL,
  `no_kamarFK` int(11) DEFAULT NULL,
  `tanggal_in` date DEFAULT NULL,
  `tanggal_out` date DEFAULT NULL,
  `check_in` date DEFAULT NULL,
  `check_out` date DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_transaksi`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transaksi`
--

LOCK TABLES `Transaksi` WRITE;
/*!40000 ALTER TABLE `Transaksi` DISABLE KEYS */;
INSERT INTO `Transaksi` VALUES (301,101,201,'2020-07-03','2020-07-03','2020-06-25','2020-06-25',400000),(303,103,203,'2020-07-03','2020-07-03','2020-06-25','2020-06-25',400000),(305,105,206,'2020-06-25','2020-06-28','2020-06-25','2020-06-25',300000),(306,106,207,'2020-07-03','2020-07-04','2020-07-03','2020-07-03',300000),(307,107,208,'2020-07-04','2020-07-05','2020-07-03','2020-07-03',400000),(308,108,201,'2020-07-03','2020-07-04','2020-07-03',NULL,300000),(309,109,202,'2020-07-03','2020-07-04',NULL,NULL,400000),(310,110,203,'2020-07-04','2020-07-05',NULL,NULL,300000);
/*!40000 ALTER TABLE `Transaksi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `admin_view`
--

DROP TABLE IF EXISTS `admin_view`;
/*!50001 DROP VIEW IF EXISTS `admin_view`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `admin_view` (
  `username` tinyint NOT NULL,
  `password` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `admin_view`
--

/*!50001 DROP TABLE IF EXISTS `admin_view`*/;
/*!50001 DROP VIEW IF EXISTS `admin_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `admin_view` AS select `Admin`.`username` AS `username`,`Admin`.`password` AS `password` from `Admin` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-15 10:31:00
