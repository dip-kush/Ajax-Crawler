-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 09, 2015 at 12:27 PM
-- Server version: 5.6.16
-- PHP Version: 5.5.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `forum`
--

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `feedback` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=41 ;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`id`, `name`, `feedback`) VALUES
(25, 'vishal', ' hello'),
(26, 'vishal', ' hello'),
(27, 'vishal', ' hello'),
(28, 'vishal', ' hello'),
(29, 'vishal', ' hello'),
(30, 'vishal', ' hello'),
(31, 'vishal', ' hello'),
(32, 'vishal', ' hello'),
(33, 'vishal', ' hello'),
(34, 'vishal', ' hello'),
(35, 'vishal', ' hello'),
(36, 'vishal', ' hello'),
(37, 'vishal', ' hello'),
(38, 'vishal', ' hello'),
(39, 'vishal', ' hello'),
(40, 'vishal', ' hello');

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE IF NOT EXISTS `members` (
  `Memberid` int(10) NOT NULL AUTO_INCREMENT,
  `Username` varchar(20) NOT NULL,
  `Email` varchar(20) NOT NULL,
  `Password` varchar(10) NOT NULL,
  `Activation` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`Memberid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`Memberid`, `Username`, `Email`, `Password`, `Activation`) VALUES
(21, 'dipkush', 'dip.kush', 'dkool', NULL),
(22, 'Vinay Sharma', 'vinaysharma@gmail', 'vinaykool', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `submit`
--

CREATE TABLE IF NOT EXISTS `submit` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=25 ;

--
-- Dumping data for table `submit`
--

INSERT INTO `submit` (`id`, `name`) VALUES
(9, 'vishal'),
(10, 'vishal'),
(11, 'vishal'),
(12, 'vishal'),
(13, 'vishal'),
(14, 'vishal'),
(15, 'vishal'),
(16, 'vishal'),
(17, 'vishal'),
(18, 'vishal'),
(19, 'vishal'),
(20, 'vishal'),
(21, 'vishal'),
(22, 'vishal'),
(23, 'vishal'),
(24, 'vishal');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
