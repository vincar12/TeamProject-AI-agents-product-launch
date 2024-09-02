# **Intellagent**

![Logo Intellagent](https://github.com/FTDS-assignment-bay/p2-final-project-ftds-018-hck-group-002/blob/main/images/logo-1.png)<br>
<p align="center" width="100%">
    <i>
    Kecerdasan di balik setiap keputusan hebat. </i><br>
</p>

## Pengenalan
"Intellagent" adalah platform berbasis AI yang menyederhanakan dan mengoptimalkan proses peluncuran produk Anda. Platform ini menggunakan tim agen AI khusus untuk menganalisis masukan pengguna dan memberikan strategi berbasis data untuk keberhasilan peluncuran. Dengan wawasan yang dapat ditindaklanjuti dan rekomendasi yang dipersonalisasi, Intellagent memastikan peluncuran produk Anda berjalan lancar dan berdampak.

Proyek ini didukung oleh kerangka kerja **CrewAI**, yang mengotomatisasi pembuatan laporan dan rencana peluncuran produk secara terperinci. CrewAI mengoordinasikan agen AI otonom, memungkinkan kolaborasi dan pelaksanaan tugas-tugas kompleks dengan efisien.

## Kerangka Kerja
Proyek ini didukung oleh tim agen AI yang berperan, dikoordinasikan melalui CrewAI. Setiap agen diberikan latar belakang, tugas, alat, dan hasil yang diharapkan untuk melaksanakan perannya. Proyek ini terdiri dari lima agen yang masing-masing berfokus pada aspek-aspek berbeda dari peluncuran produk. Mereka menggunakan **Exa Search Tool**, yang memungkinkan mereka mengumpulkan informasi daring untuk dianalisis. Bersama-sama, mereka berkolaborasi untuk memberikan laporan menyeluruh tentang strategi terbaik untuk meluncurkan produk berdasarkan masukan yang diberikan.


![Cara Kerja Intellagent](https://github.com/FTDS-assignment-bay/p2-final-project-ftds-018-hck-group-002/blob/main/images/Crew_general.png)<br>
<p align="center" width="100%">
    <i>
    Cara kerja Intellagent secara garis besar. </i><br>
</p>

Intellagent bekerja dengan menerima input dari pengguna, lalu tim AI yang terdiri dari berbagai agen akan memproses input tersebut sesuai peran masing-masing untuk melakukan riset dan analisis yang diperlukan. Setelah setiap agen menyelesaikan riset dan analisisnya, agen terakhir akan merangkum seluruh hasil dan menyusun laporan komprehensif berdasarkan input dari pengguna.


![Cara kerja Intellagent secara spesifik](https://github.com/FTDS-assignment-bay/p2-final-project-ftds-018-hck-group-002/blob/main/images/Crew_specific.png)<br>
<p align="center" width="100%">
    <i>
    Cara kerja Intellagent secara spesifik. </i><br>
</p>

Terdapat 5 agen, masing-masing memiliki tugas yang sesuai dengan peran mereka. Setiap agen diberikan tujuan (*goal*) dan latar belakang (*backstory*) yang spesifik agar dapat mengoptimalkan riset dan analisis yang mereka lakukan. Setiap tugas dilengkapi dengan deskripsi dan output yang diharapkan, sehingga para agen dapat menyelesaikan tugas mereka sesuai dengan ketentuan dan hasil yang diinginkan. Empat agen yang bertanggung jawab atas riset dan analisis memiliki alat seperti *search*, *find similar*, dan *get contents* yang digunakan untuk menelusuri web, mencari halaman yang mirip, dan mengambil isi dari halaman tersebut untuk dianalisis lebih lanjut. Agen terakhir bertugas menyusun laporan komprehensif berdasarkan hasil riset dan analisis dari agen-agen sebelumnya.

## Menjalankan Script
- **Konfigurasi Lingkungan**: Atur variabel lingkungan `env.txt` menjadi `.env` untuk OpenAI, Exa, dan Langchain.
- **Instalasi Dependensi**: Jalankan `pip install -r requirements.txt`.
- **Jalankan Script**: Jalankan `streamlit run files/app.py` dan masukkan ide Anda.

## Detail & Penjelasan
- **Menjalankan Script**: Jalankan `streamlit run files/app.py` dan masukkan informasi yang diminta saat diminta. Script ini akan memanfaatkan kerangka kerja CrewAI untuk membuat laporan peluncuran produk untuk Anda.
- **Komponen Utama**:
  - `./files/app.py`: File script utama.
  - `./files/tasks.py`: File utama berisi prompt tugas.
  - `./files/agents.py`: File utama berisi pembuatan agen.
  - `./files/tools.py`: File utama berisi alat untuk agen.

## Referensi
Arenas-Olvera, A. (n.d.). Crew AI crash course step-by-step. Alejandro AO. https://alejandro-ao.com/crew-ai-crash-course-step-by-step/

## Kontributor
- [**Heru**](https://github.com/herurmdn7)
- [**Vincar**](https://github.com/vincar12)
- [**Devon**](https://github.com/RichieDevon53)
