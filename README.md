# pytube
adalah aplikasi untuk mengunduh video YouTube langsung ke dalam komputer anda. Hal tersebut membuat anda memiliki video favorit anda di dalam komputer anda.

#### View
![](https://yanwarsolahudinn.files.wordpress.com/2015/08/pytub1.jpg)
![](https://yanwarsolahudinn.files.wordpress.com/2015/08/pytub2.jpg)

#### Versi Python
Python 3.4

#### Paket Dependensi
* pyautogui
* pafy
* pyscreeze
* pymsgbox
* pytweening

#### Instalasi Semua Paket Dependensi
```
$ pip install -r requirements.txt
```

#### Cara Menggunakan
```
$ python pytube.py
```

#### Membuat Binary File
instalasi `pyinstaller`:
```

$ pip install pyinstaller
```
build executable:
```
$ pyinstaller --onefile --windowed pytube.py
```
selesai

#### Set System Environment Windows
buat direktori di `C:\pytube`, simpan file executable atau script `pytube.py` di dalamnya. pilih `menu start` lalu ketik `System environment variables`, pilih `Edit the system environment variables`, setelah itu klik tombol `Environment Vaiables...`. edit `System variables` dan pada bagian `path` tambahkan :
```
C:\pytube
```
klik `ok -> ok -> ok` , selesai.
