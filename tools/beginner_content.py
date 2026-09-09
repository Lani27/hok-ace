"""English copy translated from Tencent's September 2026 beginner guide."""
RULES = [
 ('ACE Tournament','y1285cnprk7',[
  ('Choose your tactician','Six tacticians compete in the ACE Tournament. Each starts with 60 Health.'),
  ('Build your lineup','Buy cards to build a lineup. Each round, you face a randomly selected opponent. The winner deals damage to the loser’s Health.'),
  ('Find synergies','Use your heroes’ card effects together to strengthen your lineup.'),
  ('Be the last survivor','A tactician is eliminated at 0 Health. The last tactician standing wins.')]),
 ('Tacticians','e12866xbiwl',[
  ('Unique skills','Every tactician has a unique skill. Select the skill button to see its details.'),
  ('Secret Techniques','Every tactician has a Secret Technique mission. Complete it to earn a Secret Technique Card.'),
  ('Exclusive talents','At tactician level 6, claim an exclusive talent with a powerful effect.'),
  ('Level up','Spend Energy to raise your tactician’s level. Each level-up unlocks one free talent. Levels marked with a unit-count icon also grant +1 deployment slot. Higher tactician levels increase the chance of finding higher-tier hero cards.'),
  ('Free tactician rotation','Before Platinum, free tacticians unlock according to your rank. After you reach Platinum, the standard weekly free rotation begins the following week.')]),
 ('Heroes','k1285b6imwl',[
  ('Deploy and combine','Drag a hero card onto the battlefield to deploy that hero. Playing a duplicate of an already deployed hero combines it with that hero and increases their level.'),
  ('Hero levels','Heroes start at level 1 when deployed. Their maximum level is 999.'),
  ('Hero details','Select a hero to view their detailed stats, skills, and other information.'),
  ('Card effects','Hero cards have different effects. Use them well to strengthen your lineup faster and win.'),
  ('Factions','Each hero belongs to a faction. Different factions have different playstyles.'),
  ('Positioning and roles','The right side of a card shows the hero’s role and recommended position.')]),
 ('Talents','f1284metmmu',[
  ('Choose one of three','Each tactician level-up lets you choose one of three talents for free. Talents come in tier 1 (Bronze), tier 2 (Silver), and tier 3 (Gold); higher tiers are stronger. All six players receive the same talent tier at the same level in a match. At Silver rank and above, you can refresh your talent choices once per match.')]),
 ('Energy','k1285pr5ujb',[
  ('Earning Energy','You receive a fixed amount of Energy each round. Unspent Energy carries over. Selling a hero card gives 1 Energy; selling a deployed hero also gives 1 Energy. Some talents and effect cards grant Energy too.'),
  ('Spending Energy','Hero cards always cost 3 Energy. An effect card’s cost appears in its upper-right corner. Leveling your tactician also costs Energy; the level-up button shows the current cost.')]),
 ('Auctions','c1285joyba5',[
  ('Place a bid','At set rounds, everyone enters an auction for hero cards, effect cards, and other rewards. Select an item and press Bid. There is no bidding cap. The highest bidder wins, and unsuccessful bids cost no Energy. If bids are tied, the earlier bid wins.'),
  ('Auction dividends','Effective bids go into a dividend pool. When the auction ends, the pool’s Energy is distributed among all players. Players with lower Health receive a larger share.'),
  ('Collect waiting-area drops','While players wait, random items drop every few seconds. More waiting players means more drops. Interaction items are most common; Energy and hero cards are rarer. Energy drops give 1 Energy, and hero drops are tier 1 or tier 2.')])
]

