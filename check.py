import sys; sys.path.insert(0, '/Users/shinojimakouhei/.gemini/antigravity/scratch/project_storage')
import gws_api
SID = '162WbimQ7ENtfuYpRRg6DwXJbp-bBaRsPB0-GNWdoTqU'
hdr = gws_api.sheets_read(SID, "'⏳ 承認待ち'!A1:T1")
print('HEADERS:')
for i, h in enumerate(hdr[0] if hdr else []):
    print(f'  {i}({chr(65+i)}): {h}')
rows = gws_api.sheets_read(SID, "'⏳ 承認待ち'!A2:T10")
if rows:
    print('\nSTATUS VALUES (col H=index7):')
    for r in rows[:8]:
        padded = r + ['']*(20-len(r))
        print(f'  [{repr(padded[7])}] task=[{padded[4][:40]}]')
