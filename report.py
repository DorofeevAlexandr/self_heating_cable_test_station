import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
import matplotlib.pyplot as plt
from io import BytesIO


def create_report_word(figure: plt.figure,
                       report_name: str ='report1',
                       company_name: str = 'company_name',
                       date_report: str = 'date_report',
                       name_product: str = 'name_product',
                       numer_batch: str = 'numer_batch'
                       ):
    doc = docx.Document()

    doc.add_heading(company_name, 0).alignment = WD_ALIGN_PARAGRAPH.CENTER
    #doc.add_heading('Отчёт', 1).alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_heading('Испытание саморегулирующегося нагревательного кабеля',
                    1).alignment = WD_ALIGN_PARAGRAPH.CENTER
    par1 = doc.add_paragraph(f'Дата - {date_report}')
    par1.add_run(f'\nНаименование - {name_product}')
    par1.add_run(f'\n№ партии - {numer_batch}')

    image = BytesIO()
    extent = figure.get_window_extent().transformed(figure.dpi_scale_trans.inverted())
    figure.savefig(image, format="jpg", bbox_inches=extent.expanded(0.85, 0.85))

    pic = doc.add_picture(image,
                          width=docx.shared.Cm(18),
                          height=docx.shared.Cm(15)
                          )
    #pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
    #pic.left_indent = docx.shared.Cm(105)
    #docx.enum.text.WD_PARAGRAPH_ALIGNMENT.RIGHT
    doc.save(report_name + '.docx')
