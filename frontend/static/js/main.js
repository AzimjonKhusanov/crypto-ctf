// NullCTF — Asosiy JavaScript

// ── Nav toggle ──────────────────────────────────────────────
document.getElementById('navToggle')?.addEventListener('click', () => {
  document.querySelector('.nav-links')?.classList.toggle('open');
});

// ── Flash xabarlarni avtomatik yopish ──────────────────────
setTimeout(() => {
  document.querySelectorAll('.flash').forEach(el => {
    el.style.transition = 'opacity .4s, transform .4s';
    el.style.opacity = '0';
    el.style.transform = 'translateX(110%)';
    setTimeout(() => el.remove(), 400);
  });
}, 4000);

// ── Flag inputda NULL{ prefixi ──────────────────────────────
document.querySelectorAll('.flag-input').forEach(input => {
  input.addEventListener('input', () => {
    // NULL{ prefiksini olib tashlashdan himoya
    if (input.value.startsWith('NULL{')) {
      input.value = input.value.slice(5);
    }
  });
});

// ── Kod bloklariga "Nusxa olish" tugmasi ───────────────────
document.querySelectorAll('pre code').forEach(block => {
  const pre = block.parentElement;
  const btn = document.createElement('button');
  btn.className = 'copy-btn';
  btn.textContent = 'Nusxa';
  btn.style.cssText = `
    position:absolute; top:.5rem; right:.5rem;
    background:rgba(0,255,136,.15); color:#00ff88;
    border:1px solid rgba(0,255,136,.3); border-radius:4px;
    padding:.2rem .6rem; font-size:.72rem; cursor:pointer;
    font-family:'Share Tech Mono',monospace;
  `;
  pre.style.position = 'relative';
  pre.appendChild(btn);
  btn.addEventListener('click', () => {
    navigator.clipboard.writeText(block.textContent).then(() => {
      btn.textContent = 'Nusxalandi!';
      btn.style.color = '#fff';
      setTimeout(() => { btn.textContent = 'Nusxa'; btn.style.color = '#00ff88'; }, 1500);
    });
  });
});

// ── Challenge filterlash ────────────────────────────────────
const filterBtns = document.querySelectorAll('.filter-btn');
filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const group = btn.dataset.group;
    const value = btn.dataset.value;

    // Bir guruh ichida active ni almashtir
    document.querySelectorAll(`.filter-btn[data-group="${group}"]`).forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    filterChallenges();
  });
});

function filterChallenges() {
  const activeCategory  = document.querySelector('.filter-btn[data-group="category"].active')?.dataset.value || 'all';
  const activeDifficulty = document.querySelector('.filter-btn[data-group="difficulty"].active')?.dataset.value || 'all';

  document.querySelectorAll('.challenge-card').forEach(card => {
    const cat  = card.dataset.category || '';
    const diff = card.dataset.difficulty || '';
    const showCat  = activeCategory  === 'all' || cat  === activeCategory;
    const showDiff = activeDifficulty === 'all' || diff === activeDifficulty;
    card.style.display = (showCat && showDiff) ? '' : 'none';
  });

  // Natijaviy son
  const visible = document.querySelectorAll('.challenge-card:not([style*="none"])').length;
  const counter = document.getElementById('challengeCount');
  if (counter) counter.textContent = visible;
}

// ── Animatsiyali kirish ─────────────────────────────────────
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.animate-in').forEach(el => {
  observer.observe(el);
});

// CSS animatsiya
const style = document.createElement('style');
style.textContent = `
  .animate-in {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity .5s ease, transform .5s ease;
  }
  .animate-in.visible {
    opacity: 1;
    transform: translateY(0);
  }
`;
document.head.appendChild(style);

// ── Scoreboard counter animatsiyasi ────────────────────────
function animateCounter(el) {
  const target = parseInt(el.textContent.replace(/\D/g, ''));
  let current = 0;
  const step = target / 40;
  const timer = setInterval(() => {
    current += step;
    if (current >= target) {
      current = target;
      clearInterval(timer);
    }
    el.textContent = Math.floor(current);
  }, 25);
}

document.querySelectorAll('.stat-num').forEach(el => {
  const obs = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) {
      animateCounter(el);
      obs.disconnect();
    }
  });
  obs.observe(el);
});

// ── Admin: confirm o'chirish ────────────────────────────────
document.querySelectorAll('[data-confirm]').forEach(btn => {
  btn.addEventListener('click', e => {
    if (!confirm(btn.dataset.confirm)) e.preventDefault();
  });
});
