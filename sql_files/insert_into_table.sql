LOAD DATA LOCAL INFILE '/usr/local/airflow/store_files_airflow/store.csv' INTO TABLE Store FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;