// The only JavaScript on the site: three small jobs.


// 1. Filter buttons.
//    Clicking a button shows only the items whose data-tags include its name.
//    Works for the project cards (home + /works) and the skills (About me).
document.querySelectorAll("[data-filter-group]").forEach(function (buttonRow) {
  var buttons = buttonRow.querySelectorAll("button");
  var items = buttonRow.parentElement.querySelectorAll("[data-tags]");

  buttons.forEach(function (button) {
    button.addEventListener("click", function () {
      var chosen = button.dataset.filter;

      buttons.forEach(function (b) { b.classList.remove("is-active"); });
      button.classList.add("is-active");

      items.forEach(function (item) {
        var tags = item.dataset.tags.split("|");
        var show = chosen === "all" || tags.includes(chosen);
        item.classList.toggle("is-hidden", !show);
      });
    });
  });
});


// 2. Fade things in as they scroll into view (anything with class="reveal").
var revealWatcher = new IntersectionObserver(function (entries) {
  entries.forEach(function (entry) {
    if (entry.isIntersecting) {
      entry.target.classList.add("is-visible");
      revealWatcher.unobserve(entry.target);
    }
  });
}, { threshold: 0.15 });

document.querySelectorAll(".reveal").forEach(function (element) {
  revealWatcher.observe(element);
});


// 3. Count the About page numbers up from 0 (500+, 15+, 94%).
document.querySelectorAll("[data-count]").forEach(function (number) {
  var target = Number(number.dataset.count);
  var startTime = null;

  function step(time) {
    if (startTime === null) startTime = time;
    var progress = Math.min((time - startTime) / 1500, 1);
    var eased = 1 - Math.pow(1 - progress, 3);   // starts fast, slows down at the end
    number.textContent = Math.round(target * eased);
    if (progress < 1) requestAnimationFrame(step);
  }

  requestAnimationFrame(step);
});
