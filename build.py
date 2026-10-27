# Gera index.html a partir de template.html + br_paths.json (mapa). Os dados das vagas ficam dentro de template.html (JOBS / JOBS.push).
import json
g=json.load(open('br_paths.json'))
t=open('template.html',encoding='utf-8').read()
t=t.replace('__GEO__',json.dumps({'paths':g['paths'],'proj':g['proj']},separators=(',',':'))).replace('__W__',str(g['w'])).replace('__H__',str(g['h']))
open('index.html','w',encoding='utf-8').write(t)
print('ok', len(t))
