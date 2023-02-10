use llista_compra_m06; 

drop table if exists sessions_usuaris;
drop table if exists categories;
drop table if exists usuaris;

create table if not exists usuaris(
    id bigint unsigned AUTO_INCREMENT PRIMARY KEY,
    usuari VARCHAR(20) NOT NULL UNIQUE,
    password_hash VARCHAR(256) NOT NULL
);

create table if not exists categories(
    id bigint unsigned AUTO_INCREMENT PRIMARY KEY,
    categoria varchar(20) not null UNIQUE,
    usuari bigint unsigned,
    FOREIGN KEY (usuari) REFERENCES usuaris(id) ON DELETE CASCADE
);

create table if not exists sessions_usuaris(
    uuid char(36) not null PRIMARY KEY,
    usuari bigint unsigned NOT  NULL,
    creat TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP(6),
    FOREIGN KEY (usuari) REFERENCES usuaris(id) ON DELETE CASCADE
);

INSERT into categories (categoria) VALUES ("Frescos");
INSERT into categories (categoria) VALUES ("Begudes");
INSERT into categories (categoria) VALUES ("Làctis");
INSERT into categories (categoria) VALUES ("Neteja");
INSERT into categories (categoria) VALUES ("Fruita i verdures");
