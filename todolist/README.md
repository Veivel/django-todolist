[apaituplatform.herokuapp.com]()

1. { % csrf_token % } meng-insert sebuah CSRF (Cross-Site Request Forgery) token ke dalam template html sebelum ditampilkan.

	Token ini berguna untuk keamanan user and site, karena hanya form yang memang berasal dari site nya sendiri memiliki token ini. Sehingga jika tidak ada potongan kode ini maka kedua hal tersebut (user dan site) akan rawan dari serangan pihak eksternal. Maka untuk keamanan, Django memblokir akses website tanpa adanya CSRF token tersebut (Karena dia menganggap form yang kita buka belum terverifikasi).
	
2. Sebetulnya saya menggunakan itu: bisa. Caranya kita bukan membuat form sebagai object Intinya kita membuat input fields secara manual dalam HTML (daripada membiarkan Django yang mengurus tampilan HTML table dari form kita) kemudian membuat sebuah trigger yang mensubmit POST request dari semua input yang telah kita masukkan.

3. Ketika pengguna memencet tombol Submit (baik pada Register, Login, ataupun Add Task), browser men-submit POST request dengan input kita kepada server. POST reqeuest berbeda dengan GET request karena bisa melakukan perubahan pada database / server. Django view kita akan memproses data tersebut, contohnya dengan membuat instansi objek yang baru dengan data dari input, kemudian menyimpannya ke database.

	Terakhir kita me-redirect pengguna ke view tadi yang sudah ter-update dengan data yang baru.
	
4. Saya memulai dengan mengimplementasikan fitur login-logout-register sesuai ajaran Lab 3. Setelah trial-dan-error saya membuat mengatur model Task di models.py dan view todolist di views.py & urls.py. Kemudian saya membuat template todolist.html dan tombol Add Task yang membuka view add-task sebagai form. Setelah formnya diisi saya memanggil function untuk add_task lagi namun dgn request POST (supaya data nya bisa tersimpan ke server). Data tersebut tinggal ditampilkan di template (seperti wishlist dan katalog) dan kita tinggal perlu me-redirect pengguna kembali ke todolist dengan me-return response atau redirect.

	Setelah itu saya mengimplementasi filtering untuk masing-masing user dan fitur delete/done. Fitur delete mengaplikasikan pemanggilan view per task id, khususnya view yang functionnya menghapus data task dari database (yang sesuai task id nya).