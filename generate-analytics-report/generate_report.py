from fpdf import FPDF
import pandas as pd
import os
from time_series_analysis import plot_states,plot_countries
from datetime import datetime,timedelta
# Lcoal imports

from dailycounts import TEST_DATE



# Local Imports
from data_loader import Mode,load_relevant_data, get_country_names, get_state_names
from dailycounts import plot_daily_count_states,plot_daily_count_countries
from create_case_maps import plot_global_case_map, plot_usa_case_map



width = 210
height = 297


name = "Neeru Kushal Bhargav  Saini"


def create_title(day,pdf):
    HEADER_IMAGE = 'resources/letterhead_cropped.png'

    pdf.image(HEADER_IMAGE,0,0, width)
    pdf.set_font('Arial', 'B', 24)
    pdf.ln(60)

    pdf.write(5,f"Covid Analytics Report")

    pdf.ln(10)
    pdf.set_font('Arial', '', 16)
    
    pdf.write(4,f"{day}")
    pdf.ln(5)

    


def generate_report(day,filename ='tutorial.pdf'):
    pdf = FPDF(orientation='P',format='A4')
    pdf.add_page()

    """
    First Page
    """

    create_title(day,pdf)


    plot_usa_case_map("usa_cases.png",day = day)
    PATH =os.path.join(os.getcwd(),'usa_cases.png')

    pdf.image(PATH,0,90,width)
    # pdf.add_page()
    pdf.add_page()

    
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0,10,f'Analytics Report for {TEST_DATE}',align='C')
    # pdf.ln(20)

    # pdf.cell(80, 10, f'Hello my name is {name}!')
    states = ['New Hampshire','Massachusetts']
    plot_daily_count_states(states,filename='test.png')
    pdf.image('test.png',5, 30,width/2-5)


    plot_daily_count_states(states,mode=Mode.DEATHS,filename="test2.png")
    PATH =os.path.join(os.getcwd(),'test2.png')

    pdf.image(PATH,width/2 , 30 ,width/2-5)

    # print(get_country_names())

    # Plot States Cases
    pdf.add_page()

    plot_states(states,days =7, filename='test3.png')
    PATH =os.path.join(os.getcwd(),'test3.png')
    pdf.image(PATH,5, 105,width/2-5)

    # Plot States Deaths

    plot_states(states,days =7, mode= Mode.DEATHS,filename='test4.png')
    PATH =os.path.join(os.getcwd(),'test4.png')
    pdf.image(PATH,width/2, 105,width/2-5)



    pdf.output(filename)

if  __name__ == '__main__':
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%m/%d/%y").replace("/0","/").lstrip("0")
    
    day =  TEST_DATE

    generate_report(day)

