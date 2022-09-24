[apaituplatform.herokuapp.com]()

1. { % csrf_token % } meng-insert sebuah CSRF (Cross-Site Request Forgery) token ke dalam template html sebelum ditampilkan.

	Token ini berguna untuk keamanan user and site, karena hanya form yang memang berasal dari site nya sendiri memiliki token ini. Sehingga jika tidak ada potongan kode ini maka kedua hal tersebut (user dan site) akan rawan dari serangan pihak eksternal. Maka untuk keamanan, Django memblokir akses website tanpa adanya CSRF token tersebut (Karena dia menganggap form yang kita buka belum terverifikasi).
	
	2. 