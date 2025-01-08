create table pelayanan(
    id_pelayanan serial primary key,
    kode_pelayanan varchar(15) NOT NULL UNIQUE,
    jasa_pelayanan varchar(20) NOT NULL,
    jenis_kendaraan varchar(20) NOT NULL,
    id_service  integer, 
    CONSTRAINT id_service
    FOREIGN KEY (id_service)
        REFERENCES service1(id_service)
        ON UPDATE CASCADE ON DELETE RESTRICT
);