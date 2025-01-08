CREATE TABLE service1(
    id_service serial primary key,
    kode_service VARCHAR(15) NOT NULL UNIQUE,
    jenis_service varchar(30) NOT NULL,
    harga INTEGER NOT NULL,
    merek varchar(20) NOT NULL);