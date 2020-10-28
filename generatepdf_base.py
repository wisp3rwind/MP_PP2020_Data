# Code snippets taken from
# https://stackoverflow.com/questions/48745947/writing-a-csv-file-into-a-pdf-document

import os
import numpy as np
from reportlab.lib import colors
from reportlab.lib.pagesizes import inch, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

# Get de work directory
cwd = os.getcwd()

# PDF document layout
table_style = TableStyle([('ALIGN', (1, 1), (-2, -2), 'CENTER'),
                          ('VALIGN', (0, 0), (0, -1), 'TOP'),
                          ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                          ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                          ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                          ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
                          ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                          ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                          ])

styles = getSampleStyleSheet()
styleNormal = styles['Normal']
styleHeading = styles['Heading1']
styleHeading2 = styles['Heading2']
styleHeading.alignment = 1  # centre text (TA_CENTRE)

# Configure style and word wrap
s = getSampleStyleSheet()
s = s["BodyText"]

# Build the file
elements = []

# Introduction text


def addText(text):
    """
    Adds a text line to the pdf document.

    Args:
    text (string): the text that should be added to the document

    """
    elements.append(Paragraph(text, styleNormal))


def addSpacer(height=0.25):
    """
    Args:
    height (float) (default 0.25): the height of the spacer in inches.

    Adds a Spacer to the pdf document
    """
    elements.append(Spacer(inch, height*inch))


def addTable(header, data):
    """
    Adds a table to the pdf document. Header must have the same size as data.

    Args:
    header (list of strings, dimension=(1, D)): the table header
    data (Array, dimension=(X, D)): the table data
    """
    dataWithHeader = np.concatenate((header, data))
    if len(dataWithHeader.shape) == 1:  # if 1D array
        data_formatted = [[Paragraph(row, s) for row in dataWithHeader]]
    else:
        data_formatted = [[Paragraph(cell, s) for cell in row]
                          for row in dataWithHeader]

    t = Table(data_formatted)
    t.spaceBefore = 10
    t.spaceAfter = 10
    t.setStyle(table_style)
    elements.append(t)


def addPagebreak():
    elements.append(PageBreak())


def createPDF(experiment):
    """
    Creates the pdf file
    Args:
    experiment (string): experiments name
    name (string): students name

    """
    # Name of file
    fileName = experiment + "/" + \
        "Data" + experiment + ".pdf"
    archivo_pdf = SimpleDocTemplate(
        fileName, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=28)
    archivo_pdf.build(elements)
    print('Datasheet created', fileName)
