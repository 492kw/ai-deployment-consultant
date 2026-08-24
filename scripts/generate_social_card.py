from PIL import Image, ImageDraw, ImageFont
W,H=1200,630
im=Image.new('RGB',(W,H),'#F6F1E8'); d=ImageDraw.Draw(im)
display=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf',68)
body=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',27)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',18)
d.rectangle((0,0,W,16),fill='#A95F32'); d.text((80,100),'AI DEPLOYMENT CONSULTANT',font=mono,fill='#A95F32')
d.multiline_text((80,155),'Make AI useful\nin the way your business\nalready works.',font=display,fill='#18221F',spacing=4)
d.text((84,458),'Scoped AI workflow deployment for SMBs',font=body,fill='#4B5651')
for x,y,label,col in [(800,180,'OBSERVE','#E7EEE5'),(950,270,'SCOPE','#F8EADC'),(800,370,'BUILD/TEST','#E7EEE5'),(1010,410,'ROLL OUT','#F8EADC')]:
 d.rounded_rectangle((x,y,x+150,y+58),radius=8,fill=col,outline='#607763',width=2); d.text((x+16,y+19),label,font=mono,fill='#18221F')
d.line((915,210,950,290),fill='#A95F32',width=5);d.line((1025,328,875,370),fill='#A95F32',width=5);d.line((950,428,1010,438),fill='#A95F32',width=5)
d.text((80,550),'Brisbane + remote Australia  /  Email Simon',font=mono,fill='#18221F')
im.save('social-card.png',optimize=True)
