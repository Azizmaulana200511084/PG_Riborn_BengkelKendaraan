create table petugas(
    id_petugas serial primary key,
    nama_petugas varchar(100) NOT NULL UNIQUE,
    pssword1 varchar(100) NOT NULL,
    no_telp varchar(100) NOT NULL,
    email_petugas varchar(100) NOT NULL,
    rolename varchar(100) NOT NULL);