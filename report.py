import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
import matplotlib.pyplot as plt
from io import BytesIO


from config import COMPANY_NAME


def create_report_word(figure: plt.figure,
                       data: dict,
                       report_filename: str ='report',
                       company_name: str = COMPANY_NAME,
                       ):
    doc = docx.Document()

    doc.add_heading(company_name, 0).alignment = WD_ALIGN_PARAGRAPH.CENTER
    #doc.add_heading('Отчёт', 1).alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_heading('Испытание саморегулирующегося нагревательного кабеля',
                    1).alignment = WD_ALIGN_PARAGRAPH.CENTER
    par1 = doc.add_paragraph(f'Дата - {data.get("s_TimePuskTest", "_")}')
    par1.add_run(f'\nФамилия испытателя - {data.get("s_FamilyTester", "_")}')
    par1.add_run(f'\nНаименование - {data.get("s_KableBrandTest", "_")}')
    par1.add_run(f'\n№ партии - {data.get("s_BatchNumberTest", "_")}')

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
    doc.save(report_filename)
