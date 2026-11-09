import sys,pathlib,json,re,html,statistics
sys.path.insert(0,str(pathlib.Path(__file__).parent/'pydeps'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak,Image,Preformatted,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY,TA_CENTER,TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
ROOT=pathlib.Path(__file__).resolve().parents[2];LAB=ROOT/'lab'
data=json.loads((LAB/'results/analysis.json').read_text());s=data['summary']
def stat(code,key,dec=2):
    a=s[code][key]
    return f"{a['median']:.{dec}f} ({a['min']:.{dec}f}–{a['max']:.{dec}f})" if a else 'NA'
def med(code,key='recovered'):return s[code][key]['median']
def mdtable(header,rows):return '| '+' | '.join(header)+' |\n|'+'|'.join(['---']*len(header))+'|\n'+'\n'.join('| '+' | '.join(map(str,row))+' |' for row in rows)
cpu=json.loads((LAB/'environment/cpu.json').read_text(encoding='utf-8-sig'))
mem=json.loads((LAB/'environment/memory.json').read_text(encoding='utf-8-sig'))
host=json.loads((LAB/'environment/host.json').read_text())
tokens={
'ENV_TABLE':mdtable(['Thuộc tính','Giá trị'],[['CPU',cpu['Name']],['Nhân vật lý / luồng logic',f"{cpu['NumberOfCores']} / {cpu['NumberOfLogicalProcessors']}"],['RAM máy',f"{mem['TotalPhysicalMemory']/2**30:.1f} GiB"],['Hệ điều hành',host['platform']],['John','1.9.0-jumbo-1, Cygwin x64, AVX2, OpenMP 4 luồng'],['Hashcat','8.0.0; thiết bị theo environment/hashcat-devices.txt'],['Môi trường đo','Windows native, chưa dựng Linux VM']]),
'HC_ENV_NOTE':'Log thiết bị liệt kê Intel HD Graphics 630 và NVIDIA GTX 1050 ở OpenCL, nhưng không có CPU OpenCL backend. CUDA không khởi tạo được với runtime hiện có. Thử CPU được giữ lại như bằng chứng lỗi môi trường; thử GPU được ghi riêng nếu thành công.',
'A_TABLE':mdtable(['Phép thử','G1','G2','G3','Tổng /100','Wall giây¹'],[[c,*[int(s[c]['groups'][g]) for g in ['G1','G2','G3']],stat(c,'recovered',0),stat(c,'wall_time_s')] for c in ['A1','A2','A3','A4']])+ '\n\n¹ Median (min–max), ba lượt. G4 và G5 đều bằng 0 trong các lượt A1–A4.',
'A_INTERPRETATION':f"A4 khôi phục median {med('A4'):.0f}/100 trong giới hạn thời gian, còn A3 hoàn tất mask với wall time median {med('A3','wall_time_s'):.2f} giây. Vì hai cơ chế có thứ tự thử và overhead khác nhau, tỷ lệ không gian 322 lần không được coi là hệ số tăng tốc đo được. G4/G5 chưa được tìm trong các lượt này.",
'A5_RESULT':f"Kết quả khôi phục là {med('A5'):.0f}/100, wall time {med('A5','wall_time_s'):.2f} giây.",
'A6_RESULT':f"John khôi phục {med('A6'):.0f}/8 mật khẩu giả lập, wall time {med('A6','wall_time_s'):.2f} giây.",
'B_TABLE':mdtable(['Cấu hình','Khôi phục /100¹','Wall giây¹','Kết thúc'],[[label,stat(c,'recovered',0),stat(c,'wall_time_s'),', '.join(s[c]['stop_reasons'])] for c,label in [('B1','Raw SHA-256'),('B2','bcrypt cost 10'),('B3','bcrypt cost 12')]])+'\n\n¹ Median (min–max), ba lượt; thời gian thực có thể vượt 60 giây do hoàn tất batch.',
'B_INTERPRETATION':f"Raw SHA-256 khôi phục median {med('B1'):.0f}/100, bcrypt cost 10 khôi phục {stat('B2','recovered',0)}/100 và cost 12 khôi phục {stat('B3','recovered',0)}/100. Với 100 salt riêng, công cụ phải thực hiện nhiều phép xác minh cho cùng một ứng viên. Trong ngân sách ngắn, đáp án có trong wordlist vẫn có thể chưa được xử lý tới; vì vậy mức khôi phục thấp không mâu thuẫn với thiết kế G1/G2.",
'D_TABLE':mdtable(['Đối chứng','p/s¹','Wall giây¹','Kết thúc'],[[label,stat(c,'p_s'),stat(c,'wall_time_s'),', '.join(s[c]['stop_reasons'])] for c,label in [('D1','Raw SHA-256'),('D2','bcrypt 10'),('D3','bcrypt 12')]])+'\n\n¹ Median (min–max) tốc độ p/s cuối do John báo và wall time. Mỗi lượt chỉ có một hash.',
'D_INTERPRETATION':f"Tốc độ bcrypt cost 10 có median {med('D2','p_s'):.2f} p/s; cost 12 là {med('D3','p_s'):.2f} p/s. Tỷ số tương ứng {med('D2','p_s')/med('D3','p_s'):.2f} lần, gần mức tăng công việc 4 lần của tham số vòng lặp. Kết luận chỉ áp dụng cấu hình đã đo; tốc độ còn chịu ảnh hưởng tải nền và batch.",
'CONCLUSION_METRICS':f"Trong kịch bản 2, bcrypt cost 10 và 12 khôi phục median lần lượt {med('B2'):.0f} và {med('B3'):.0f}/100 trong ngân sách 60 giây. Đối chứng một hash ghi nhận median {med('D2','p_s'):.2f} và {med('D3','p_s'):.2f} p/s, chênh lệch {med('D2','p_s')/med('D3','p_s'):.2f} lần. Những số đo này cho thấy tăng cost làm giảm khả năng thử trong cùng thời gian ở môi trường nghiên cứu."
}
gpu=s.get('C_G',{})
if gpu.get('successful_runs')==3:
    tokens['HC_RESULT']=f"Thử CPU không thực hiện được do thiếu backend. Thử GPU Intel HD Graphics 630 với Hashcat khôi phục median {gpu['recovered']['median']:.0f}/100 từ cùng 4.000 ứng viên; wall time median {gpu['wall_time_s']['median']:.2f} giây ({gpu['wall_time_s']['min']:.2f}–{gpu['wall_time_s']['max']:.2f}), ba lượt. John CPU trên cùng tập ứng viên khôi phục {med('B1'):.0f}/100, wall time {stat('B1','wall_time_s')} giây. Đây là hai cấu hình triển khai khác nhau; không suy hệ số tăng tốc phần mềm từ wall time này."
    tokens['HC_CONCLUSION']='Kết quả xác nhận hai cấu hình tìm cùng các mật khẩu có trong tập ứng viên. Chưa có phép đo hiệu năng cùng backend giữa hai công cụ.'
else:
    tokens['HC_RESULT']='Các lần kiểm tra Hashcat và lỗi backend được lưu trong environment và results. Chưa có đủ ba lượt chạy thành công trên backend phù hợp để tổng hợp hiệu năng. Vì vậy phần so sánh hoàn thành ở mức chức năng và khả năng triển khai; không điền số đo thay cho quan sát chưa có.'
    tokens['HC_CONCLUSION']='Chưa đủ điều kiện xếp hạng hiệu năng giữa hai công cụ tại môi trường này.'
text=(ROOT/'report/Bao-cao.template.md').read_text(encoding='utf8')
for key,value in tokens.items():text=text.replace('{{'+key+'}}',value)
assert '{{' not in text
(ROOT/'report/Bao-cao.md').write_text(text,encoding='utf8')
plt.rcParams.update({'font.family':'Arial','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':150})
figdir=LAB/'figures';figdir.mkdir(exist_ok=True)
fig,ax=plt.subplots(figsize=(8,3.0));codes=['A1','A2','A3','A4'];bottom=[0]*4
for g,col in zip(['G1','G2','G3'],['#164a63','#16857b','#d49a2a']):
    vals=[s[c]['groups'][g] for c in codes];ax.bar(codes,vals,bottom=bottom,label=g,color=col,width=.56);bottom=[a+b for a,b in zip(bottom,vals)]
ax.set_ylabel('Số mật khẩu /100');ax.set_ylim(0,50);ax.set_xlabel('Median của ba lượt');ax.legend(frameon=False,ncol=3);fig.tight_layout();fig.savefig(figdir/'strategies.png');plt.close(fig)
fig,ax=plt.subplots(figsize=(8,2.7));codes=['B1','B2','B3'];v=[med(c) for c in codes];ax.bar(['SHA-256','bcrypt 10','bcrypt 12'],v,color=['#164a63','#16857b','#d49a2a'],width=.5);ax.set_ylabel('Khôi phục /100');ax.set_ylim(0,50)
for i,n in enumerate(v):ax.text(i,n+1,f'{n:g}',ha='center')
fig.tight_layout();fig.savefig(figdir/'hash-recovery.png');plt.close(fig)
fig,ax=plt.subplots(figsize=(8,2.7));v=[med(c,'p_s') for c in ['D2','D3']];ax.bar(['bcrypt cost 10','bcrypt cost 12'],v,color=['#16857b','#d49a2a'],width=.45);ax.set_ylabel('Ứng viên mỗi giây (p/s)')
for i,n in enumerate(v):ax.text(i,n+2,f'{n:.2f}',ha='center')
ax.set_ylim(0,max(v)*1.25);fig.tight_layout();fig.savefig(figdir/'bcrypt-speed.png');plt.close(fig)
pdfmetrics.registerFont(TTFont('TimesVN','C:/Windows/Fonts/times.ttf'))
pdfmetrics.registerFont(TTFont('TimesVN-Bold','C:/Windows/Fonts/timesbd.ttf'))
pdfmetrics.registerFont(TTFont('TimesVN-Italic','C:/Windows/Fonts/timesi.ttf'))
pdfmetrics.registerFontFamily('TimesVN',normal='TimesVN',bold='TimesVN-Bold',italic='TimesVN-Italic')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle('BodyVN',fontName='TimesVN',fontSize=12,leading=17,spaceAfter=8,alignment=TA_JUSTIFY))
styles.add(ParagraphStyle('RefVN',fontName='TimesVN',fontSize=12,leading=17,spaceAfter=8,alignment=TA_LEFT))
styles.add(ParagraphStyle('TitleVN',fontName='TimesVN-Bold',fontSize=20,leading=26,spaceAfter=18,textColor=colors.black))
styles.add(ParagraphStyle('H2VN',fontName='TimesVN-Bold',fontSize=13,leading=18,spaceBefore=8,spaceAfter=8,keepWithNext=True))
styles.add(ParagraphStyle('CellVN',fontName='TimesVN',fontSize=10.5,leading=14,spaceAfter=0))
styles.add(ParagraphStyle('CaptionVN',fontName='TimesVN-Italic',fontSize=10.5,leading=14,spaceAfter=9,alignment=TA_CENTER))
def inline(t):
    t=html.escape(t);t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t);t=re.sub(r'`(.+?)`',r'\1',t);return t
