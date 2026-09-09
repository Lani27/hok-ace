"""Build the English beginner guide. Run from any directory; standard library only."""
from pathlib import Path
from html import escape as e
import struct
from beginner_content import RULES, TACTICIANS, KEYWORDS, VIDEOS, keyword_video_slug
from beginner_lineups import LINEUPS, CARD_EFFECTS

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'docs/assets/beginner-guide'
PREFIX = '../assets/beginner-guide/'

def img(name, alt, zoom=False):
    path = ASSETS / name
    if not path.exists():
        raise FileNotFoundError(f'Missing required asset: {path}')
    dimensions = ''
    if path.suffix == '.png':
        width, height = struct.unpack('>II', path.read_bytes()[16:24])
        dimensions = f' width="{width}" height="{height}"'
    tag = f'<img src="{PREFIX}{name}" alt="{e(alt)}"{dimensions} loading="lazy">'
    return f'<button class="zoom" type="button" aria-label="Enlarge {e(alt)}">{tag}</button>' if zoom else tag

def video(vid, title, poster=None):
    content = (img(poster, title) + '<span class="play" aria-hidden="true">▶</span>') if poster else '▶ Watch original video (Chinese) ↗'
    cls = 'video-link' if poster else 'button'
    return f'<a class="{cls}" href="https://wxq.qq.com/cp/a202609xszy/index.html" data-video="{vid}" target="_blank" rel="noopener" aria-label="{e(title)} — original Chinese-language video">{content}</a>'

def tabs(group, labels, extra=''):
    label = 'Chessplayers' if group == 'tacticians' else group
    out = f'<div class="tabs {extra}" role="tablist" aria-label="{e(label)}" data-tabs>'
    for i, label in enumerate(labels):
        out += f'<button type="button" role="tab" id="{group}-tab-{i}" aria-controls="{group}-{i}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">{label}</button>'
    return out + '</div>'

def panel(group, i, cls=''):
    return f'<div role="tabpanel" class="{cls}" id="{group}-{i}" aria-labelledby="{group}-tab-{i}"' + (' hidden' if i else '') + '>'

def dl(items):
    return '<dl>' + ''.join(f'<dt>{e(title)}</dt><dd>{e(text)}</dd>' for title, text in items) + '</dl>'

