import re

HEAD_LANG_SCRIPT = '''<script>
  // Apply a stored language choice before first paint, so the correct
  // font stack is active immediately (avoids a flash of the wrong font).
  (function () {
    try {
      var l = localStorage.getItem('site-lang');
      if (l === 'ru') document.documentElement.setAttribute('lang', 'ru');
    } catch (e) {}
  })();
</script>'''

SIDEBAR = '''  <header class="sidebar">
    <div class="topbar">
      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>

    <div class="sidebar-top">
      <a href="index.html" class="site-name">[PLACEHOLDER NAME]</a>
      <nav class="primary-nav">
        <a href="experience.html" class="nav-link" data-en="Experience" data-ru="\u041e\u043f\u044b\u0442">
          <span class="mark"></span>
          <span class="nav-label-primary"></span>
          <span class="nav-reveal"><span class="nav-sep">/</span><span class="nav-label-secondary"></span></span>
        </a>
        <a href="projects.html" class="nav-link" data-en="Projects" data-ru="\u041f\u0440\u043e\u0435\u043a\u0442\u044b">
          <span class="mark"></span>
          <span class="nav-label-primary"></span>
          <span class="nav-reveal"><span class="nav-sep">/</span><span class="nav-label-secondary"></span></span>
        </a>
        <a href="resume.html" class="nav-link" data-en="Resume" data-ru="\u0420\u0435\u0437\u044e\u043c\u0435">
          <span class="mark"></span>
          <span class="nav-label-primary"></span>
          <span class="nav-reveal"><span class="nav-sep">/</span><span class="nav-label-secondary"></span></span>
        </a>
        <a href="contact.html" class="nav-link" data-en="Contact" data-ru="\u0421\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f">
          <span class="mark"></span>
          <span class="nav-label-primary"></span>
          <span class="nav-reveal"><span class="nav-sep">/</span><span class="nav-label-secondary"></span></span>
        </a>
      </nav>

      <div class="lang-toggle" role="group" aria-label="Language / \u042f\u0437\u044b\u043a">
        <button type="button" data-lang="en" aria-pressed="true">EN</button>
        <span class="lang-toggle-sep">/</span>
        <button type="button" data-lang="ru" aria-pressed="false">RU</button>
      </div>
    </div>

    <div class="sidebar-footer">
      <span data-en="Based in London, UK" data-ru="\u0416\u0438\u0432\u0451\u0442 \u0432 \u041b\u043e\u043d\u0434\u043e\u043d\u0435, \u0412\u0435\u043b\u0438\u043a\u043e\u0431\u0440\u0438\u0442\u0430\u043d\u0438\u044f">Based in London, UK</span>
      <div class="footer-links">
        <a href="contact.html">[PLACEHOLDER@EMAIL.COM]</a>
        <a href="#" data-en="LinkedIn \u2014 [PLACEHOLDER]" data-ru="LinkedIn \u2014 [\u0421\u0421\u042b\u041b\u041a\u0410]">LinkedIn \u2014 [PLACEHOLDER]</a>
      </div>
    </div>
  </header>'''

def page(title_en, title_ru, body_title_en, body_title_ru, main_html, extra_head=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{HEAD_LANG_SCRIPT}
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_en}</title>
{extra_head}<link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">
<link rel="stylesheet" href="css/style.css">
</head>
<body data-title-en="{title_en}" data-title-ru="{title_ru}">

<div class="shell">

{SIDEBAR}

  <main>
{main_html}
  </main>

</div>

