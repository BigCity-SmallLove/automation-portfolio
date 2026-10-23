"use strict";
(() => {
  const contact = window.PORTFOLIO_CONTACT || {};
  const httpsUrl = value => {
    try { const url = new URL(value); return url.protocol === "https:" && !url.username && !url.password ? url.href : null; }
    catch { return null; }
  };
  const github = httpsUrl(contact.github);
  if (github && new URL(github).hostname === "github.com") {
    document.querySelectorAll("[data-contact-github]").forEach(link => { link.href = github; });
  }
  if (typeof contact.email === "string" && /^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/.test(contact.email)) {
    const link = document.querySelector("[data-contact-email]");
    link.href = `mailto:${contact.email}`; link.textContent = contact.email; link.hidden = false;
  }
  if (Array.isArray(contact.additionalLinks)) {
    const list = document.querySelector("[data-contact-extra]");
    contact.additionalLinks.forEach(item => {
      const url = httpsUrl(item.url);
      if (!url || typeof item.label !== "string" || !item.label.trim()) return;
      const link = document.createElement("a"); link.href = url; link.textContent = item.label;
      link.className = "optional-contact"; list.append(link);
    });
  }
  const portfolio = httpsUrl(contact.portfolioUrl);
  if (portfolio) document.querySelectorAll("[data-published-portfolio]").forEach(link => { link.href = portfolio; link.hidden = false; });
})();
