from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import sys,hashlib,urllib.request,time,json
root=Path('public') if Path('public/index.html').exists() else Path('.')
sections=('about','projects','skills','collection','training','contact')
pages=['index.html',*(f'{section}/index.html' for section in sections)]
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.refs=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  for key in ['src','href','srcset']:
   if key in a:self.refs.append(a[key])
parsed={}
for name in [*pages,'404.html']:
 p=Parser();p.feed((root/name).read_text(encoding='utf-8'));parsed[name]=p
 assert p.h1==1 and len(p.ids)==len(set(p.ids)),name
for name,p in parsed.items():
 for ref in p.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  target=root/unquote(u.path).lstrip('/') if u.path.startswith('/') else (root/name).parent/unquote(u.path) if u.path else root/name
  if target.is_dir():target=target/'index.html'
  assert target.is_file(),(name,ref)
  if u.fragment:assert u.fragment in parsed[target.relative_to(root).as_posix()].ids,(name,ref)
 main_sections=set(p.ids)&{'top',*sections}
 expected={'top'} if name=='index.html' else set() if name=='404.html' else {name.split('/')[0]}
 assert main_sections==expected,(name,main_sections)
assert 'project-lp-001' in parsed['collection/index.html'].ids
assert (root/'assets/cv/Ammar_Aikan_ATS_CV.pdf').read_bytes().startswith(b'%PDF-')
print('Static assets, anchors, headings and PDF checks passed.')
if len(sys.argv)>1:
 base=sys.argv[1].rstrip('/')+'/'
 for attempt in range(8):
  try:
   for name in [*pages,'assets/img/ammar-cutout.webp','assets/cv/Ammar_Aikan_ATS_CV.pdf','assets/cv/Ammar_Aikan_ATS_CV.docx']:
    route=name.removesuffix('index.html')
    with urllib.request.urlopen(base+route+'?verify='+str(time.time_ns()),timeout=20) as r:data=r.read()
    expected=(root/name).read_bytes()
    assert hashlib.sha256(data).digest()==hashlib.sha256(expected).digest(),'Live content differs: '+name
    print(json.dumps({'url':base+route,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}))
   print('LIVE_CONTENT_VERIFIED');break
  except Exception as exc:
   print('Attempt',attempt+1,str(exc))
   if attempt==7:raise
   time.sleep(10)