TACTICIANS = [
 ('Xiangxiang','xiangxiang','Bring your own firepower, then modify your weapon into different forms.',[
  [('Ultimate Ballista','At the start of combat, Xiangxiang attacks enemies with her weapon. Her base Attack is 20. Each tier 1–3 hero you have at level 10 or above grants her +20 Attack.')],
  [('Art of Artillery','Deal a cumulative 10/15/20/30 damage to tacticians to earn a Weapon Modification Secret Technique Card.'),('Weapon Modification','Xiangxiang gains +20% Attack. Choose one weapon modification.')],
  [('Full Firepower','Xiangxiang gains an Attack bonus of (the total level of your heroes × 0.5)%.')]]),
 ('Yaria','yaomei','Summon a fawn to absorb frontline damage and strengthen it through victories.',[
  [('Adorable Fawn','At the start of the game, Yaria summons her beloved fawn. It gains 2 levels each round, plus 4 more if you won the previous battle.')],
  [('Super-Adorable Fawn','Every 3 rounds, receive a Magical Fawn Secret Technique Card.'),('Magical Fawn · Taunt','After combat begins, the fawn moves between enemies without collision. Every 3 seconds, it taunts enemies within 1 tile. +8 levels.'),('Magical Fawn · Armored','The fawn can wear equipment and immediately equips a Frozen Storm. +10 levels.'),('Magical Fawn · Twin','At combat start, the fawn creates a copy of itself nearby. If you have won 5 battles this match, the fawn gains 12 levels. The original preview shows 0 wins.'),('Magical Fawn · Resonance','Double the fawn’s level.'),('Magical Fawn · Devotion','When the fawn dies, divide its levels evenly among your heroes as Temporary Levels.')],
  [('Giant Plush','The fawn gains 30 levels. Receive a Fawn’s Protection item.'),('Fawn’s Protection','Unique. 30% of the wearer’s incoming damage is transferred to the fawn.')]]),
 ('Bai Ge','baige','Combine heroes to earn copies, then split key cards with your Secret Technique.',[
  [('Inspired Stroke','After every 4 hero combinations, Bai Ge receives an Improvisation card.'),('Improvisation','Receive a copy of a random deployed hero.')],
  [('Born Talented','Use 6 Improvisation cards to receive an Inspiration Burst Secret Technique Card.'),('Inspiration Burst','Release 3 sword waves at 3 random non-awakened hero cards in your hand. Split each card into 2 Fleeting copies.')],
  [('Brilliant Talent','Receive a Prodigy card.'),('Prodigy','Select a hero and receive 4 copies of that hero’s card.')]]),
 ("Chang Xiao'e",'changxiaoe','Gain levels with an increasingly powerful skill and develop four elite heroes.',[
  [('Little Bunny’s Help','Use the skill to give a random hero +2 levels. For every previous use this match, the level gain increases by 1.')],
  [('Leaps and Bounds','When your heroes’ combined levels reach 50/150/375, receive a Bunny’s Blessing Secret Technique Card.'),('Bunny’s Blessing','Trigger Little Bunny’s Help once on each of 4 random deployed heroes. The base preview shows +2 levels.')],
  [('Moonlight Special','Whenever the bunny grants levels, every 5 levels also grant a random stat bonus: 15% Attack Speed, 2% physical and magical lifesteal, or 2 physical and magical Defense. Each time Little Bunny’s Help grants a total of 65 levels, receive a Bunny’s Blessing card.')]]),
 ('Naonao','naonao','Specialize in one faction and earn additional faction talents.',[
  [('Party Bubbles','Choose one of two random factions. Your skill then becomes: spend 1 Energy to receive a hero card from that faction.')],
  [('Happy Gathering','Deploy 6 heroes from your selected faction to earn a Plenty of Friends Secret Technique Card.'),('Plenty of Friends','Draw 4 random hero cards from the faction selected by your skill.')],
  [('Party Time','Receive a Join the Fun card.'),('Join the Fun','Choose one of three talents associated with the faction selected by your skill.')]])
]

KEYWORDS = [
 ('Deploy','Triggers after you play this card.','d1284dm1gdr'),
 ('Engage','Triggers at the start of combat.','l1284jfb9u9'),
 ('Prepare','Triggers at the start of a round.','n1284srjdfi'),
 ('Sacrifice','Triggers when the hero dies.','b1284q4g43n'),
 ('Combine','Play a card matching a deployed hero to combine it with that hero and strengthen them.','b1284t3mk6x'),
 ('Flash','At combat start, the hero jumps to the mirrored position on the enemy battlefield.','i1284gzvf2q'),
 ('Seize','When this card is played, take levels from one random allied hero within 1 tile: up to 10 levels, excluding Temporary Levels.','f1284thzx39'),
 ('Temporary Levels','These levels are removed at the end of combat.','d1284syb2br'),
 ('Fleeting','Automatically destroyed at the end of the round. Selling it gives no Energy.','c1284acq47n'),
 ('Revive','The hero returns after dying with 50% Health. Each hero can revive at most 10 times per round.','x1284nuts79'),
 ('Triumph','Triggers if you win a battle while this hero is deployed.','c12846eud2v'),
 ('Defeat','Triggers if you lose a battle while this hero is deployed.','y1284jf7njl'),
 ('Exit','Triggers when this deployed hero is sold.','j1284qykxo5')
]

VIDEOS = [
 (5,'Bai Ge · Three Kingdoms Loop','A powerful full-team level 999 lineup','Xijun','u1285fwc3t3'),
 (7,'Xiangxiang · Totem Opening Barrage','Dominate once your lineup is complete','Hajimide','r1285hzfmdv'),
 (10,"Chang Xiao'e · Sea, Land & Air",'An easy build for new players','Master Shark','d1286zqeaup'),
 (2,'Naonao · Sunset Sea Prepare','A smooth beginner pick for climbing ranks','Winter Melon Soup','w1285mnvwq8'),
 (1,'Yaria · Li Xin Sacrifice','Learn the build and climb steadily','Lao Pili','x1285t5msir'),
 (6,'Marco · Hypercarry','Simple, fun, and bursts down fragile foes','European Fish','s12859tprze'),
 (4,'Director Jiang · Xuance Carry','Easy to learn, ready to win','Yan Xiaoxiu','g1286io0xgc'),
 (11,'Qiao Xi · Sikong Zhen','A powerful, easy-to-play hidden strategy','Yan Xiaoxiu','o1285xdiyfb'),
 (3,'Little Daji · Conquest Tactics','A satisfying must-learn beginner build','An Cang Xuan G','l1285jh2lbj'),
 (8,'Zhuang Xiaoyu · Ancient Coin Mulan','Endless revives sweep the battlefield','Master Shark','p1285dxymau'),
 (12,'Mr. Ming · Pool Party','Fill the battlefield with summons','Liuyun','o1285znw720'),
 (9,'Yuhuan · Sunset Sea Loop','A high-ceiling build for beginners','Hansang','j128758vqd7')
]
