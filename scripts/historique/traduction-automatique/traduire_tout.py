# -*- coding: utf-8 -*-
"""Translate Prema Kavali Hindi V7 into French with local NLLB, preserving 143 human-reviewed draft subtitles."""
import argparse,csv,re,sys,os
from pathlib import Path

def read_srt(path):
    raw=Path(path).read_text(encoding='utf-8-sig').replace('\r\n','\n').strip()
    blocks=re.split(r'\n\s*\n',raw)
    entries=[]
    for block in blocks:
        parts=block.splitlines()
        if len(parts)<3 or not parts[0].strip().isdigit() or '-->' not in parts[1]:
            raise ValueError('Invalid SRT block: '+repr(block[:150]))
        start,end=[a.strip() for a in parts[1].split('-->',1)]
        entries.append((int(parts[0]),start,end,' '.join(x.strip() for x in parts[2:] if x.strip())))
    return entries

def save_srt(entries,path):
    with Path(path).open('w',encoding='utf-8-sig',newline='\n') as f:
        for n,start,end,t in entries:
            f.write(f'{n}\n{start} --> {end}\n{t}\n\n')

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--model',default='facebook/nllb-200-distilled-600M')
    p.add_argument('--batch-size',type=int,default=4)
    p.add_argument('--cpu',action='store_true',help='Force CPU')
    args=p.parse_args()
    base=Path(__file__).resolve().parent
    source=read_srt(base/'Prema_Kavali_Hindi_V7.srt')
    known=read_srt(base/'Prema_Kavali_FR_001-143.srt')
    if len(source)!=1597 or len(known)!=143:
        raise SystemExit(f'Unexpected entry count: {len(source)=}, {len(known)=}')
    for i,k in enumerate(known):
        s=source[i]
        if s[:3]!=k[:3]: raise SystemExit(f'Timecode mismatch at {i+1}')
    try:
        import torch
        from transformers import AutoTokenizer,AutoModelForSeq2SeqLM
    except ImportError:
        raise SystemExit('Dependencies missing. Run Installer.ps1, then retry.')
    device='cuda' if (torch.cuda.is_available() and not args.cpu) else 'cpu'
    print('Device:',device,flush=True)
    print('Loading NLLB model (first run downloads ~2.5GB)...',flush=True)
    tokenizer=AutoTokenizer.from_pretrained(args.model,src_lang='hin_Deva')
    model=AutoModelForSeq2SeqLM.from_pretrained(args.model).to(device)
    model.eval()
    if 'fra_Latn' not in tokenizer.lang_code_to_id:
        raise SystemExit('Missing fra_Latn language code')
    bos=tokenizer.lang_code_to_id['fra_Latn']
    cache=base/'traduction_progression.tsv'
    result={}
    if cache.exists():
        with cache.open(encoding='utf-8',newline='') as f:
            for row in csv.reader(f,delimiter='\t'):
                if len(row)==2 and row[0].isdigit(): result[int(row[0])]=row[1]
    problems=[]
    for i in range(143,len(source),args.batch_size):
        group=[s for s in source[i:i+args.batch_size] if s[0] not in result]
        if not group: continue
        texts=[]
        for n,a,b,t in group:
            # Do not feed Unicode replacement characters to translation model.
            if '�' in t or not t.strip():
                result[n]='[Paroles indistinctes — à vérifier]'
                problems.append((n,a,'Source illisible',t))
            else: texts.append((n,t))
        if texts:
            inputs=tokenizer([t for n,t in texts],return_tensors='pt',padding=True,truncation=True,max_length=256).to(device)
            with torch.inference_mode():
                output=model.generate(**inputs,forced_bos_token_id=bos,max_new_tokens=200,num_beams=4)
            for (n,t),translated in zip(texts,tokenizer.batch_decode(output,skip_special_tokens=True)):
                translated=' '.join(translated.split()).strip()
                result[n]=translated or '[Paroles indistinctes — à vérifier]'
                if not translated or re.search(r'[\u0900-\u097f]',translated):
                    problems.append((n,source[n-1][1],'Hindi retained in translation',translated))
        # Persist after every batch to resume if interrupted
        with cache.open('w',encoding='utf-8',newline='') as f:
            writer=csv.writer(f,delimiter='\t'); writer.writerows(sorted(result.items()))
        done=len(result)
        if done%40<args.batch_size: print(f'Translated {done}/1454 remaining subtitles',flush=True)
    out=[]
    for n,a,b,t in source:
        fr=known[n-1][3] if n<=143 else result.get(n,'[Paroles à vérifier]')
        out.append((n,a,b,fr))
    save_srt(out,base/'Prema_Kavali_FR_CA_COMPLET_AUTOMATIQUE_A_REVISER.srt')
    for n,a,b,fr in out:
        if '�' in fr or '[' in fr or re.search(r'[\u0900-\u097f]',fr) or len(fr)>95 or (n>143 and len(fr)<2):
            problems.append((n,a,'Review translation',fr))
    with (base/'Prema_Kavali_relecture_necessaire.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f);w.writerow(['numero','debut','motif','texte']);w.writerows(problems)
    print(f'DONE: {len(out)} subtitles; French SRT saved to {base / "Prema_Kavali_FR_CA_COMPLET_AUTOMATIQUE_A_REVISER.srt"}',flush=True)
    print('Note: this is machine translation, NOT audio-verified, and a French-Canadian linguistic revision is needed.')

if __name__=='__main__': main()
