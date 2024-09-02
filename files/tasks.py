from textwrap import dedent
from crewai import Task

class ProductLaunchPlanningTask():
  def product_research_task(self, agent, info_product, info_goals):
    return Task(
      description=dedent(f"""\
        		Lakukan analisis mendalam terhadap produk serupa di 
          		pasaran yang memiliki fitur inti serupa dengan produk {info_product}. 
            	Identifikasi selling point utama masing-masing produk, analisis kekuatan dan kelemahannya, 
             	serta identifikasi celah pasar yang belum terpenuhi untuk dapat {info_goals}

				produk: {info_product}
				tujuan: {info_goals}"""),
      expected_output=dedent(f"""\
        		Laporan komprehensif dalam Bahasa Indonesia yang menyajikan fitur, harga, target audiens, dan ulasan pelanggan. 
          		identifikasi tren terbaru dalam industri terkait yang dapat mempengaruhi strategi peluncuran produk"""), 
      agent=agent
    #   async_execution=True
    )
    
  def industry_analysis_task(self, agent, info_industry, info_goals):
    return Task(
			description=dedent(f"""\
				bertanggung jawab untuk melakukan analisis mendalam terhadap lanskap 
    			industri terkait produk baru yang akan diluncurkan. Melalui riset komprehensif, 
       			tim akan mengidentifikasi tren pasar, pesaing utama, dan peluang bisnis potensial. 
          		Dengan menggunakan alat analisis data dan visualisasi, tim akan menghasilkan laporan 
            	yang menyajikan temuan-temuan utama, serta rekomendasi strategis untuk mendukung peluncuran 
             	produk yang sukses. Analisis ini mencakup pemetaan lanskap industri, analisis produk kompetitor, 
              	analisis sentimen pasar, analisis tren pasar, dan pengembangan insights yang actionable.

				Industri: {info_industry}
				Tujuan: {info_goals}"""),
			expected_output=dedent("""\
				Laporan komprehensif dalam Bahasa Indonesia yang menyajikan pemahaman mendalam tentang lanskap industri, tren pasar, dan pesaing utama."""),
			agent=agent
		)
    
  def marketting_and_sales_strategy_task(self, agent, info_industry, info_goals):
    return Task(
			description=dedent(f"""\
				Merancang strategi pemasaran dan penjualan yang komprehensif untuk peluncuran produk
				berdasarkan analisis mendalam terhadap data pasar, pesaing, dan target audiens. 
    			Identifikasi saluran distribusi yang paling efektif, pesan pemasaran yang relevan, 
       			dan taktik penjualan yang akan digunakan. Buatlah rencana tindakan yang detail, 
          		termasuk timeline, metrik keberhasilan, perencanaan alokasi sumberdaya dan alokasi anggaran.

				Industri: {info_industry}
				Tujuan: {info_goals}"""),
			expected_output=dedent("""\
				laporan komprehensif dalam Bahasa Indonesia yang mencakup analisis SWOT, peta perjalanan pelanggan, matriks prioritas, dan rencana aksi yang jelas. 
    			Laporan ini harus memberikan rekomendasi yang konkret untuk memaksimalkan jangkauan pasar dan mendorong penjualan produk."""),
			agent=agent
		)
    
  def product_positioning_and_messaging_task(self, agent, info_product, info_industry, info_goals):
    return Task(
			description=dedent(f"""\
				Lakukan analisis mendalam terhadap produk, pasar, dan kompetitor untuk menentukan positioning 
    			produk yang unik dan menarik. Identifikasi Unique Selling Proposition (USP) yang membedakan 
       			produk kita dari pesaing. Analisis insight dari konsumen dan kompetitor untuk mengembangkan messaging yang kuat dan relevan. 
          		Buatlah matriks positioning yang membandingkan produk kita dengan pesaing utama. 

				Produk: {info_product}
				Industri: {info_industry}
    			Tujuan: {info_goals}"""),
			expected_output=dedent("""\
				Laporan komprehensif dalam Bahasa Indonesia yang mencakup USP yang jelas, positioning statement, messaging key, 
    			dan rekomendasi untuk visual identity dan tone of voice yang sesuai dengan positioning produk"""),
			agent=agent
		)

  def summary_and_briefing_task(self, agent, info_goals):
    return Task(
			description=dedent(f"""\
				Menggabungkan hasil dari berbagai tugas penelitian yang telah diselesaikan sebelumnya untuk 
                membuat laporan berbahasa indonesia yang komprehensif. Laporan ini akan menyajikan temuan-temuan utama, 
                rekomendasi perencanaan strategis, perencanaan berdasarkan timeline dan sumber daya, positioning statement, 
                messaging key, dan rekomendasi untuk visual identity dan tone of voice yang sesuai dengan positioning produk

                Tujuan: {info_goals}"""),
			expected_output=dedent("""\
				Laporan eksekutif dalam Bahasa Indonesia yang ringkas dan mudah dipahami dengan bahasa indonesia, berisi:
                * Ringkasan temuan utama dari setiap tugas dengan rinci
                * Rekomendasi strategis rinci untuk mencapai tujuan bisnis
                * perencanaan berdasarkan timeline dan sumber daya
                * Pernyataan Posisi
                * Pesan Utama
                * rekomendasi untuk visual identity dan tone of voice yang sesuai dengan positioning produk"""),
			agent=agent
		)

