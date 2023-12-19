import PyPDF2 
import json

reader = PyPDF2.PdfReader('mpdf.pdf')


fanlar = reader.pages[0].extract_text()[reader.pages[0].extract_text().find("Test topshirish fanlari"):reader.pages[0].extract_text().find("Test sinovi topshirish hududi va hududga kelish vaqti")].split('Test topshirish fanlari:')[1].splitlines()



data = {
   'Ism familya' : f'{reader.pages[0].extract_text()[reader.pages[0].extract_text().find('F.I.Sh.'):reader.pages[0].extract_text().find('Pasport')].split(':')[1].splitlines('')[0]} {reader.pages[0].extract_text()[reader.pages[0].extract_text().find('F.I.Sh.'):reader.pages[0].extract_text().find('Pasport')].split(':')[1].splitlines('')[1]}',
    'Universetlar' : {
        '1':reader.pages[0].extract_text()[reader.pages[0].extract_text().find("TANLANGAN TA'LIM YO‘NALISHLARI"):reader.pages[0].extract_text().find("IMTIYOZLAR")].splitlines()[1] +' '+reader.pages[0].extract_text()[reader.pages[0].extract_text().find("TANLANGAN TA'LIM YO‘NALISHLARI"):reader.pages[0].extract_text().find("IMTIYOZLAR")].splitlines()[2],
        '2':reader.pages[0].extract_text()[reader.pages[0].extract_text().find("TANLANGAN TA'LIM YO‘NALISHLARI"):reader.pages[0].extract_text().find("IMTIYOZLAR")].splitlines()[3] +' '+reader.pages[0].extract_text()[reader.pages[0].extract_text().find("TANLANGAN TA'LIM YO‘NALISHLARI"):reader.pages[0].extract_text().find("IMTIYOZLAR")].splitlines()[4],
        '3':reader.pages[0].extract_text()[reader.pages[0].extract_text().find("TANLANGAN TA'LIM YO‘NALISHLARI"):reader.pages[0].extract_text().find("IMTIYOZLAR")].splitlines()[5] +' '+reader.pages[0].extract_text()[reader.pages[0].extract_text().find("TANLANGAN TA'LIM YO‘NALISHLARI"):reader.pages[0].extract_text().find("IMTIYOZLAR")].splitlines()[6],
        '4':reader.pages[0].extract_text()[reader.pages[0].extract_text().find("TANLANGAN TA'LIM YO‘NALISHLARI"):reader.pages[0].extract_text().find("IMTIYOZLAR")].splitlines()[7] +' '+reader.pages[0].extract_text()[reader.pages[0].extract_text().find("TANLANGAN TA'LIM YO‘NALISHLARI"):reader.pages[0].extract_text().find("IMTIYOZLAR")].splitlines()[8],
        '5':reader.pages[0].extract_text()[reader.pages[0].extract_text().find("TANLANGAN TA'LIM YO‘NALISHLARI"):reader.pages[0].extract_text().find("IMTIYOZLAR")].splitlines()[9] +' '+reader.pages[0].extract_text()[reader.pages[0].extract_text().find("TANLANGAN TA'LIM YO‘NALISHLARI"):reader.pages[0].extract_text().find("IMTIYOZLAR")].splitlines()[10],
    },
'Fanlar': fanlar[0]+' , '+fanlar[1],
}
print(data['Fanlar'])


