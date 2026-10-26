/* Optional, dependency-free export controls. Data stays in the document. */
window.htmlAuthoring = {
  downloadJSON(value, filename = 'decision.json') {
    const text = JSON.stringify(value, null, 2) + '\n';
    const url = URL.createObjectURL(new Blob([text], { type: 'application/json' }));
    const link = document.createElement('a');
    link.href = url; link.download = filename;
    document.body.append(link); link.click(); link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  },
  async copy(text, fallback) {
    try { await navigator.clipboard.writeText(text); return true; }
    catch {
      fallback.hidden = false;
      fallback.value = text;
      fallback.focus(); fallback.select();
      return false;
    }
  }
};
