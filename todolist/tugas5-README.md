1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

	Inline CSS adalah CSS yang diaplikasikan pada masing-masing elemen HTML. Ini berguna untuk kasus-kasus spesifik (dimana hanya satu-dua elemen yang memiliki style berbeda), namun sangat sulit untuk diaplikasikan secara manual.
	
	Internal CSS adalah CSS yang di-definisikan secara internal dalam file HTML namun terpisah dari elemen HTML lainnya. Intinya dia dibuat dalam section tersendiri secara internal.
	
	External CSS adalah CSS yang didefinisikan dari luar file HTML. File HTML bisa di-link ke file .css yang mengendalikan elemen stylingnya. 

	Pembuatannya mirip dengan internal CSS karena semua class-class nya didefinisikan terpisah dari HTML, namun bedanya satu file external CSS bisa digunakan ulang untuk banyak file HTML sedangkan internal CSS harus di-definisikan untuk setiap file HTML.

2. Jelaskan tag HTML5 yang kamu ketahui.

	`<head></hear>` dan `<body></body> `mendefinisikan struktur HTML. Di dalam head terdapat tag yang mengandung informasi terkait halaman tersebut seperti `<title></title>` untuk judul halaman.

	Konten atau elemen bisa ditutup dalam `<div></div>` yaitu divider atau semacam container untuk elemen-elemen lainnya, seperti:

	* `<p></p>` untuk paragraph,
	* `<img src=''/>` untuk gambar,
	* `<h1></h1>` untuk heading,
	* `<br>` untuk line break,
	* `<table></table>` untuk tabel
		* `<tr></tr>` untuk table row
		* `<th></th>` untuk table header
		* `<td></td>` untuk table content
	* `<a></a>` untuk elemen mengandung hyperlink.
	* `<form></form>` untuk elemen form

3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
	* ID selector (bersifat individual dan unik ) e.g. 001 (dari primary key)
	* Element selector (bersifat universal untuk elemen tertentu) e.g. table, h1
	* Class selector (bersifat universal untuk semua elemen yang ditandai dengan nama class tersebut) e.g. wishlist-table, table-stripped, d-block

	
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

	Pertama saya men-delete CSS yang sudah ada supaya bisa mengaplikasikan Bootstrap secara clean dan sesuai ekspektasi. Kemudian saya mendesain navbar untuk user dan logout button, dilanjutkan dengan menentukan bootstrap class yang diperlukan untuk tampilan login / register. Setelah sudah rapi semua, saya buat cards di dalam for-loop untuk setiap todo, yang disimpan dalam bootstrap grid container dengan 2 kolom.
	
	Untuk membuat websitenya responsive, saya menambahkan tag `<meta name="viewport" content="width=device-width, initial-scale=1.0">` dan membuka menu F12 untuk menguji responsiveness dari websitenya dengan mengubah resolusi browser (caranya dengan menekan 'Toggle device emulation') dan mencoba-coba banyak display mode untuk memastikan tampilan berubah dan masih enak dilihat.