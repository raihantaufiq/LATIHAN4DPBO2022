# LATIHAN4DPBO2022

Saya Raihan Taufiqurrahman mengerjakan evaluasi Latihan Praktikum dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

### Penjelasan
Terdapat 6 kelas yaitu vehicle, airplane, ship, person, job, dan driver. Pada gambar ini kelas direpresentasikan dengan lingkaran berwarna hijau, hubungan inheritance berwarna oren, dan hubungan composition berwarna biru.

![gambar_penjelasan](https://github.com/raihantaufiq/LATIHAN4DPBO2022/blob/main/Hubungan%20antar%20kelas.png?raw=true)

- Kelas person memiliki hubungan composition dengan kelas job, pekerjaan merupakan atribut dari orang karena orang memiliki pekerjaan (person has a job)
- Kelas driver merupakan turunan kelas person, atribut dan method dari kelas person diturunkan pada kelas driver karena pengemudi merupakan orang, lalu kelas person memiliki kelas job sebagai atributnya sehingga pengemudi adalah orang yang memiliki pekerjaan (driver is a person and has a job)
- Kelas vehicle memiliki hubungan composition dengan kelas driver, hal ini karena pada kendaraan terdapat orang yang mengemudikannya (vehicle has a driver)
- Kelas airplane merupakan turunan kelas vehicle karena pesawat terbang merupakan salah satu jenis kendaraan (airplane is a vehicle). Kelas vehicle juga memiliki kelas driver sebagai salah satu atributnya (airplane is a vehicle and has a driver)
- Kelas ship merupakan turunan kelas vehicle karena kapal merupakan salah satu jenis kendaraan (ship is a vehicle).Kelas vehicle juga memiliki kelas driver sebagai salah satu atributnya (ship is a vehicle and has a driver)
- Pada kelas vehicle terdapat method Move(), pada kelas anaknya yaitu airplane dan ship dibuat lagi fungsi Move() dengan isi yang berbeda, hal ini karena pesawat dan kapal memiliki cara bergerak yang berbeda. Jadi jika Move() dipanggil dari kelas vehicle maka akan menampilkan: vehicle is moving, jika dipanggil dari kelas airplane akan menampilkan: airplane is flying, pada kelas ship: ship is sailing
- Pada kelas person terdapat method sleeping(), pada kelas anaknya yaitu kelas driver tidak dibuat method tersebut lagi sehingga jika method sleep() dipanggil dari kelas person maupun driver akan tetap menampilkan: "nama orang" is sleeping.


### Screenshot
![1](https://github.com/raihantaufiq/LATIHAN4DPBO2022/blob/main/Screenshot%20(1).png?raw=true)
![2](https://github.com/raihantaufiq/LATIHAN4DPBO2022/blob/main/Screenshot%20(2).png?raw=true)
![3](https://github.com/raihantaufiq/LATIHAN4DPBO2022/blob/main/Screenshot%20(3).png?raw=true)
![4](https://github.com/raihantaufiq/LATIHAN4DPBO2022/blob/main/Screenshot%20(4).png?raw=true)
![5](https://github.com/raihantaufiq/LATIHAN4DPBO2022/blob/main/Screenshot%20(5).png?raw=true)
![6](https://github.com/raihantaufiq/LATIHAN4DPBO2022/blob/main/Screenshot%20(6).png?raw=true)
![7](https://github.com/raihantaufiq/LATIHAN4DPBO2022/blob/main/Screenshot%20(7).png?raw=true)
![8](https://github.com/raihantaufiq/LATIHAN4DPBO2022/blob/main/Screenshot%20(8).png?raw=true)
