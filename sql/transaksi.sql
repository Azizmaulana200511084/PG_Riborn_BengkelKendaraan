CREATE TABLE transaksi(
    id_transaksi serial primary key,
    nomor_transaksi integer NOT NULL UNIQUE,
    nama_pelanggan varchar(20) NOT NULL,
    nomor_polisi varchar(10) NOT NULL,
    kode_pelayanan varchar(15) NOT NULL,
    waktu_pelayanan TIME NOT NULL,
    waktu_selesai TIME NOT NULL,
    tanggal_transaksi DATE NOT NULL,
    kode_service1 VARCHAR(15),
    kode_service2 VARCHAR(15),
    kode_service3 VARCHAR(15),
    total_biaya INTEGER,
    uang_masuk INTEGER,
    uang_kembali INTEGER,
    id_petugas integer NOT NULL,
    status_transaksi VARCHAR(12) NOT NULL,
    CONSTRAINT id_petugas
    FOREIGN KEY (id_petugas)
        REFERENCES petugas(id_petugas)
        ON UPDATE CASCADE ON DELETE RESTRICT
);