story=[];lines=text.splitlines();i=0
while i<len(lines):
    l=lines[i].strip()
    if not l:i+=1;continue
    if l=='<!-- page -->':story.append(PageBreak());i+=1;continue
    if l.startswith('# '):story.append(Paragraph(inline(l[2:]),styles['TitleVN']));i+=1;continue
    if l.startswith('## '):story.append(Paragraph(inline(l[3:]),styles['H2VN']));i+=1;continue
    if l.startswith('|'):
        rows=[]
        while i<len(lines) and lines[i].strip().startswith('|'):
            a=[c.strip() for c in lines[i].strip().strip('|').split('|')]
            if not all(re.fullmatch(r'[:\- ]+',x) for x in a):rows.append(a)
            i+=1
        n=len(rows[0]);width=pdfmetrics.stringWidth('a','TimesVN',12)
        widths={2:[155,332],3:[95,220,172],4:[125,115,120,127],6:[82,40,40,40,105,180]}.get(n,[487/n]*n)
        if rows[0][0]=='Nhóm':widths=[55,90,342]
        if rows[0][0]=='Phần':widths=[125,307,55]
        table=Table([[Paragraph(inline(c),styles['CellVN']) for c in row] for row in rows],colWidths=widths,repeatRows=1,hAlign='LEFT')
        table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8eef2')),('GRID',(0,0),(-1,-1),.5,colors.HexColor('#d9d9d9')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f7f8fa')])]))
        story.extend([table,Spacer(1,10)]);continue
    if l.startswith('!['):
        m=re.match(r'!\[(.+?)\]\((.+?)\)',l);p=(ROOT/'report'/m[2]).resolve()
        from PIL import Image as PILImage
        iw,ih=PILImage.open(p).size
        im=Image(str(p),width=487,height=487*ih/iw)
        story.extend([im,Paragraph(inline(m[1]),styles['CaptionVN'])]);i+=1;continue
    if l.startswith('```'):
        code=[];i+=1
        while i<len(lines) and not lines[i].startswith('```'):code.append(lines[i]);i+=1
        for a in code:story.append(Paragraph(inline(a),ParagraphStyle('CodeVN',parent=styles['CellVN'],spaceAfter=3)))
        story.append(Spacer(1,7));i+=1;continue
    p=[l];i+=1
    while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','```','![','<!--')):p.append(lines[i].strip());i+=1
    body=' '.join(p)
    story.append(Paragraph(inline(body),styles['RefVN'] if re.match(r'^\[\d+\]',body) else styles['BodyVN']))
def page(c,doc):
    c.setFont('TimesVN',9);c.setFillColor(colors.HexColor('#555555'));c.drawString(54,27,'An toàn thông tin nâng cao • John the Ripper');c.drawRightString(A4[0]-54,27,str(doc.page))
doc=SimpleDocTemplate(str(ROOT/'report/Bao-cao-John-the-Ripper.pdf'),pagesize=A4,leftMargin=54,rightMargin=54,topMargin=48,bottomMargin=48,title='Nghiên cứu John the Ripper',author='Nhóm 3 thành viên - bản thảo hỗ trợ bằng Codex')
doc.build(story,onFirstPage=page,onLaterPages=page)
# Complete values for editable native charts in the deck.
(pathlib.Path(__file__).parent/'deck-data.json').write_text(json.dumps({'summary':s,'tokens':tokens},ensure_ascii=False,indent=2),encoding='utf8')
print('Report and figures built')
