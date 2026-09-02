(function () {
  'use strict';

  var PRICE = 100;
  var input = document.getElementById('metrekare');
  if (input) {
    var total = document.getElementById('toplam-fiyat');
    var waLink = document.getElementById('wa-teklif');

    function format(n) {
      return n.toLocaleString('tr-TR') + ' TL';
    }

    function update() {
      var m2 = parseFloat(input.value);
      if (!m2 || m2 < 1) {
        if (total) total.textContent = '—';
        if (waLink) {
          waLink.href = 'https://wa.me/905356292706?text=' + encodeURIComponent('Merhaba, boya badana hizmeti için fiyat teklifi almak istiyorum.');
        }
        return;
      }
      var price = Math.round(m2 * PRICE);
      if (total) total.textContent = format(price);
      if (waLink) {
        waLink.href = 'https://wa.me/905356292706?text=' + encodeURIComponent(
          'Merhaba, ' + m2 + ' m² boya işi için tahmini ' + format(price) + ' hesapladım. Kesin fiyat teklifi alabilir miyim?'
        );
      }
    }

    input.addEventListener('input', update);
  }

  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!prefersReduced) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          observer.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    document.querySelectorAll('.section-fade').forEach(function (el) { observer.observe(el); });
  } else {
    document.querySelectorAll('.section-fade').forEach(function (el) { el.classList.add('visible'); });
  }

  var sections = ['hizmetler', 'hesapla', 'hakkimda', 'neden-biz', 'surec', 'sss', 'iletisim'];
  var navLinks = document.querySelectorAll('.nav-link[data-section]');
  var header = document.getElementById('header');
  if (navLinks.length && header) {
    function onScroll() {
      var scrollY = window.scrollY + 120;
      var current = '';
      sections.forEach(function (id) {
        var el = document.getElementById(id);
        if (el && el.offsetTop <= scrollY) current = id;
      });
      navLinks.forEach(function (link) {
        link.classList.toggle('active', link.dataset.section === current);
      });
      header.classList.toggle('scrolled', window.scrollY > 20);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  } else {
    document.querySelectorAll('.section-fade').forEach(function (el) { el.classList.add('visible'); });
    if (header) {
      window.addEventListener('scroll', function () {
        header.classList.toggle('scrolled', window.scrollY > 20);
      }, { passive: true });
    }
  }

  document.querySelectorAll('header details a[href]').forEach(function (link) {
    link.addEventListener('click', function () {
      var d = link.closest('details');
      if (d) d.removeAttribute('open');
    });
  });
})();