<script src="js/main.js"></script>
</body>
</html>
'''

# ---------------------------------------------------------------
# INDEX
# ---------------------------------------------------------------
index_main = '''    <section class="hero">
      <p class="hero-eyebrow">
        <span class="mark"></span>
        <span class="eyebrow-text">
          <span class="lang-en">Art Historian \u2014 Soviet Avant-Garde, 1913\u20131934</span>
          <span class="lang-ru" lang="ru">\u0418\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u043e\u0432\u0435\u0434 \u2014 \u0441\u043e\u0432\u0435\u0442\u0441\u043a\u0438\u0439 \u0430\u0432\u0430\u043d\u0433\u0430\u0440\u0434, 1913\u20131934</span>
        </span>
      </p>

      <p class="hero-statement">
        <span class="line" data-en="This research is about construction." data-ru="\u042d\u0442\u043e \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0435 \u2014 \u043e \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438.">This research is about construction.</span>
        <span class="line" data-en="This research is about the collective over the individual." data-ru="\u042d\u0442\u043e \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0435 \u2014 \u043e \u043a\u043e\u043b\u043b\u0435\u043a\u0442\u0438\u0432\u043d\u043e\u043c \u043d\u0430\u0447\u0430\u043b\u0435, \u0430 \u043d\u0435 \u0438\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u043e\u043c.">This research is about the collective over the individual.</span>
        <span class="line accent" data-en="This research is about utopia, built and unbuilt." data-ru="\u042d\u0442\u043e \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0435 \u2014 \u043e\u0431 \u0443\u0442\u043e\u043f\u0438\u0438, \u0432\u043e\u043f\u043b\u043e\u0449\u0451\u043d\u043d\u043e\u0439 \u0438 \u043d\u0435\u0442.">This research is about utopia, built and unbuilt.</span>
        <span class="line" data-en="This research is about the printed page as a weapon." data-ru="\u042d\u0442\u043e \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0435 \u2014 \u043e \u043f\u0435\u0447\u0430\u0442\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 \u043a\u0430\u043a \u043e\u0440\u0443\u0436\u0438\u0438.">This research is about the printed page as a weapon.</span>
        <span class="line" data-en="This research is about the line, after Rodchenko." data-ru="\u042d\u0442\u043e \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0435 \u2014 \u043e \u043b\u0438\u043d\u0438\u0438, \u0432\u0441\u043b\u0435\u0434 \u0437\u0430 \u0420\u043e\u0434\u0447\u0435\u043d\u043a\u043e.">This research is about the line, after Rodchenko.</span>
        <span class="line" data-en="This research is about the museum as an archive of belief." data-ru="\u042d\u0442\u043e \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0435 \u2014 \u043e \u043c\u0443\u0437\u0435\u0435 \u043a\u0430\u043a \u0430\u0440\u0445\u0438\u0432\u0435 \u0432\u0435\u0440\u044b.">This research is about the museum as an archive of belief.</span>
        <span class="line" data-en="This research is about looking again." data-ru="\u042d\u0442\u043e \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0435 \u2014 \u043e \u0442\u043e\u043c, \u0447\u0442\u043e\u0431\u044b \u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0441\u043d\u043e\u0432\u0430.">This research is about looking again.</span>
      </p>

      <div class="hero-meta">
        <div class="hero-meta-item">
          <strong data-en="Focus" data-ru="\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435">Focus</strong>
          <span data-en="Constructivism, Suprematism, and Productivism \u2014 from the 1915 \u201c0.10\u201d exhibition to the Socialist Realist turn of the 1930s." data-ru="\u041a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u0438\u0432\u0438\u0437\u043c, \u0441\u0443\u043f\u0440\u0435\u043c\u0430\u0442\u0438\u0437\u043c \u0438 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0438\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u043e \u2014 \u043e\u0442 \u0432\u044b\u0441\u0442\u0430\u0432\u043a\u0438 \u00ab0,10\u00bb 1915 \u0433\u043e\u0434\u0430 \u0434\u043e \u043f\u043e\u0432\u043e\u0440\u043e\u0442\u0430 \u043a \u0441\u043e\u0446\u0440\u0435\u0430\u043b\u0438\u0437\u043c\u0443 \u0432 1930-\u0445.">Constructivism, Suprematism, and Productivism \u2014 from the 1915 \u201c0.10\u201d exhibition to the Socialist Realist turn of the 1930s.</span>
        </div>
        <div class="hero-meta-item">
          <strong data-en="Background" data-ru="\u041e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435">Background</strong>
          <span data-en="BA Film Studies, [PLACEHOLDER UNIVERSITY] \u00b7 MA Art History, [PLACEHOLDER UNIVERSITY]" data-ru="\u0411\u0430\u043a\u0430\u043b\u0430\u0432\u0440\u0438\u0430\u0442 \u043f\u043e \u043a\u0438\u043d\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044e, [\u041c\u0415\u0421\u0422\u041e \u0414\u041b\u042f \u0423\u041d\u0418\u0412\u0415\u0420\u0421\u0418\u0422\u0415\u0422\u0410] \u00b7 \u041c\u0430\u0433\u0438\u0441\u0442\u0440\u0430\u0442\u0443\u0440\u0430 \u043f\u043e \u0438\u0441\u0442\u043e\u0440\u0438\u0438 \u0438\u0441\u043a\u0443\u0441\u0441\u0442\u0432, [\u041c\u0415\u0421\u0422\u041e \u0414\u041b\u042f \u0423\u041d\u0418\u0412\u0415\u0420\u0421\u0418\u0422\u0415\u0422\u0410]">BA Film Studies, [PLACEHOLDER UNIVERSITY] \u00b7 MA Art History, [PLACEHOLDER UNIVERSITY]</span>
        </div>
        <div class="hero-meta-item">
          <strong data-en="Interested in" data-ru="\u0418\u043d\u0442\u0435\u0440\u0435\u0441\u0443\u0435\u0442">Interested in</strong>
          <span data-en="Curatorial practice, art education, and provenance / sourcing work with London institutions." data-ru="\u041a\u0443\u0440\u0430\u0442\u043e\u0440\u0441\u043a\u0430\u044f \u043f\u0440\u0430\u043a\u0442\u0438\u043a\u0430, \u0430\u0440\u0442-\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0438 \u0440\u0430\u0431\u043e\u0442\u0430 \u0441 \u043f\u0440\u043e\u0432\u0435\u043d\u0430\u043d\u0441\u043e\u043c / \u043f\u043e\u0438\u0441\u043a\u043e\u043c \u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0439 \u0434\u043b\u044f \u043b\u043e\u043d\u0434\u043e\u043d\u0441\u043a\u0438\u0445 \u0438\u043d\u0441\u0442\u0438\u0442\u0443\u0446\u0438\u0439.">Curatorial practice, art education, and provenance / sourcing work with London institutions.</span>
        </div>
      </div>
    </section>'''

open('site/index.html', 'w', encoding='utf-8').write(
    page("[PLACEHOLDER \u2014 YOUR NAME]", "[PLACEHOLDER \u2014 \u0412\u0410\u0428\u0415 \u0418\u041c\u042f]",
         None, None, index_main,
         extra_head='<meta name="description" content="Art historian specialising in Soviet Avant-Garde art. Portfolio, experience, and research.">\n')
)

# ---------------------------------------------------------------
# EXPERIENCE
# ---------------------------------------------------------------
def experience_item(when_en, when_ru, role_en, role_ru, org_en, org_ru, desc_en, desc_ru):
    return f'''      <article class="experience-item">
        <div class="experience-when">
          <span class="mark"></span><span data-en="{when_en}" data-ru="{when_ru}">{when_en}</span>
        </div>
        <div class="experience-body">
          <h3 data-en="{role_en}" data-ru="{role_ru}">{role_en}</h3>
          <p class="experience-role" data-en="{org_en}" data-ru="{org_ru}">{org_en}</p>
          <p data-en="{desc_en}" data-ru="{desc_ru}">{desc_en}</p>
        </div>
      </article>'''

experience_main = '''    <div class="page-header">
      <p class="eyebrow"><span class="mark"></span><span data-en="01 \u2014 Experience" data-ru="01 \u2014 \u041e\u043f\u044b\u0442">01 \u2014 Experience</span></p>
      <h1 class="page-title">
        <span class="lang-en">Experience</span>
        <span class="lang-ru" lang="ru">\u041e\u043f\u044b\u0442</span>
      </h1>
      <p class="page-intro" data-en="A record of roles, placements, and research positions. Replace each box below with your own history \u2014 titles, institutions, and dates." data-ru="\u0425\u0440\u043e\u043d\u0438\u043a\u0430 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0435\u0439, \u0441\u0442\u0430\u0436\u0438\u0440\u043e\u0432\u043e\u043a \u0438 \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u043e\u0439 \u0440\u0430\u0431\u043e\u0442\u044b. \u0417\u0430\u043c\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0436\u0434\u044b\u0439 \u0431\u043b\u043e\u043a \u043d\u0438\u0436\u0435 \u0441\u0432\u043e\u0435\u0439 \u0438\u0441\u0442\u043e\u0440\u0438\u0435\u0439 \u2014 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044f\u043c\u0438, \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f\u043c\u0438 \u0438 \u0434\u0430\u0442\u0430\u043c\u0438.">A record of roles, placements, and research positions. Replace each box below with your own history \u2014 titles, institutions, and dates.</p>
    </div>

    <div class="experience-list">
