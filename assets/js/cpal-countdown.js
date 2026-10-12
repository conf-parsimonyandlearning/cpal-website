(function () {
  'use strict';

  function pad(value) {
    return String(value).padStart(2, '0');
  }

  function formatRemaining(milliseconds) {
    var totalSeconds = Math.max(0, Math.floor(milliseconds / 1000));
    var days = Math.floor(totalSeconds / 86400);
    var hours = Math.floor((totalSeconds % 86400) / 3600);
    var minutes = Math.floor((totalSeconds % 3600) / 60);
    var seconds = totalSeconds % 60;
    return days + ' days ' + pad(hours) + ':' + pad(minutes) + ':' + pad(seconds);
  }

  function updateCountdown(element) {
    var target = Date.parse(element.getAttribute('data-countdown'));
    if (!Number.isFinite(target)) {
      element.textContent = '—';
      return;
    }

    var remaining = target - Date.now();
    if (remaining <= 0) {
      element.textContent = 'Passed';
      element.classList.add('cpal-countdown-passed');
      return;
    }

    element.textContent = formatRemaining(remaining);
  }

  function updateAll() {
    document.querySelectorAll('[data-countdown]').forEach(updateCountdown);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      updateAll();
      window.setInterval(updateAll, 1000);
    });
  } else {
    updateAll();
    window.setInterval(updateAll, 1000);
  }
})();