def build():
    banner = (ROOT/'templates/unofficial-banner.html').read_text(encoding='utf-8')
    body = [banner, '<nav class="site-nav" aria-label="Guide sections"><a href="../index.html">HoK: ACE · English</a>']
    body += [f'<a href="#{key}">{title}</a>' for key,title in [('rules','Basic rules'),('lineups','Starter lineups'),('tacticians','Chessplayers'),('keywords','Keywords'),('videos','Expert guides')]]
    body += ['</nav><h1 class="sr-only">Honor of Kings: ACE — Beginner Guide</h1><div class="masthead">', img('part1-en.png','Your ACE Journey — Honor of Kings: ACE Beginner Guide').replace('loading="lazy"','fetchpriority="high"'), '</div>',
     '<div class="source-row"><a href="https://wxq.qq.com/cp/a202609xszy/index.html" target="_blank" rel="noopener">View this guide on the official Chinese site ↗</a><a href="https://wxq.qq.com/" target="_blank" rel="noopener">Official downloads ↗</a><span>Chinese-server guide · September 2026</span></div><main>',
     '<section id="rules"><h2><span>01</span>Basic rules</h2><p class="section-intro">Learn the essentials and get ready for your first match.</p>', tabs('rules', [e(r[0]) for r in RULES])]
    for i, (name, vid, slides) in enumerate(RULES):
        body.append(panel('rules',i,'panel'))
        body.append('<div data-carousel>')
        for j,(title,text) in enumerate(slides):
            body.append(f'<div class="slide"'+(' hidden' if j else '')+'>'+img(f'swiper{i+1}_{j+1}-en.png',title,True)+f'<div><span class="slide-count">{j+1:02}</span><h3>{e(title)}</h3><p>{e(text)}</p></div></div>')
        if len(slides)>1:
            body.append(f'<div class="slide-controls"><button type="button" data-direction="-1" aria-label="Previous {e(name)} slide">‹</button><span data-counter aria-live="polite">1 / {len(slides)}</span><button type="button" data-direction="1" aria-label="Next {e(name)} slide">›</button></div>')
        body.append('</div><p class="zoom-note">Select an image to enlarge it.</p>'+video(vid,name)+'</div>')
    body.append('</section><section id="lineups"><h2><span>02</span>Starter lineups</h2><p class="section-intro">Five beginner builds, with quick diagrams, detailed guides, and original videos.</p>')
    labels=[img(x['avatar']+'_avatar.png','')+f'<span>{e(x["name"])}<strong>{e(x["hero"])}</strong></span>' for x in LINEUPS]
    body.append(tabs('lineups',labels,'lineup-tabs'))
    for i, x in enumerate(LINEUPS):
        body.append(panel('lineups',i,'panel')+f'<div class="lineup-header"><div><h3>{e(x["name"])}</h3><p>Main carry: {e(x["hero"])}</p></div><div><button type="button" class="button" data-code="{i+1}">Copy lineup code</button><p class="status" role="status"></p></div></div>')
        sub=f'lineup-view-{i}'
        body.append(tabs(sub,['Quick overview','Detailed infographic','Video tutorial']))
        body.append(panel(sub,0,'guide-image')+img(f'guide_{i+1}_2-en.png',x['name']+' quick overview',True)+'</div>')
        body.append(panel(sub,1,'long-guide')+img(f'guide_{i+1}_3-en.png',x['name']+' detailed infographic',True)+'</div>')
        body.append(panel(sub,2)+video(x['video'],x['name'],f'video_poster_{i+1}-en.png')+'<p class="language">Original video in Chinese; plays in the original Tencent player.</p></div>')
        body.append('<p class="zoom-note">Select a diagram to enlarge it. Some small labels in the AI-edited artwork may be imperfect; use the text guide below for precise hero names and effects.</p><details class="text-guide"><summary>Read the complete English text guide</summary>')
        body.append('<h4>Core lineup</h4><p>'+e(x['roster'])+'</p><h4>How it works</h4><p>'+e(x['logic'])+'</p><h4>Practical tips</h4><ul>'+''.join('<li>'+e(t)+'</li>' for t in x['tips'])+'</ul><h4>Round-by-round plan</h4>')
        for label,text in zip(['Rounds 1–3','Rounds 4–7','Rounds 8–11','Round 12+'],x['rounds']):
            body.append('<div class="rounds"><strong>'+label+'</strong><div>'+e(text)+'</div></div>')
        body.append('<h4>Recommended equipment</h4>'+dl(x['equipment'])+'<h4>Recommended Chessplayers</h4>'+dl(x['tacticians'])+'<h4>Recommended talents</h4>'+dl(x['talents'])+'<h4>Hero card effects</h4>'+dl(CARD_EFFECTS[i])+'</details></div>')
    body.append('<details class="import"><summary>How to import a lineup</summary>')
    instructions=['Copy the lineup code, sign in to the game, and select Lineups in the lower-right corner of the lobby.','Select Saved Lineups, then Import Lineup in the lower-right corner.','If your saved lineups are full, select a lineup to replace and press Replace.']
    for i,text in enumerate(instructions):
        body.append(f'<figure><figcaption><strong>Step {i+1}.</strong> {e(text)}</figcaption>'+img(f'step{i+1}-en.png',f'Lineup import step {i+1}',True)+'</figure>')
    body.append('</details><p><a href="https://wxq.qq.com/cp/a20260707sfgw/teamlist.html" target="_blank" rel="noopener">More lineups on the official Chinese site ↗</a></p></section>')
    body.append('<section id="tacticians"><h2><span>03</span>Recommended Chessplayers</h2><p class="section-intro">Explore each Chessplayer’s skill, Secret Skill, and exclusive talent.</p>'+tabs('tacticians',[e(t[0]) for t in TACTICIANS]))
    for i,(name,asset,blurb,skills) in enumerate(TACTICIANS):
        body.append(panel('tacticians',i,'panel tactician')+'<div class="portrait">'+img(f'hero/{asset}.png',name)+'</div><div><h3>'+e(name)+'</h3><p>'+e(blurb)+'</p>')
        group=f'skill-{i}'
        labels=[img(f'hero/skill{i+1}_{j+1}.png','')+label for j,label in enumerate(['Skill','Secret Skill','Exclusive'])]
        body.append(tabs(group,labels,'skill-tabs'))
        for j,entries in enumerate(skills):
            body.append(panel(group,j,'skill-panel skill-copy')+''.join('<h4>'+e(title)+'</h4><p>'+e(text)+'</p>' for title,text in entries)+'</div>')
        body.append('</div></div>')
    body.append('</section><section id="keywords"><h2><span>04</span>Keyword dictionary</h2><p class="section-intro">Understand the effects written on your cards. Each short demonstration is available with English subtitles and original Chinese audio.</p><label class="search">Search keywords<input id="keyword-search" type="search" placeholder="Try: combat, levels, revive…"></label><p id="keyword-status" class="status" role="status">13 keywords shown</p><div class="keywords">')
    for name,text,vid in KEYWORDS:
        clip = 'keyword-videos/' + keyword_video_slug(name) + '-en.mp4'
        if not (ASSETS / clip).is_file():
            raise FileNotFoundError(f'Missing subtitled keyword video: {clip}')
        body.append('<article class="keyword"><h3>'+e(name)+'</h3><p>'+e(text)+f'</p><div class="keyword-actions"><a class="button" href="{PREFIX}{clip}" data-subtitled-video="{e(name)}" aria-label="{e(name)} — watch with English subtitles">▶ Watch with English subtitles</a><a href="https://wxq.qq.com/cp/a202609xszy/index.html" data-video="{vid}" target="_blank" rel="noopener">▶ Original demonstration · Chinese ↗</a></div></article>')
    body.append('<dialog id="subtitled-video-dialog" aria-labelledby="subtitled-video-title"><div class="dialog-bar"><strong id="subtitled-video-title">Keyword demonstration</strong><button type="button">Close ×</button></div><video controls playsinline preload="none" aria-label="Keyword demonstration with English subtitles"></video><p class="language">English subtitles · Original Chinese audio and game interface · Unofficial fan translation</p><p class="status" role="status"></p><a class="download-video" href="#" download>Download subtitled video</a></dialog>')
    body.append('</div></section><section id="videos"><h2><span>05</span>Expert guides</h2><p class="section-intro">More builds from the creators featured on the official site.</p><p class="video-note">Video titles and thumbnails are translated. The linked videos retain their original Chinese audio and on-screen text.</p><div class="video-grid">')
    for n,title,subtitle,author,vid in VIDEOS:
        body.append('<article class="video-card">'+video(vid,title,f'video_poster{n}-en.png')+'<div><h3>'+e(title)+'</h3><p>'+e(subtitle)+'</p><p>By '+e(author)+' · Chinese-language video</p></div></article>')
    body.append('</div></section></main><footer>Unofficial fan translation of Tencent’s September 2026 beginner guide. Original artwork and game content belong to Tencent and their respective owners. Image text was localized with AI-assisted editing; minor visual differences may be present. English names are fan translations and may differ from the international release. <a href="https://wxq.qq.com/cp/a202609xszy/index.html">Official source</a> · <a href="https://github.com/Lani27/hok-ace">Repository</a> · <a href="../index.html">All translations</a></footer><dialog id="video-dialog" aria-label="Original Chinese-language video"><div class="dialog-bar"><span>Original video · Chinese audio and text</span><button type="button">Close ×</button></div><div id="video-player"></div><p class="video-status" role="status"></p><p><a href="https://wxq.qq.com/cp/a202609xszy/index.html" target="_blank" rel="noopener">Watch on the official Chinese guide ↗</a></p></dialog><dialog id="image-dialog" aria-label="Enlarged guide image"><div class="dialog-bar"><a href="#" target="_blank" rel="noopener">Open full-resolution image ↗</a><button type="button">Close ×</button></div><img alt=""></dialog>')
    css=(ROOT/'templates/beginner-guide.css').read_text(encoding='utf-8')
    js=(ROOT/'templates/beginner-guide.js').read_text(encoding='utf-8')
    html='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Honor of Kings: ACE — Beginner Guide in English</title><meta name="description" content="Unofficial English translation of the official HoK: ACE beginner guide: rules, five starter lineups, Chessplayers, keywords, and translated artwork."><style>'+css+'</style></head><body>'+''.join(body)+'<script>'+js+'</script></body></html>'
    output=ROOT/'docs/guides/beginner-guide.html'
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(html,encoding='utf-8')
    print(f'Built {output.name}: {len(html):,} characters; 21 rule slides, 5 lineups, 5 Chessplayers, 13 keywords, 12 expert videos.')

if __name__=='__main__':
    build()