''' + "\n\n".join([
    experience_item(
        "[PLACEHOLDER \u2014 MONTH YEAR] \u2013 [PLACEHOLDER \u2014 MONTH YEAR]",
        "[\u041c\u0415\u0421\u042f\u0426, \u0413\u041e\u0414] \u2013 [\u041c\u0415\u0421\u042f\u0426, \u0413\u041e\u0414]",
        "[PLACEHOLDER \u2014 ROLE TITLE]", "[\u0414\u041e\u041b\u0416\u041d\u041e\u0421\u0422\u042c]",
        "[PLACEHOLDER \u2014 INSTITUTION / GALLERY / ORGANISATION], [PLACEHOLDER \u2014 CITY]",
        "[\u041e\u0420\u0413\u0410\u041d\u0418\u0417\u0410\u0426\u0418\u042f / \u0413\u0410\u041b\u0415\u0420\u0415\u042f], [\u0413\u041e\u0420\u041e\u0414]",
        "[PLACEHOLDER \u2014 description of responsibilities and outcomes. E.g. assisted with collections research, contributed to exhibition planning, or supported public programming. Keep this to two or three sentences.]",
        "[\u041c\u0415\u0421\u0422\u041e \u0414\u041b\u042f \u041e\u041f\u0418\u0421\u0410\u041d\u0418\u042f \u2014 \u043e\u043f\u0438\u0448\u0438\u0442\u0435 \u043e\u0431\u044f\u0437\u0430\u043d\u043d\u043e\u0441\u0442\u0438 \u0438 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: \u0443\u0447\u0430\u0441\u0442\u0438\u0435 \u0432 \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0438 \u043a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u0439, \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0438 \u0432\u044b\u0441\u0442\u0430\u0432\u043e\u043a \u0438\u043b\u0438 \u043f\u0443\u0431\u043b\u0438\u0447\u043d\u044b\u0445 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430\u0445. \u0414\u0432\u0430-\u0442\u0440\u0438 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f.]"
    ),
    experience_item(
        "[PLACEHOLDER \u2014 MONTH YEAR] \u2013 [PLACEHOLDER \u2014 MONTH YEAR]",
        "[\u041c\u0415\u0421\u042f\u0426, \u0413\u041e\u0414] \u2013 [\u041c\u0415\u0421\u042f\u0426, \u0413\u041e\u0414]",
        "[PLACEHOLDER \u2014 ROLE TITLE]", "[\u0414\u041e\u041b\u0416\u041d\u041e\u0421\u0422\u042c]",
        "[PLACEHOLDER \u2014 INSTITUTION / GALLERY / ORGANISATION], [PLACEHOLDER \u2014 CITY]",
        "[\u041e\u0420\u0413\u0410\u041d\u0418\u0417\u0410\u0426\u0418\u042f / \u0413\u0410\u041b\u0415\u0420\u0415\u042f], [\u0413\u041e\u0420\u041e\u0414]",
        "[PLACEHOLDER \u2014 description of responsibilities and outcomes. E.g. cataloguing, condition reporting, provenance research, or archival work.]",
        "[\u041c\u0415\u0421\u0422\u041e \u0414\u041b\u042f \u041e\u041f\u0418\u0421\u0410\u041d\u0418\u042f \u2014 \u043e\u043f\u0438\u0448\u0438\u0442\u0435 \u043e\u0431\u044f\u0437\u0430\u043d\u043d\u043e\u0441\u0442\u0438 \u0438 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0438\u0437\u0430\u0446\u0438\u044f, \u0441\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0430\u043a\u0442\u043e\u0432 \u0441\u043e\u0445\u0440\u0430\u043d\u043d\u043e\u0441\u0442\u0438, \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0432\u0435\u043d\u0430\u043d\u0441\u0430 \u0438\u043b\u0438 \u0430\u0440\u0445\u0438\u0432\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430.]"
    ),
    experience_item(
        "[PLACEHOLDER \u2014 MONTH YEAR] \u2013 [PLACEHOLDER \u2014 MONTH YEAR]",
        "[\u041c\u0415\u0421\u042f\u0426, \u0413\u041e\u0414] \u2013 [\u041c\u0415\u0421\u042f\u0426, \u0413\u041e\u0414]",
        "[PLACEHOLDER \u2014 ROLE TITLE]", "[\u0414\u041e\u041b\u0416\u041d\u041e\u0421\u0422\u042c]",
        "[PLACEHOLDER \u2014 INSTITUTION / GALLERY / ORGANISATION], [PLACEHOLDER \u2014 CITY]",
        "[\u041e\u0420\u0413\u0410\u041d\u0418\u0417\u0410\u0426\u0418\u042f / \u0413\u0410\u041b\u0415\u0420\u0415\u042f], [\u0413\u041e\u0420\u041e\u0414]",
        "[PLACEHOLDER \u2014 description of responsibilities and outcomes. E.g. teaching assistance, gallery education, or front-of-house / visitor experience.]",
        "[\u041c\u0415\u0421\u0422\u041e \u0414\u041b\u042f \u041e\u041f\u0418\u0421\u0410\u041d\u0418\u042f \u2014 \u043e\u043f\u0438\u0448\u0438\u0442\u0435 \u043e\u0431\u044f\u0437\u0430\u043d\u043d\u043e\u0441\u0442\u0438 \u0438 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: \u043f\u043e\u043c\u043e\u0449\u044c \u0432 \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u0438, \u0430\u0440\u0442-\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0438\u043b\u0438 \u0440\u0430\u0431\u043e\u0442\u0430 \u0441 \u043f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u044f\u043c\u0438.]"
    ),
]) + '''
    </div>

    <p class="page-footer"><span data-en="To add a fourth entry, duplicate an" data-ru="\u0427\u0442\u043e\u0431\u044b \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0447\u0435\u0442\u0432\u0451\u0440\u0442\u0443\u044e \u0437\u0430\u043f\u0438\u0441\u044c, \u0441\u043a\u043e\u043f\u0438\u0440\u0443\u0439\u0442\u0435 \u0431\u043b\u043e\u043a">To add a fourth entry, duplicate an</span> <code>.experience-item</code> <span data-en="block in experience.html." data-ru="\u0432 experience.html.">block in experience.html.</span></p>'''

open('site/experience.html', 'w', encoding='utf-8').write(
    page("Experience \u2014 [PLACEHOLDER \u2014 YOUR NAME]", "\u041e\u043f\u044b\u0442 \u2014 [PLACEHOLDER \u2014 \u0412\u0410\u0428\u0415 \u0418\u041c\u042f]",
         None, None, experience_main)
)
# ---------------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------------
def project_card(svg, tag_en, tag_ru, title_en, title_ru, desc_en, desc_ru):
    return f'''      <article class="project-card">
        <div class="project-thumb">
{svg}
        </div>
        <p class="project-tag"><span class="mark"></span><span data-en="{tag_en}" data-ru="{tag_ru}">{tag_en}</span></p>
        <h3 data-en="{title_en}" data-ru="{title_ru}">{title_en}</h3>
        <p data-en="{desc_en}" data-ru="{desc_ru}">{desc_en}</p>
        <a href="#" class="project-more"><span class="mark"></span><span data-en="View project" data-ru="\u0421\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442">View project</span></a>
      </article>'''

svg1 = '''          <svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="300" fill="#eae7df"/>
            <rect x="40" y="40" width="140" height="220" fill="#141414"/>
            <rect x="200" y="60" width="160" height="16" fill="#c81e1e"/>
            <circle cx="280" cy="180" r="60" fill="none" stroke="#141414" stroke-width="6"/>
            <line x1="40" y1="260" x2="360" y2="40" stroke="#141414" stroke-width="2"/>
          </svg>'''
svg2 = '''          <svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="300" fill="#eae7df"/>
            <rect x="60" y="220" width="280" height="14" fill="#141414"/>
            <rect x="60" y="180" width="200" height="14" fill="#141414"/>
            <rect x="60" y="140" width="120" height="14" fill="#c81e1e"/>
            <rect x="290" y="60" width="60" height="60" fill="#141414" transform="rotate(45 320 90)"/>
          </svg>'''
svg3 = '''          <svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="300" fill="#eae7df"/>
            <polygon points="60,240 200,60 340,240" fill="none" stroke="#141414" stroke-width="6"/>
            <rect x="180" y="150" width="40" height="40" fill="#c81e1e"/>
          </svg>'''
svg4 = '''          <svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="300" fill="#eae7df"/>
            <rect x="50" y="50" width="90" height="90" fill="#141414"/>
            <rect x="160" y="50" width="90" height="90" fill="none" stroke="#141414" stroke-width="4"/>
            <rect x="270" y="50" width="90" height="90" fill="#c81e1e"/>
            <line x1="50" y1="200" x2="360" y2="200" stroke="#141414" stroke-width="2"/>
            <line x1="50" y1="230" x2="360" y2="230" stroke="#141414" stroke-width="2"/>
          </svg>'''

projects_main = '''    <div class="page-header">
      <p class="eyebrow"><span class="mark"></span><span data-en="02 \u2014 Projects" data-ru="02 \u2014 \u041f\u0440\u043e\u0435\u043a\u0442\u044b">02 \u2014 Projects</span></p>
      <h1 class="page-title">
        <span class="lang-en">Projects</span>
        <span class="lang-ru" lang="ru">\u041f\u0440\u043e\u0435\u043a\u0442\u044b</span>
      </h1>
      <p class="page-intro" data-en="Research and coursework from the MA, plus independent writing. Swap the placeholder thumbnails for your own installation shots, essay covers, or archival material." data-ru="\u0418\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u044f \u0438 \u0440\u0430\u0431\u043e\u0442\u044b \u0432\u0440\u0435\u043c\u04451 \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u0430\u0442\u0443\u0440\u044b, \u0430 \u0442\u0430\u043a\u0436\u0435 \u0441\u0430\u043c\u043e\u0441\u0442\u043e\u044f\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0442\u0435\u043a\u0441\u0442\u044b. \u0417\u0430\u043c\u0435\u043d\u0438\u0442\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f-\u0437\u0430\u0433\u043b\u0443\u0448\u043a\u0438 \u043d\u0430 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438 \u0438\u043d\u0441\u0442\u0430\u043b\u043b\u044f\u0446\u0438\u0439, \u043e\u0431\u043b\u043e\u0436\u043a\u0438 \u044d\u0441\u0441\u0435 \u0438\u043b\u0438 \u0430\u0440\u0445\u0438\u0432\u043d\u044b\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b.">Research and coursework from the MA, plus independent writing. Swap the placeholder thumbnails for your own installation shots, essay covers, or archival material.</p>
    </div>

    <div class="project-grid">

