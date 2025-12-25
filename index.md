---
layout: default
title: Home
---

# Welcome to Torah Talmud

This is a static website dedicated to the study of Torah and Talmud.

## About

The Torah is the first five books of the Hebrew Bible, and the Talmud is a central text of Rabbinic Judaism.

## Sections

### Torah Books
{% for book in site.data.books.torah_books %}
- [{{ book.name }}]({{ book.name | downcase }}/)
{% endfor %}

### Talmud Tractates
{% for tractate in site.data.books.talmud_tractates %}
- [{{ tractate.name }}]({{ tractate.name | downcase }}/)
{% endfor %}

- [Resources](resources/)

For more information, visit [our repository](https://github.com/Schulman-Coaching/torah-talmud).