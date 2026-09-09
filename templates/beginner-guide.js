document.querySelectorAll('[data-tabs]').forEach(group => {
  const tabs = [...group.querySelectorAll(':scope > [role="tab"]')];
  function select(tab) {
    for (const item of tabs) {
      const selected = item === tab;
      item.setAttribute('aria-selected', String(selected));
      item.tabIndex = selected ? 0 : -1;
      document.getElementById(item.getAttribute('aria-controls')).hidden = !selected;
    }
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => select(tab));
    tab.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next !== undefined) { event.preventDefault(); select(tabs[next]); tabs[next].focus(); }
    });
  });
});
document.querySelectorAll('[data-carousel]').forEach(carousel => {
  const slides = [...carousel.querySelectorAll('.slide')];
  let current = 0;
  carousel.querySelectorAll('[data-direction]').forEach(button => button.addEventListener('click', () => {
    current = (current + Number(button.dataset.direction) + slides.length) % slides.length;
    slides.forEach((slide, index) => slide.hidden = index !== current);
    carousel.querySelector('[data-counter]').textContent = `${current + 1} / ${slides.length}`;
  }));
});
const imageDialog = document.getElementById('image-dialog');
const videoDialog = document.getElementById('video-dialog');
let player;
let playerScript;
function loadPlayer() {
  if (!playerScript) {
    playerScript = new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = 'https://vm.gtimg.cn/thumbplayer/superplayer/superplayer.js';
      script.onload = resolve;
      script.onerror = () => { script.remove(); playerScript = undefined; reject(new Error('Player unavailable')); };
      document.head.append(script);
    });
  }
  return playerScript;
}
document.querySelectorAll('[data-video]').forEach(link => link.addEventListener('click', async event => {
  event.preventDefault();
  videoDialog.showModal();
  const status = videoDialog.querySelector('.video-status');
  status.textContent = 'Loading original video…';
  try {
    await loadPlayer();
    if (!videoDialog.open) return;
    player ||= new SuperPlayer({container: '#video-player'});
    player.play({vid: link.dataset.video});
    status.textContent = '';
  } catch {
    status.textContent = 'The original player could not load. Use the official guide link below.';
  }
}));
videoDialog.querySelector('button').addEventListener('click', () => videoDialog.close());
videoDialog.addEventListener('close', () => player?.stop());
document.querySelectorAll('.zoom').forEach(button => button.addEventListener('click', () => {
  const source = button.querySelector('img');
  imageDialog.querySelector('img').src = source.src;
  imageDialog.querySelector('img').alt = source.alt;
  imageDialog.querySelector('a').href = source.src;
  imageDialog.showModal();
}));
imageDialog.querySelector('button').addEventListener('click', () => imageDialog.close());
imageDialog.addEventListener('click', event => { if (event.target === imageDialog) imageDialog.close(); });
document.querySelectorAll('[data-code]').forEach(button => button.addEventListener('click', async () => {
  const status = button.parentElement.querySelector('.status');
  try {
    await navigator.clipboard.writeText(button.dataset.code);
    status.textContent = 'Copied. In the game, open Lineups → Saved Lineups → Import Lineup.';
  } catch {
    status.textContent = `Clipboard unavailable. Copy this official lineup code manually: ${button.dataset.code}`;
  }
}));
document.getElementById('keyword-search').addEventListener('input', event => {
  const query = event.target.value.toLowerCase().trim();
  let count = 0;
  document.querySelectorAll('.keyword').forEach(card => {
    card.hidden = !card.textContent.toLowerCase().includes(query);
    if (!card.hidden) count++;
  });
  document.getElementById('keyword-status').textContent = `${count} keyword${count === 1 ? '' : 's'} shown`;
});
