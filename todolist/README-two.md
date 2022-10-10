1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Synchronous programming adalah paradigma programming untuk sebuah aplikasi atau sistem yang tidak bisa diotak-atik di tengah jalan. Hal ini dikarenakan metode pemanggilan function atau request yang hanya bisa dilakukan satu-satu (synchronous). Contohnya, web yang synchronous ketika pagenya dibuka oleh user maka dia harus refresh untuk melihat perubahan yang baru. 

Asynchronous programming adalah paradigma untuk sebuah sistem yang bisa update atau berubah tanpa harus dijalankan ulang. Hal ini dikarenakan sistem bisa multitasking dan menjalankan banyak hal sekaligus (sambil jalan sambil update). Contohnya, web yang asynchronous bisa mengubah tampilan sambil dibuka oleh user.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-driven programming adalah paradigma dimana program bergantung pada 'event' yang terjadi pada sistem atau aplikasi. Event yang dimaksud dapat berupa perubahan waktu, button click, button hover, key press, dll. Contohnya, pada tugas 6 kita membuat modal (yang sudah ada di html) yang hanya akan muncul jika tombol New Task dipencet.


3. Jelaskan penerapan asynchronous programming pada AJAX.

AJAX (Asynchronous JavaScript And XML) memiliki kemampuan untuk mengubah isi html / tampilan page tanpa harus mengubah file/data yang tentunya membutuhkan refresh. AJAX juga mampu membuat HTTP POST dan GET request sendirinya. 

Maka dari itu, dengan ajax kita bisa mensubmit atau mengambil data dan langsung menampilkannya di web.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Saya memulai dengan yang paling simple, yaitu membuat path yang mengarah ke view yang mengembalikan json dari tasks sebuah user. Kemudian saya membuat path baru (/todolist/ajax) untuk mencoba membuat ajax GET request. Saya membuat file .js yang dirujuk oleh file todolist_ajax.html kemudian mulai membuat function js yang bisa mengembalikan data dari json, tepatnya dalam bentuk bootstrap Card (dengan string concatenation supaya yang di-return sudah bentuk html yang siap).

Kemudian, dengan proses trial-and-error yang panjang dan belibet, saya juga berhasil membuat POST request setelah mensubmit data di form modal. Function yang saya buat juga sekaligus menyimpan data ke databse (sesuai view Django) dan menambahkan Card dari data task yang baru. Function ini dihubungkan ke view Django 'add', dan cara JQuery bisa menambahkan Card langsung adalah dengan menerima data Task object yang direturn oleh Django. 

Intinya:

Submit(HTML) onclick tombol untuk memanggil JQuery Function -> JQuery makes POST request -> Django creates new Task object (and saves it) then returns it to JQuery -> JQuery creates Card from Task object -> HTML displays Card

Tentunya setelah itu saya juga menambahkan fungsionalitas lain secara async, seperti 'Done/Finish Task, dan Delete Task (inti alurnya sama).

