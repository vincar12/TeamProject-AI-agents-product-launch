from textwrap import dedent
from crewai import Agent
import streamlit as st
from typing import Union, List, Tuple, Dict
from langchain_core.agents import AgentFinish
import json
from tools import ExaSearchToolset

class ProductLaunchPlanningAgents():
  def step_callback(
        self,
        agent_output: Union[str, List[Tuple[Dict, str]], AgentFinish],
        agent_name,
        *args,
    ):
        with st.chat_message("AI"):
            # Try to parse the output if it is a JSON string
            if isinstance(agent_output, str):
                try:
                    agent_output = json.loads(agent_output)
                except json.JSONDecodeError:
                    pass

            if isinstance(agent_output, list) and all(
                isinstance(item, tuple) for item in agent_output
            ):

                for action, description in agent_output:
                    # Print attributes based on assumed structure
                    st.write(f"Nama Agent: {agent_name}")
                    st.write(f"Tool used: {getattr(action, 'tool', 'Unknown')}")
                    st.write(f"Tool input: {getattr(action, 'tool_input', 'Unknown')}")
                    st.write(f"{getattr(action, 'log', 'Unknown')}")
                    with st.popover("Show observation"):
                        st.markdown(f"Observation\n\n{description}")
                    st.toast(f'{agent_name} Menggunakan Alat')

            # Check if the output is a dictionary as in the second case
            elif isinstance(agent_output, AgentFinish):
                st.write(f"Agent Name: {agent_name}")
                output = agent_output.return_values
                st.write(f"I finished my task:\n{output['output']}")
                st.toast(f'{agent_name} Menyelesaikan Tugas') 
                
            # Handle unexpected formats
            else:
                st.write(type(agent_output))
                st.write(agent_output)
                
                
  def product_research_agent(self):
    return Agent(
      role="Product Research Specialist",
      goal='Melakukan Riset mendalam terkait dengan produk yang akan diluncurkan',
      tools=ExaSearchToolset.tools(),
      backstory=dedent("""\
        Sebagai product research specialist, misi anda adalah memberikan analisis mendalam tentang lanskap kompetitif suatu produk. Anda akan mengumpulkan, menganalisis, dan menginterpretasikan data pasar yang relevan untuk mengidentifikasi kekuatan dan kelemahan pesaing, tren pasar, serta peluang bisnis yang belum tergarap. Dengan memanfaatkan berbagai sumber data, termasuk ulasan konsumen, laporan industri, dan data penjualan, Anda akan memberikan rekomendasi strategis untuk membantu tim produk dalam membuat keputusan yang tepat. Anda memiliki akses ke berbagai alat analisis data dan kecerdasan buatan untuk mendukung tugas Anda"""),
      verbose=True,
      step_callback=lambda step: self.step_callback(step, "Product Research Specialist"),
    )
    
  def industry_analysis_agent(self):
    return Agent(
      role='Analis Industri Senior',
      goal='Memahami secara mendalam lanskap industri, tren pasar, dan pesaing utama untuk mendukung pengambilan keputusan strategis.',
      tools=ExaSearchToolset.tools(),
      backstory=dedent("""\
          Sebagai seorang analis industri senior, Anda memiliki pengalaman luas dalam menganalisis berbagai industri. Anda memiliki keahlian dalam mengumpulkan, menganalisis, dan menginterpretasikan data pasar yang kompleks. Dengan menggunakan berbagai alat analisis data dan kecerdasan buatan, Anda mampu mengidentifikasi pola, tren, dan hubungan yang tersembunyi dalam data. Anda juga memiliki pemahaman yang mendalam tentang metodologi penelitian pasar dan mampu merancang serta melaksanakan studi pasar yang komprehensif. Misi Anda adalah memberikan wawasan yang mendalam tentang lanskap industri sehingga perusahaan dapat membuat keputusan bisnis yang strategis."""),
      verbose=True,
      step_callback=lambda step: self.step_callback(step, "Analis Industri Senior"),
    )
    
  def marketting_and_sales_strategy_agent(self):
    return Agent(
      role='Strategis Pemasaran Senior',
      goal='Merancang rencana pemasaran komprehensif yang pemilihan saluran distribusi, pengembangan pesan pemasaran yang persuasif dan mengembangkan strategi pemasaran yang inovatif untuk membedakan produk dari pesaing.',
      tools=ExaSearchToolset.tools(),
      backstory=dedent("""\
          Sebagai seorang strategis pemasaran senior, Anda memiliki pengalaman luas dalam merancang dan melaksanakan kampanye pemasaran yang sukses. Anda memiliki keahlian dalam menganalisis pasar, mengidentifikasi target audiens, dan mengembangkan strategi pemasaran yang inovatif. Dengan menggunakan berbagai alat analisis data dan kecerdasan buatan, Anda mampu mengukur efektivitas kampanye pemasaran dan membuat penyesuaian yang diperlukan. Misi Anda adalah memastikan peluncuran produk baru berjalan sukses dan mencapai target penjualan yang ditetapkan.
          Sebagai analis industri senior dengan pengalaman lebih dari 10 tahun, Anda telah menganalisis ratusan perusahaan rintisan dan perusahaan mapan. Anda memiliki keahlian dalam mengidentifikasi tren konsumen yang muncul dan memprediksi dampaknya terhadap pasar. Dengan menggunakan alat analisis data yang canggih, Anda akan memberikan rekomendasi strategis untuk membantu perusahaan dalam mengembangkan model bisnis yang inovatif."""),
      verbose=True,
      step_callback=lambda step: self.step_callback(step, "Strategis Pemasaran Senior"),
    )
    
  def product_positioning_and_messaging_agent(self):
    return Agent(
      role='Strategi Branding Senior',
      tools=ExaSearchToolset.tools(),
      goal='Membangun identitas merek yang kuat dan unik melalui positioning yang jelas dan pesan yang menarik, untuk mencapai keunggulan kompetitif di pasar.',
      backstory=dedent("""\
          Sebagai seorang Strategi Branding Senior, Anda memiliki pengalaman luas dalam membangun merek-merek sukses di berbagai industri. Anda memiliki pemahaman yang mendalam tentang psikologi konsumen, teori warna, dan prinsip-prinsip desain. Anda mampu menganalisis data pasar, tren konsumen, dan perilaku kompetitor untuk mengembangkan strategi branding yang efektif. Dengan menggunakan berbagai alat analisis dan kreativitas, Anda dapat menciptakan identitas merek yang kuat dan berkelanjutan. Misi Anda adalah memastikan produk ini memiliki positioning yang jelas dan pesan yang menarik sehingga dapat bersaing dengan efektif di pasar."""),
      verbose=True,
      step_callback=lambda step: self.step_callback(step, "Strategi Branding Senior"),
    )
    
  def summary_and_briefing_agent(self): 
    return Agent(
      role='Koordinator Strategi Peluncuran Produk',
      goal='Menyusun laporan komprehensif yang mengintegrasikan temuan dari riset produk, analisis industri, strategi pemasaran, dan positioning merek untuk memberikan rekomendasi strategis bagi peluncuran produk yang sukses.',
      backstory=dedent("""\
          Sebagai seorang Koordinator Strategi Peluncuran Produk, Anda adalah penghubung antara berbagai tim yang terlibat dalam peluncuran produk. Anda memiliki kemampuan yang kuat dalam komunikasi, manajemen proyek, dan analisis data. Anda bertanggung jawab untuk memastikan bahwa semua tugas diselesaikan tepat waktu dan sesuai dengan standar yang telah ditetapkan. Anda juga akan memantau kinerja tim dan membuat penyesuaian yang diperlukan untuk memastikan keberhasilan peluncuran produk."""),
      verbose=True,
      step_callback=lambda step: self.step_callback(step, "Koordinator Strategi Peluncuran Produk"),
    )
