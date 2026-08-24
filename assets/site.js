(() => {
  const menu = document.querySelector('.menu-button');
  const links = document.querySelector('#nav-links');
  if (menu && links) menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') === 'true';
    menu.setAttribute('aria-expanded', String(!open)); links.classList.toggle('open', !open);
  });
  const fields = ['volume', 'minutes', 'reduction', 'cost'].map(id => document.getElementById(id));
  const hours = document.getElementById('hours'); const value = document.getElementById('value');
  const aud = new Intl.NumberFormat('en-AU', {style:'currency', currency:'AUD', maximumFractionDigits:0});
  function calculate(){
    let [volume, minutes, reduction, cost] = fields.map(f => Number(f.value));
    volume = Math.min(100000, Math.max(0, volume || 0)); minutes = Math.min(1440, Math.max(0, minutes || 0));
    reduction = Math.min(95, Math.max(0, reduction || 0)); cost = Math.min(1000, Math.max(0, cost || 0));
    const monthlyHours = volume * minutes / 60 * reduction / 100;
    hours.textContent = `${monthlyHours.toLocaleString('en-AU',{maximumFractionDigits:1})} hours`;
    value.textContent = aud.format(monthlyHours * cost * 12);
  }
  fields.forEach(f => f.addEventListener('input', calculate)); calculate();
  const form = document.getElementById('assessment-form'); const error = document.getElementById('form-error');
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!form.checkValidity()) { error.hidden = false; form.querySelector(':invalid').focus(); return; }
    error.hidden = true;
    const get = name => form.elements[name].value.trim();
    const subject = 'Workflow assessment enquiry — ' + get('business');
    const body = [
      'Workflow assessment enquiry', '',
      'Business type: ' + get('business'),
      'Current bottleneck: ' + get('bottleneck'),
      'Approx. monthly volume: ' + get('monthly'),
      'Current delay / time: ' + get('delay'),
      'Tools involved: ' + get('tools'),
      'Desired outcome: ' + get('outcome'),
      'Sensitivity category: ' + form.elements.sensitivity.value, '',
      'I have not included passwords, API keys, full client records or sensitive documents.'
    ].join('\n');
    window.location.href = 'mailto:enzo491kw@gmail.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  });
})();
