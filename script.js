/* Lettera landing page — interactions */
(function () {
  "use strict";

  /* ---------- Newsletter form (front-end only) ---------- */
  const form = document.getElementById("signupForm");
  const msg = document.getElementById("signupMsg");
  const input = document.getElementById("email");
  if (!form || !msg || !input) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const value = input.value.trim();
    const valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    if (!valid) {
      msg.classList.add("is-error");
      msg.textContent = "Please enter a valid email address.";
      input.focus();
      return;
    }
    msg.classList.remove("is-error");
    msg.textContent = "Thanks! You're on the list — we'll be in touch.";
    form.reset();
  });
})();
