/* Lettera landing page — interactions */
(function () {
  "use strict";

  /* ---------- Newsletter form (front-end only) ---------- */
  const form = document.getElementById("signupForm");
  const msg = document.getElementById("signupMsg");
  const input = document.getElementById("email");

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const value = input.value.trim();
    const valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    if (!valid) {
      msg.style.color = "#d9382f";
      msg.textContent = "Please enter a valid email address.";
      input.focus();
      return;
    }
    msg.style.color = "";
    msg.textContent = "Thanks! You're on the list — we'll be in touch.";
    form.reset();
  });
})();
