---

marp: true
math: katex
paginate: true
theme: product-docs
footer: "[23f2002999@ds.study.iitm.ac.in](mailto:23f2002999@ds.study.iitm.ac.in)"
---------------------------------------------------------------------------------

<!--
_class: lead
-->

<style>
/* @theme product-docs */
section {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, Ubuntu, Cantarell, "Noto Sans", "Helvetica Neue", Arial, "Apple Color Emoji","Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  background: #ffffff;
  color: #111827;
  padding: 64px;
}

h1, h2, h3 { line-height: 1.15; }

/* Page numbers */
section::after {
  content: attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
  position: absolute;
  right: 28px;
  bottom: 20px;
  font-size: 0.8rem;
  opacity: 0.6;
}

footer { font-size: 12px; color: #6b7280; }

/* Accent */
:root { --brand: #2563eb; }
h1 { color: var(--brand); }
a { color: var(--brand); }

/* Lead slide tweak */
.lead h1 { font-size: 2.8rem; }
</style>

---

# Product Documentation

**Maintainable Marp-based slides in version control**

📧 [23f2002999@ds.study.iitm.ac.in](mailto:23f2002999@ds.study.iitm.ac.in)

---

<!-- _class: lead -->

# Why Marp?

* Plain **Markdown** ⇒ perfect for Git
* Converts to **HTML / PDF / PPTX** (via Marp CLI)
* **Custom themes** with CSS (embedded or external)
* Slide-level **directives** for per-slide styling

---

# Custom Styling via Directives

This deck uses:

* Front‑matter directives: `marp`, `theme`, `paginate`, `math`, `footer`
* Slide directive: `<!-- _class: lead -->`
* Theme block with `/* @theme product-docs */` inside `<style>`
* CSS to render **page numbers** (`section::after`)

---

# Background Image (with overlay text)

![bg](https://images.unsplash.com/photo-1518779578993-ec3579fee39f?q=80\&w=1920)

<!-- _color: #ffffff -->

## Telemetry Pipeline (Example)

* Collect → Validate → Ingest → Store
* Visualize in Grafana / build alerts

---

# Algorithmic Complexity (Math)

With KaTeX enabled via `math: katex`:

* Sorting complexity: \$T(n) = O(n \log n)\$
* Hash operations (avg.): \$O(1)\$

Block formula for amortized resize in dynamic arrays:

$$
T(n) = \frac{1}{n}\sum_{i=1}^{n} c_i = O(1)
$$

Average Precision in IR:

$$
\mathrm{AP} = \frac{1}{N}\sum_{k=1}^{N} \mathrm{precision}(k)\,\cdot\,\mathrm{rel}(k)
$$

---

# Conversion

```bash
# PDF
npx @marp-team/marp-cli@latest slides.md --html --allow-local-files -o slides.pdf

# PPTX
npx @marp-team/marp-cli@latest slides.md --html --allow-local-files -o slides.pptx
```

---

# Summary

* ✅ Version-controlled Markdown
* ✅ Custom theme + page numbers
* ✅ Background image slide
* ✅ Slide-level directives
* ✅ Math (KaTeX)

---

# Thank You

Questions? 📧 [23f2002999@ds.study.iitm.ac.in](mailto:23f2002999@ds.study.iitm.ac.in)
