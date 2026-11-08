(() => {
  const menu = document.querySelector('.menu-toggle');
  const nav = document.getElementById('primary-nav');
  menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
  });
  nav.addEventListener('click', (event) => {
    if (event.target.closest('a')) {
      menu.setAttribute('aria-expanded', 'false');
      nav.classList.remove('is-open');
    }
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
      menu.setAttribute('aria-expanded', 'false');
      nav.classList.remove('is-open');
      menu.focus();
    }
  });
  const input = document.getElementById('project-search');
  const buttons = [...document.querySelectorAll('.filter')];
  const rows = [...document.querySelectorAll('.project-row')];
  const status = document.getElementById('results-status');
  const clear = document.getElementById('clear-search');
  let category = 'All';
  const filter = () => {
    const query = input.value.trim().toLowerCase();
    let count = 0;
    rows.forEach((row) => {
      const show = (category === 'All' || row.dataset.category === category) && row.dataset.search.includes(query);
      row.hidden = !show;
      if (show) count += 1;
    });
    buttons.forEach((button) => {
      const active = button.dataset.category === category;
      button.classList.toggle('active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    status.textContent = `Showing ${count} of ${rows.length} collection entries`;
    document.getElementById('empty-state').hidden = count !== 0;
    clear.hidden = !query && category === 'All';
  };
  input.addEventListener('input', filter);
  buttons.forEach((button) => button.addEventListener('click', () => { category = button.dataset.category; filter(); }));
  clear.addEventListener('click', () => { input.value = ''; category = 'All'; filter(); input.focus(); });
  filter();
})();
