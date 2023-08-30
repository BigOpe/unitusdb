DROP DATABASE IF EXISTS `mydatabase`;
CREATE DATABASE `mydatabase`; 
USE `mydatabase`;

SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;

CREATE TABLE `unitus__profile`(
					'id' bigint not null auto_increment,
                   'name' varchar (50) not null)
                   

CREATE TABLE 'unitus__user' (
                    'id' bigint not null auto_increment
					primary key,
					'firstname' varchar (50) not null,
                    'lastname' varchar (50) not null,
                    'cf' varchar (16) unique index not null,
                    'email_p' varchar (100) unique not null,
                    'email_u' varchar (100) unique not null,
                    'mobile' bigint unique not null,
                    'department' int (2) not null,
                    'profile' int (2) not null,
                    'expired' boolean not null)
                    
create table 'unitus__department' (
                   'id' int auto_increment not null
                   primary key,
                   'name' varchar (10) not null)
                   
create table 'unitus__test' (
					'id' bigint auto_increment not null primary
                    key,
                    'ay' int (4) not null,
                    'date' date not null,
                    'online' boolean not null)
		
create table 'unitus__macroaree' (
                     'id' bigint auto_increment not null
                     primary key,
                     'name' varchar (50) not null)
                     
create table 'unitus__macroaree_test' (
					'id' bigint not null auto_increment
                    primary key,
                    'id_test' bigint not null,
                    'id_macroaree' bigint not null)
                    
create table 'unitus__availability' (
                    'id' bigint auto_increment not null 
                    primary key,
                    'id_test' bigint not null,
                    'id_user' bigint not null,
                    'involved' boolean,
                    'rate' int)
                    
             