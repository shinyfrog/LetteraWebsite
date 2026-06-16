/* Lettera landing page — interactions */
(function () {
  "use strict";

  /* ---------- FAQ: keep only one open at a time ---------- */
  const faqItems = document.querySelectorAll(".faq-item");
  faqItems.forEach((item) => {
    item.addEventListener("toggle", () => {
      if (item.open) {
        faqItems.forEach((other) => {
          if (other !== item) other.open = false;
        });
      }
    });
  });

  /* ---------- Reveal on scroll ---------- 
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -10% 0px", threshold: 0.08 }
    );
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("in"));
  }

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
