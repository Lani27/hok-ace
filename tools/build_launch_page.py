"""Build GitHub Pages output from the translated article and shared templates."""
from pathlib import Path
from html import escape
import struct

PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT / 'docs'
ASSETS = ROOT / 'assets' / 'launch'

# Translated from the supplied Tencent Camp launch announcement. Image dates
# intentionally retain the source graphics, including differences from the prose.
GROUPS = [
    ('Honor of Kings crossover rewards', [
        ('Lucky bags: free HOK limited-time tokens', 'September 10, after launch – October 7, 23:59',
         'Log in each day and open lucky bags to collect Honor of Kings limited-time tokens. Play Honor of Kings: ACE to earn them faster, up to a total of 1,000. Log in on 7 days to claim the Little Daji — Sea Salt & Orange Blossom skin in ACE. Golden lucky bags also offer a chance to win cash; reach Silver rank to withdraw it.', [4]),
        ('Claim Arli’s new Honor of Kings skin', 'September 10, after launch – September 30, 23:59',
         'Register in ACE to receive 5 Honor Draw Vouchers. Complete 1 ACE match each day to advance through the event stages and claim HOK Star Coins, limited-time voice lines, a Sprite outfit, and ACE Rose Coins. The final reward is Arli’s new Shimmering Butler skin in Honor of Kings.', [5]),
        ('Find your perfect Chessplayer', 'September 7 – October 7, 23:59',
         'Take the quiz to discover your ACE Chessplayer match. Participate to receive The Cards Are Fine avatar frame in Honor of Kings. Players who previously played HOK Simulation Battle, and players who join through a friend’s shared link, can also claim the exclusive Training Sandtable board in ACE.', [6]),
    ]),
    ('Honor of Kings: ACE launch rewards', [
        ('Free Treasure Coins at launch', 'Launch events and ongoing season rewards',
         'Join the ACE City reward collection from September 10, after launch, through October 14 at 23:59. Level up your Growth Journey: every 5 levels from Level 5 to Level 40 awards 30 Treasure Coins, for up to 240 in total. Climb the ACE Tournament ranks to claim up to 60 more Treasure Coins through the ongoing season rewards. The Seven Steps to Victory event also awards 6 Treasure Coins on your fourth login day. Use them to draw for collection rewards.', [7, 8]),
        ('Earn Rose Coins for Ying Lu — Elegant Lover', 'September 10, after launch – October 14, 23:59',
         'Climb the ranks to earn Rose Coins. Rank milestones award 200 in total: Silver 20, Gold 30, Platinum 40, Diamond 50, and Star 60. From Platinum onward, post-match card flips can award additional Rose Coins.\nSpend Rose Coins in the ongoing S1 exchange on skins such as Ying Lu — Elegant Lover. A skin costs 200 Rose Coins; avatars, avatar frames, emotes, and chat bubbles cost 50 each.', [9, 10]),
        ('Seven-day login: a Chessplayer and a board', 'From September 10 • Ongoing',
         'Unlocked after launch. Log in on 7 days to claim a reward each day: Day 1 — 200 Diamonds; Day 2 — Zhuang Xiaoyu Chessplayer; Day 3 — 1 Lineup Slot Card; Day 4 — 6 Treasure Coins; Day 5 — Dimensional Collapse attack effect for 30 days; Day 6 — Random Chessplayer Trial Card for 3 days; Day 7 — ACE Supermarket board.', [11]),
        ('Begin your journey: a Chessplayer and a skin', 'From September 10 • Ongoing',
         'Eight days of missions unlock in sequence after launch. Complete 3 daily missions to earn 15 Journey Points. Exchange points for the Qiao Xi Chessplayer and Qiao Xi — Crimson Koi Dream skin. Complete every mission to unlock challenge missions that award another 500 Diamonds. These challenge missions have a 90-day time limit.', [12]),
        ('Complete practice stages to unlock Naonao', 'From September 10 • Ongoing',
         'Complete any 3 reinforcement practice stages to claim the Naonao Chessplayer. These stages help you move into training matches and learn basic lineups and battle techniques.', [13]),
        ('Link HOK and ACE data for an avatar frame', 'September 10, after launch – October 7, 23:59',
         'Authorize the sharing of friend online status, Intimacy, and Sprite data between the two games to receive the ACE-exclusive The Cards Are Fine avatar frame.', []),
        ('Wang Wei event: a chat bubble', 'September 10, after launch – October 7, 23:59',
         'Join the new hero Wang Wei for an encounter across a thousand years. Complete the designated event missions to receive 200 Diamonds and the Voices in the Empty Mountains chat bubble.', []),
        ('King rank milestones', 'September 10, after launch – December 9, 23:59',
         'Work together across the server to reach King rank. As more players reach King, server-wide milestones unlock Diamond rewards and modes such as Diamond Frenzy and Ace Showdown. See the in-game event page for the exact milestones and rewards. The first 9,999 players on the server to reach King also earn an exclusive Launch Founder title, numbered according to their order of achievement. Claim it through the achievement system.', []),
        ('Raise a Super Ace hero', 'September 10, after launch – October 7, 23:59',
         'Raise your favorite hero to Level 100 in ranked matches to earn votes for that hero. Participate each week to receive 1 random Tier 1 Hero Card, up to 5 cards during the event.', []),
        ('Fast track to ACE mastery', 'Ongoing',
         'Complete 4 challenge missions to become an ACE expert and earn up to a 100% bonus to rank points. This event and its rank-point bonus end when you reach Platinum, and its entry disappears.', []),
        ('Team up with an expert', 'September 10, after launch – December 9, 23:59',
         'Players at Platinum or above are Experts; players below Platinum are Rising Stars. An Expert and a Rising Star can form a one-to-one partnership. The mentoring is complete when the Rising Star reaches Platinum. Experts earn rewards based on how many players they help: avatar frames, Intimacy items, and rank-protection cards for Platinum, Diamond, Star, and King. A leaderboard tracks the server’s most successful mentors.', []),
        ('One-to-one coaching', 'September 10, after launch – December 9, 23:59',
         'Receive coaching for the first time to claim 100 Diamonds once. Coach other players 1, 3, 5, and 10 times to earn Diamond rewards. Coaching 200 times also awards an exclusive title through the achievement system. A successful coaching session requires finishing the match together with your student and placing in the top three.', []),
        ('ACE guide videos', 'September 10, after launch – September 23, 23:59',
         'Watch the launch tutorial videos to learn about ACE Season 1. Watch each video for at least 10 seconds to claim 50 Diamonds for that video.', []),
        ('Share the wins', 'September 10, after launch – December 9, 23:59',
         'Play together for rewards. Complete 1 match in a team to receive an emote, 3 team matches to receive an Intimacy item, and 5 team matches to receive another emote.', []),
        ('Log in on mobile and PC for Diamonds', 'September 10, after launch – December 9, 23:59',
         'Log in on mobile to claim 200 Diamonds, then log in on PC to claim another 200. The event entry disappears after completion.', []),
        ('Season journey', 'September 10, after launch – December 9, 23:59',
         'Beta players can review their beta data and see the beta-related rewards carried over to launch. All players can use the Season Journey to explore the current season’s new content and progress.', []),
    ]),
    ('Launch discounts', [
        ('Top up ¥1 for an exclusive board', 'From September 10, after launch • Ongoing',
         'Join the One-Yuan Gift event and top up ¥1 to receive the Epic Dreamland District board, valued at 888 Tokens. After topping up, return to the One-Yuan Gift event page to claim the board.', [14]),
        ('Naonao — Feeling Blue flash sale', 'September 10, after launch – September 23, 23:59',
         'The Naonao — Feeling Blue Fun skin, valued at 488 Tokens, is available for 60 Tokens during the event.', [15]),
        ('Shop skins: up to 50% off', 'September 10, after launch – September 23, 23:59',
         'Shop skins have limited-time launch discounts. Epic skins are 50% off, and new Legendary skins are 20% off. Crossed-out prices indicate the planned non-event prices after this promotion ends; actual prices are those shown in the shop at that time.', [16]),
        ('First 50 Treasure bundles: half price', 'September 10, after launch – September 23, 23:59',
         'Treasure draws offer a chance to obtain an ACE Crystal, which can be exchanged for the Ink Dragon collection skin or the Sea of Clouds Dreamscape collection board. During the event, your first 50 purchases of the Treasure bundle are 50% off: 30 Tokens for 6 Treasure Coins instead of the regular 60 Tokens.', [17]),
    ]),
]

