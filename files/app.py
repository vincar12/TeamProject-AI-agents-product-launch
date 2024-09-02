import streamlit as st
from dotenv import load_dotenv
from crewai import Crew
from tasks import ProductLaunchPlanningTask
from agents import ProductLaunchPlanningAgents

class ProductPlan:
    def __init__(self) -> None:
        self.session_state = st.session_state
        load_dotenv()
        self.initialize_session_state()
        
    def initialize_session_state(self):
    
        if "industry" not in st.session_state:
            st.session_state.industry = ""

        if "product" not in st.session_state:
            st.session_state.product = ""
            
        if "tujuan" not in st.session_state:
            st.session_state.tujuan = ""

        if "report" not in st.session_state:
            st.session_state.report = ""

        if "generating" not in st.session_state:
            st.session_state.generating = False
            
    def generate_report(self, product, industry, tujuan):
        
        tasks = ProductLaunchPlanningTask()
        agents = ProductLaunchPlanningAgents()
        
        # create agents
        product_research_agent = agents.product_research_agent()
        industry_analysis_agent = agents.industry_analysis_agent()
        marketting_and_sales_strategy_agent = agents.marketting_and_sales_strategy_agent()
        product_positioning_and_messaging_agent = agents.product_positioning_and_messaging_agent()
        summary_and_briefing_agent = agents.summary_and_briefing_agent()
        
        product_research_task = tasks.product_research_task(product_research_agent, product, tujuan)
        industry_analysis_task = tasks.industry_analysis_task(industry_analysis_agent, industry, tujuan)
        marketting_and_sales_strategy_task = tasks.marketting_and_sales_strategy_task(marketting_and_sales_strategy_agent, industry, tujuan)
        product_positioning_and_messaging_task = tasks.product_positioning_and_messaging_task(product_positioning_and_messaging_agent, product, industry, tujuan)
        summary_and_briefing_task = tasks.summary_and_briefing_task(summary_and_briefing_agent, tujuan)
        
        # industry_analysis_task.context = [product_research_task]
        marketting_and_sales_strategy_task.context = [product_research_task, industry_analysis_task]
        product_positioning_and_messaging_task.context = [product_research_task, industry_analysis_task, marketting_and_sales_strategy_task]
        summary_and_briefing_task.context = [product_research_task, industry_analysis_task, marketting_and_sales_strategy_task, product_positioning_and_messaging_task]
        
        crew = Crew(
            agents=[
                product_research_agent,
                industry_analysis_agent,
                marketting_and_sales_strategy_agent,
                product_positioning_and_messaging_agent,
                summary_and_briefing_agent
            ],
            tasks=[
                product_research_task,
                industry_analysis_task,
                marketting_and_sales_strategy_task,
                product_positioning_and_messaging_task,
                summary_and_briefing_task
            ]
        )
        return crew.kickoff()

    def report_generation(self):

        if st.session_state.generating:
            with st.status('Crew Sedang Berdiskusi.', expanded=False) as status:
                st.session_state.report = self.generate_report(
                    st.session_state.product, st.session_state.industry, st.session_state.tujuan
                )
                status.update(label='Diskusi Selesai', state='complete', expanded=False)

        if st.session_state.report and st.session_state.report != "":
            st.sidebar.success("Planning Selesai Dimuat")
            st.session_state.generating = False

    def sidebar(self):
        with st.sidebar:
            col1, col, col3 = st.columns([1,4.5,1])
            col.image("logo.png", width=175)
            st.caption('The intelligence behind every great decision')

            st.write(
                """
                Mohon melakukan inputasi terhadap beberapa informasi yang dibutuhkan oleh Crew kami. \n
                """
            )

            industry = st.text_area(
                "**Nama Perusahaan dan Sektor Industri.**", 
                key="industry", 
                placeholder="Perusahaan Telkomsel yang bergerak di bidang telekomunikasi pada kawasan Indonesia"
            )

            product = st.text_area(
                "**Informasi Produk.**",
                key="product",
                placeholder="Peluncuran produk jaringan Wifi satelit tanpa perlu penarikan Kabel. ",
            )
            
            tujuan = st.text_area(
                "Tujuan dari Peluncuran Produk.",
                key="tujuan",
                placeholder="Meningkatkan keuntungan perusahaan dan jumlah pelanggan.",
            )

            if industry and product and tujuan:
                if st.button("Generate Meeting"):
                    st.toast('Meeting Dimulai', icon='📢')
                    st.session_state.generating = True
            
            
    def render(self):
        st.set_page_config(page_title="Intellagent - Planning Crew", page_icon="🤖")

        self.sidebar()
        
        st.title('Product Launch Planning Crew')
        st.image('https://cdn-uploads.huggingface.co/production/uploads/noauth/niqLS16if9xuvs2rpXV-q.webp', caption='hanya ilustrasi ')
        st.markdown('''
                    Tim AI agents akan membantu kamu dalam membuat insight penting seperti Keys Finding, Strategic Recommendation, Timeline and Resource Planning, Positioning Statement, Key Message, Visual Identity dan lain-lain.  \n\n
                    ''')
        self.report_generation()

        if self.session_state.report and self.session_state.report != "":
            st.header("Laporan Hasil Diskusi Crew")  # Clearer heading
            st.markdown(self.session_state.report)
            st.toast('Meeting Selesai', icon='🎉')

if __name__ == "__main__":
    ProductPlan().render()
