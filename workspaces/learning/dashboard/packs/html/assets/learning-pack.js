(function () {
  const root = document.documentElement;
  const storedTheme = localStorage.getItem("learning-pack-theme");
  if (storedTheme) {
    root.dataset.theme = storedTheme;
  }

  const themeButton = document.querySelector("[data-theme-toggle]");
  if (themeButton) {
    themeButton.addEventListener("click", () => {
      const current = root.dataset.theme || "";
      const next = current === "dark" ? "light" : "dark";
      root.dataset.theme = next;
      localStorage.setItem("learning-pack-theme", next);
    });
  }

  const progressBoxes = document.querySelectorAll("[data-progress-key]");
  progressBoxes.forEach((box) => {
    const key = "learning-pack-progress:" + box.dataset.progressKey;
    box.checked = localStorage.getItem(key) === "1";
    box.addEventListener("change", () => {
      if (box.checked) {
        localStorage.setItem(key, "1");
      } else {
        localStorage.removeItem(key);
      }
    });
  });

  const sourceTrace = document.querySelector(".section-source-trace");
  if (sourceTrace) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "source-trace-toggle";
    button.textContent = "Toggle Source Trace";
    button.setAttribute("aria-expanded", "true");
    const heading = sourceTrace.querySelector("h1");
    if (heading) {
      heading.insertAdjacentElement("afterend", button);
      button.addEventListener("click", () => {
        const collapsed = sourceTrace.classList.toggle("is-collapsed");
        button.setAttribute("aria-expanded", String(!collapsed));
      });
    }
  }

  const tocLinks = Array.from(document.querySelectorAll(".toc-link"));
  const headings = tocLinks
    .map((link) => document.getElementById(link.getAttribute("href").slice(1)))
    .filter(Boolean);

  if ("IntersectionObserver" in window && headings.length) {
    const activeById = new Map();
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => activeById.set(entry.target.id, entry.isIntersecting));
        const active = headings.find((heading) => activeById.get(heading.id));
        if (!active) return;
        tocLinks.forEach((link) => {
          link.classList.toggle("is-active", link.getAttribute("href") === "#" + active.id);
        });
      },
      { rootMargin: "-10% 0px -75% 0px", threshold: 0.01 }
    );
    headings.forEach((heading) => observer.observe(heading));
  }
})();