''' + "\n\n".join([
    project_card(svg1, "MA Research Essay \u2014 [PLACEHOLDER YEAR]", "\u0418\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u043e\u0435 \u044d\u0441\u0441\u0435 (\u043c\u0430\u0433\u0438\u0441\u0442\u0440\u0430\u0442\u0443\u0440\u0430) \u2014 [\u0413\u041e\u0414]",
                 "[PLACEHOLDER \u2014 PROJECT TITLE]", "[\u041d\u0410\u0417\u0412\u0410\u041d\u0418\u0415 \u041f\u0420\u041e\u0415\u041a\u0422\u0410]",
                 "[PLACEHOLDER \u2014 one to two sentence description of the project, its scope, and any institution or archive involved.]",
                 "[\u041c\u0415\u0421\u0422\u041e \u0414\u041b\u042f \u041e\u041f\u0418\u0421\u0410\u041d\u0418\u042f \u2014 \u043e\u0434\u043d\u043e-\u0434\u0432\u0430 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043e \u043f\u0440\u043e\u0435\u043a\u0442\u0435, \u0435\u0433\u043e \u043e\u0445\u0432\u0430\u0442\u0435 \u0438 \u0443\u0447\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u0438 \u0438\u043b\u0438 \u0430\u0440\u0445\u0438\u0432\u0435, \u0435\u0441\u043b\u0438 \u043e\u043d\u0438 \u0431\u044b\u043b\u0438 \u0437\u0430\u0434\u0435\u0439\u0441\u0442\u0432\u043e\u0432\u0430\u043d\u044b.]"),
    project_card(svg2, "Dissertation Chapter \u2014 [PLACEHOLDER YEAR]", "\u0413\u043b\u0430\u0432\u0430 \u0434\u0438\u0441\u0441\u0435\u0440\u0442\u0430\u0446\u0438\u0438 \u2014 [\u0413\u041e\u0414]",
                 "[PLACEHOLDER \u2014 PROJECT TITLE]", "[\u041d\u0410\u0417\u0412\u0410\u041d\u0418\u0415 \u041f\u0420\u041e\u0415\u041a\u0422\u0410]",
                 "[PLACEHOLDER \u2014 one to two sentence description, e.g. close reading of a specific artist, exhibition, or publication.]",
                 "[\u041c\u0415\u0421\u0422\u041e \u0414\u041b\u042f \u041e\u041f\u0418\u0421\u0410\u041d\u0418\u042f \u2014 \u043e\u0434\u043d\u043e-\u0434\u0432\u0430 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 \u0431\u043b\u0438\u0437\u043a\u043e\u0435 \u0440\u0430\u0441\u0441\u043c\u043e\u0442\u0440\u0435\u043d\u0438\u0435 \u0442\u0432\u043e\u0440\u0447\u0435\u0441\u0442\u0432\u0430 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u0445\u0443\u0434\u043e\u0436\u043d\u0438\u043a\u0430, \u0432\u044b\u0441\u0442\u0430\u0432\u043a\u0438 \u0438\u043b\u0438 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438.]"),
    project_card(svg3, "Curatorial Proposal \u2014 [PLACEHOLDER YEAR]", "\u041a\u0443\u0440\u0430\u0442\u043e\u0440\u0441\u043a\u043e\u0435 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u2014 [\u0413\u041e\u0414]",
                 "[PLACEHOLDER \u2014 PROJECT TITLE]", "[\u041d\u0410\u0417\u0412\u0410\u041d\u0418\u0415 \u041f\u0420\u041e\u0415\u041a\u0422\u0410]",
                 "[PLACEHOLDER \u2014 one to two sentence description of an exhibition concept, checklist, or gallery proposal you developed.]",
                 "[\u041c\u0415\u0421\u0422\u041e \u0414\u041b\u042f \u041e\u041f\u0418\u0421\u0410\u041d\u0418\u042f \u2014 \u043e\u0434\u043d\u043e-\u0434\u0432\u0430 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043e \u043a\u043e\u043d\u0446\u0435\u043f\u0446\u0438\u0438 \u0432\u044b\u0441\u0442\u0430\u0432\u043a\u0438, \u0441\u043f\u0438\u0441\u043a\u0435 \u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0439 \u0438\u043b\u0438 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0438 \u0434\u043b\u044f \u0433\u0430\u043b\u0435\u0440\u0435\u0438.]"),
    project_card(svg4, "Conference Paper \u2014 [PLACEHOLDER YEAR]", "\u0414\u043e\u043a\u043b\u0430\u0434 \u043d\u0430 \u043a\u043e\u043d\u0444\u0435\u0440\u0435\u043d\u0446\u0438\u0438 \u2014 [\u0413\u041e\u0414]",
                 "[PLACEHOLDER \u2014 PROJECT TITLE]", "[\u041d\u0410\u0417\u0412\u0410\u041d\u0418\u0415 \u041f\u0420\u041e\u0415\u041a\u0422\u0410]",
                 "[PLACEHOLDER \u2014 one to two sentence description of the paper, where it was presented, and its central argument.]",
                 "[\u041c\u0415\u0421\u0422\u041e \u0414\u041b\u042f \u041e\u041f\u0418\u0421\u0410\u041d\u0418\u042f \u2014 \u043e\u0434\u043d\u043e-\u0434\u0432\u0430 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043e \u0434\u043e\u043a\u043b\u0430\u0434\u0435, \u043c\u0435\u0441\u0442\u0435 \u0435\u0433\u043e \u043f\u0440\u0435\u0437\u0435\u043d\u0442\u0430\u0446\u0438\u0438 \u0438 \u0435\u0433\u043e \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u043c \u0442\u0435\u0437\u0438\u0441\u0435.]"),
]) + '''

    </div>

    <p class="page-footer"><span data-en="Thumbnails are original placeholder compositions \u2014 replace" data-ru="\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u2014 \u043e\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u043a\u043e\u043c\u043f\u043e\u0437\u0438\u0446\u0438\u0438-\u0437\u0430\u0433\u043b\u0443\u0448\u043a\u0438 \u2014 \u0437\u0430\u043c\u0435\u043d\u0438\u0442\u0435 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435">Thumbnails are original placeholder compositions \u2014 replace</span> <code>.project-thumb</code> <span data-en="contents with your own images (e.g." data-ru="\u043d\u0430 \u0441\u0432\u043e\u0438 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440,">contents with your own images (e.g.</span> <code>&lt;img src="assets/images/project-1.jpg" alt="..."&gt;</code><span data-en="." data-ru=").">.</span></p>'''

open('site/projects.html', 'w', encoding='utf-8').write(
    page("Projects \u2014 [PLACEHOLDER \u2014 YOUR NAME]", "\u041f\u0440\u043e\u0435\u043a\u0442\u044b \u2014 [PLACEHOLDER \u2014 \u0412\u0410\u0428\u0415 \u0418\u041c\u042f]",
         None, None, projects_main)
)
print("projects.html written")

# ---------------------------------------------------------------
# RESUME
# ---------------------------------------------------------------
resume_main = '''    <div class="page-header">
      <p class="eyebrow"><span class="mark"></span><span data-en="03 \u2014 Resume" data-ru="03 \u2014 \u0420\u0435\u0437\u044e\u043c\u0435">03 \u2014 Resume</span></p>
      <h1 class="page-title">
        <span class="lang-en">Resume</span>
        <span class="lang-ru" lang="ru">\u0420\u0435\u0437\u044e\u043c\u0435</span>
      </h1>
      <p class="page-intro"><span data-en="Add your resume as" data-ru="\u0414\u043e\u0431\u0430\u0432\u044c\u0442\u0435 \u0441\u0432\u043e\u0451 \u0440\u0435\u0437\u044e\u043c\u0435 \u043f\u043e \u043f\u0443\u0442\u0438">Add your resume as</span> <code>assets/resume/resume.pdf</code> <span data-en="and it will appear below automatically, with a download link." data-ru="\u0438 \u043e\u043d\u043e \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u043e\u044f\u0432\u0438\u0442\u0441\u044f \u043d\u0438\u0436\u0435, \u0432\u043c\u0435\u0441\u0442\u0435 \u0441\u043e \u0441\u0441\u044b\u043b\u043a\u043e\u0439 \u0434\u043b\u044f \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u044f.">and it will appear below automatically, with a download link.</span></p>
    </div>

    <div class="resume-frame-wrap" id="resume-frame-wrap">
      <div class="resume-placeholder" id="resume-placeholder">
        <span class="mark" style="display:block;width:14px;height:14px;"></span>
        <span data-en="[PLACEHOLDER]" data-ru="[PLACEHOLDER]">[PLACEHOLDER]</span><br>
        <span data-en="Add your PDF at" data-ru="\u0414\u043e\u0431\u0430\u0432\u044c\u0442\u0435 \u0432\u0430\u0448 PDF \u043f\u043e \u043f\u0443\u0442\u0438">Add your PDF at</span><br>
        <code>assets/resume/resume.pdf</code>
      </div>
      <iframe id="resume-iframe" src="assets/resume/resume.pdf" title="Resume" style="display:none;"></iframe>
    </div>

    <div class="resume-actions">
      <a class="btn" href="assets/resume/resume.pdf" download>
        <span class="mark"></span><span data-en="Download PDF" data-ru="\u0421\u043a\u0430\u0447\u0430\u0442\u044c PDF">Download PDF</span>
      </a>
      <a class="text-link" href="assets/resume/resume.pdf" target="_blank" rel="noopener" data-en="Open in new tab" data-ru="\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u043d\u043e\u0432\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0435">Open in new tab</a>
    </div>

    <p class="page-footer"><span data-en="The download and &quot;open in new tab&quot; links point to the same path \u2014 once" data-ru="\u0421\u0441\u044b\u043b\u043a\u0438 \u00ab\u0441\u043a\u0430\u0447\u0430\u0442\u044c\u00bb \u0438 \u00ab\u043e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u043d\u043e\u0432\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0435\u00bb \u0432\u0435\u0434\u0443\u0442 \u043f\u043e \u043e\u0434\u043d\u043e\u043c\u0443 \u0438 \u0442\u043e\u043c\u0443 \u0436\u0435 \u043f\u0443\u0442\u0438 \u2014 \u043a\u0430\u043a \u0442\u043e\u043b\u044c\u043a\u043e">The download and "open in new tab" links point to the same path \u2014 once</span> <code>resume.pdf</code> <span data-en="exists in" data-ru="\u043f\u043e\u044f\u0432\u0438\u0442\u0441\u044f \u0432">exists in</span> <code>assets/resume/</code><span data-en=", both work with no further edits." data-ru=", \u043e\u0431\u0435 \u0441\u0441\u044b\u043b\u043a\u0438 \u0437\u0430\u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0442 \u0431\u0435\u0437 \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u043f\u0440\u0430\u0432\u043e\u043a.">, both work with no further edits.</span></p>'''

resume_extra_script = '''<script>
  // Quietly check whether resume.pdf actually exists before showing
  // the embed, so the placeholder is what renders until it's added.
  (function () {
    var path = "assets/resume/resume.pdf";
    fetch(path, { method: "HEAD" })
      .then(function (res) {
        if (res.ok) {
          document.getElementById("resume-placeholder").style.display = "none";
          document.getElementById("resume-iframe").style.display = "block";
        }
      })
      .catch(function () {
        /* file:// or offline preview \u2014 leave the placeholder showing */
      });
  })();
</script>
'''

resume_html = page("Resume \u2014 [PLACEHOLDER \u2014 YOUR NAME]", "\u0420\u0435\u0437\u044e\u043c\u0435 \u2014 [PLACEHOLDER \u2014 \u0412\u0410\u0428\u0415 \u0418\u041c\u042f]",
                    None, None, resume_main)
resume_html = resume_html.replace("</body>", resume_extra_script + "</body>")
open('site/resume.html', 'w', encoding='utf-8').write(resume_html)
print("resume.html written")

# ---------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------
contact_main = '''    <div class="page-header">
      <p class="eyebrow"><span class="mark"></span><span data-en="04 \u2014 Contact" data-ru="04 \u2014 \u0421\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f">04 \u2014 Contact</span></p>
      <h1 class="page-title">
        <span class="lang-en">Contact</span>
        <span class="lang-ru" lang="ru">\u0421\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f</span>
      </h1>
      <p class="page-intro" data-en="The quickest way to reach me. Replace the email address below with your own \u2014 the link is set to open the visitor's mail client automatically." data-ru="\u0421\u0430\u043c\u044b\u0439 \u0431\u044b\u0441\u0442\u0440\u044b\u0439 \u0441\u043f\u043e\u0441\u043e\u0431 \u0441\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u0441\u043e \u043c\u043d\u043e\u0439. \u0417\u0430\u043c\u0435\u043d\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u044b \u043d\u0438\u0436\u0435 \u043d\u0430 \u0441\u0432\u043e\u0439 \u2014 \u0441\u0441\u044b\u043b\u043a\u0430 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u043e\u0442\u043a\u0440\u043e\u0435\u0442 \u043f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u043a\u043b\u0438\u0435\u043d\u0442 \u043f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u044f.">The quickest way to reach me. Replace the email address below with your own \u2014 the link is set to open the visitor's mail client automatically.</p>
    </div>

    <div class="contact-block">
      <a class="contact-email" href="mailto:[PLACEHOLDER@EMAIL.COM]">
        <span class="mark"></span>[PLACEHOLDER@EMAIL.COM]
      </a>

      <ul class="contact-list">
        <li><span class="label" data-en="Location" data-ru="\u041c\u0435\u0441\u0442\u043e\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435">Location</span> <span data-en="London, UK" data-ru="\u041b\u043e\u043d\u0434\u043e\u043d, \u0412\u0435\u043b\u0438\u043a\u043e\u0431\u0440\u0438\u0442\u0430\u043d\u0438\u044f">London, UK</span></li>
        <li><span class="label">LinkedIn</span> <a href="#" class="text-link" data-en="[PLACEHOLDER \u2014 LINKEDIN URL]" data-ru="[PLACEHOLDER \u2014 \u0421\u0421\u042b\u041b\u041a\u0410 \u041d\u0410 LINKEDIN]">[PLACEHOLDER \u2014 LINKEDIN URL]</a></li>
        <li><span class="label">Instagram</span> <a href="#" class="text-link" data-en="[PLACEHOLDER \u2014 @HANDLE]" data-ru="[PLACEHOLDER \u2014 @\u0410\u041a\u041a\u0410\u0423\u041d\u0422]">[PLACEHOLDER \u2014 @HANDLE]</a></li>
      </ul>
    </div>

    <p class="page-footer"><span data-en="To change the email, edit the" data-ru="\u0427\u0442\u043e\u0431\u044b \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c email, \u043e\u0442\u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u0443\u0439\u0442\u0435 \u0430\u0434\u0440\u0435\u0441">To change the email, edit the</span> <code>mailto:</code> <span data-en="address in contact.html (and the matching link in the sidebar footer on every page)." data-ru="\u0432 contact.html (\u0438 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0443\u044e \u0441\u0441\u044b\u043b\u043a\u0443 \u0432 \u043f\u043e\u0434\u0432\u0430\u043b\u0435 \u0441\u0430\u0439\u0434\u0431\u0430\u0440\u0430 \u043d\u0430 \u043a\u0430\u0436\u0434\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435).">address in contact.html (and the matching link in the sidebar footer on every page).</span></p>'''

open('site/contact.html', 'w', encoding='utf-8').write(
    page("Contact \u2014 [PLACEHOLDER \u2014 YOUR NAME]", "\u0421\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u2014 [PLACEHOLDER \u2014 \u0412\u0410\u0428\u0415 \u0418\u041c\u042f]",
         None, None, contact_main)
)
print("contact.html written")