def picture(number, label):
    path = ASSETS / f'{number:02}-en.png'
    image_bytes = path.read_bytes()
    width, height = struct.unpack('>II', image_bytes[16:24])
    return f'<figure><img src="../assets/launch/{number:02}-en.png" alt="{escape(label)}" width="{width}" height="{height}" loading="lazy"></figure>'

def build():
    missing = [f'{i:02}-en.png' for i in range(1,18) if not (ASSETS/f'{i:02}-en.png').exists()]
    if missing:
        raise SystemExit('Missing translated assets: ' + ', '.join(missing))
    nav, body = [], []
    for group_index, (group, entries) in enumerate(GROUPS, 1):
        nav.append(f'<details open><summary><a href="#group-{group_index}">{escape(group)}</a></summary><ul>')
        body.append(f'<section id="group-{group_index}"><h2>{escape(group)}</h2>')
        for index, (title, dates, text, images) in enumerate(entries, 1):
            anchor = f'event-{group_index}-{index}'
            nav.append(f'<li><a href="#{anchor}">{escape(title)}</a></li>')
            body.append(f'<section id="{anchor}" class="event"><h3>{escape(title)}</h3><p class="dates">{escape(dates)}</p>')
            body.extend(f'<p>{escape(p)}</p>' for p in text.split('\n'))
            body.extend(picture(i, title) for i in images)
            body.append('</section>')
        body.append('</section>')
        nav.append('</ul></details>')
    intro = '''<h1>Honor of Kings: ACE<br>Launch &amp; Rewards Preview</h1>
<p class="byline">Honor of Kings: ACE</p>
<p>Pre-download is now available. The game launches on all supported platforms on <strong>September 10 at 07:00</strong>.</p>
<h3>How to download</h3>
<ol><li><strong>Android and HarmonyOS:</strong> Find the game through QQ, WeChat, app stores, or game centers. You can also use the ACE section in King’s Camp or the download message from the official ACE — Bai Ge WeCom service account.</li>
<li><strong>iOS:</strong> Find the game in the App Store.</li>
<li><strong>PC:</strong> Download the official PC client from <a href="https://wxq.qq.com/">wxq.qq.com</a>, or find the game in WeGame.</li></ol>
<p>ACE supports Android, iOS, HarmonyOS, and PC, with shared progress across all platforms.</p>'''
    publisher = '../assets/launch/publisher.png'
    intro = intro.replace('<p class="byline">', f'<p class="byline"><img src="{publisher}" alt="" style="display:inline-block;width:40px;height:40px;border-radius:50%;vertical-align:middle;margin-right:12px">')
    intro += picture(1, 'ACE launches September 10 with mobile and PC cross-play')
    intro += '<p>Launch gifts include HOK limited-time tokens and Arli’s new skin, plus ACE Treasure Coins, Epic boards, and more. Here are the rewards available across both games.</p>'
    intro += picture(2, 'Honor of Kings crossover reward overview')
    intro += picture(3, 'ACE launch reward overview')
    intro += '''<aside class="note"><strong>About this English copy.</strong> This translates the Chinese-server announcement; it does not announce a global release. Event times are retained as published. Some overview graphics use different dates from the article: the Arli promotion begins September 9 in the overview but September 10 in the text; the Chessplayer quiz begins September 7 in the text but September 10 in its screenshot. The HOK avatar-frame overview also shows September 7–22. These differences are preserved. Check the in-game event page for the applicable schedule. English cosmetic names are descriptive translations where an official name was not verified. Images were localized with AI and may contain small artwork or fine-text differences.</aside>'''
    css = '''*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:24px}body{margin:0;color:#253442;background:radial-gradient(ellipse at 0 45%,#d4e4f3,transparent 65%),#e8f0f6;font:16px/1.75 "Segoe UI",Arial,sans-serif}a{color:#3155a0;text-underline-offset:3px}main{max-width:1280px;margin:0 auto;padding:52px 32px;display:grid;grid-template-columns:minmax(0,930px) 250px;gap:36px}article{min-width:0}h1{font-size:32px;line-height:1.3;font-weight:550;margin:0 0 26px}h2{font-size:25px;color:#244774;border-bottom:1px solid #adc4dc;padding:24px 0 10px;margin-top:38px}h3{font-size:21px;line-height:1.45;margin:27px 0 10px;font-weight:600}p{margin:14px 0}li{margin:7px 0}figure{margin:22px 0}figure a{display:block}img{display:block;width:100%;height:auto;border-radius:5px}.byline{padding:15px 22px;background:#ffffff45;border-radius:40px;border:1px solid #ffffff80}.dates{color:#375773;font-weight:600;font-size:15px}.note{font-size:14px;line-height:1.65;background:#ffffff66;border-left:3px solid #7798c5;padding:16px 19px;margin-top:25px}nav{position:sticky;top:24px;align-self:start;max-height:calc(100vh - 48px);overflow:auto;font-size:14px;line-height:1.5}nav h2{font-size:18px;margin:0;padding:14px 16px;background:linear-gradient(120deg,#6c92c9,#415d8f);color:white;border:0}nav summary{padding:13px 12px;background:#d6e3ef;cursor:pointer;font-weight:600}nav a{color:inherit;text-decoration:none}nav a:hover{text-decoration:underline;color:#245bb5}nav ul{padding:5px 12px 9px 28px;margin:0}nav li{margin:9px 0}footer{font-size:13px;color:#566f83;border-top:1px solid #b7cbdc;margin-top:40px;padding-top:18px}@media(max-width:900px){main{display:block;padding:26px 20px}nav{position:static;max-height:none;margin-bottom:28px}nav details{display:none}nav h2{display:none}h1{font-size:28px}h2{font-size:24px}h3{font-size:20px}}@media print{body{background:white}main{display:block;padding:0}nav{display:none}figure{break-inside:avoid}h2,h3{break-after:avoid}.note{font-size:11px}}'''
    content = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Honor of Kings: ACE — Launch &amp; Rewards Preview</title><style>' + css + '</style></head><body><main><article>' + intro + ''.join(body) + '<footer>English reading copy of the Tencent Camp launch announcement. Original game artwork and event content belong to their respective owners. All 17 localized images are embedded for offline viewing.</footer></article><nav aria-label="Contents"><h2>Contents</h2>' + ''.join(nav) + '</nav></main></body></html>'
    banner = (PROJECT / 'templates' / 'unofficial-banner.html').read_text(encoding='utf-8')
    content = content.replace('<body>', '<body>' + banner, 1)
    content = content.replace('<h1>Honor of Kings: ACE', '<p><a href="../index.html">← All translations</a></p><h1>Honor of Kings: ACE', 1)
    content = content.replace('All 17 localized images are embedded for offline viewing.', 'Unofficial fan translation. All 17 images have been localized into English.')
    output = ROOT / 'announcements' / 'launch-rewards.html'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content, encoding='utf-8')
    index = (PROJECT / 'templates' / 'index.html').read_text(encoding='utf-8')
    (ROOT / 'index.html').write_text(index.replace('<!-- UNOFFICIAL_BANNER -->', banner), encoding='utf-8')
    print(f'Built {output.name}: {output.stat().st_size:,} bytes; 17 images; {sum(len(entries) for _, entries in GROUPS)} events.')

if __name__ == '__main__':
    build()
