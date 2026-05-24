---
title: Natural numbers all the way down
date: 2026-05-26
tags: code, python
---

> The distant king of birds, the Simurgh, drops one of his splendid feathers
somewhere in the middle of China; on learning of this, the other birds, tired of
their present anarchy, decide to seek him. They know that the king’s name means
‘thirty birds’; they know that his castle lies in the Kaf, the mountain or range
of mountains that ring the earth. At the outset, some of the birds lose heart:
the nightingale pleads his love for the rose; the parrot pleads his beauty, for
which he lives caged; the partridge cannot do without his home in the hills, nor
the heron with- out his marsh, nor the owl without his ruins. But finally,
certain of them set out on the perilous venture; they cross seven valleys or
seas, the next to last bearing the name Bewilderment, the last the name
Annihilation. Many of the pilgrims desert; the journey takes its toll among the
rest. Thirty, made pure by their sufferings, reach the great peak of the
Simurgh. At last they behold him; they realize that they are the Simurgh, and
that the Simurgh is each of them and all of them.
>
> --- Jorge Luis Borges, excerpt from *The Book of Imaginary Beings*.

I was binge-reading Borges during Covid when I came across a passage describing
a mythical creature - a bird made of birds, where each indivial bird was itself
the whole bird. Don't know why, but that image stayed with me for a while.

A few days later that piece of writing inspired me to create a Droste-style
terminal animation. I knew I'd use Braille effects to render pixels, but I
didn't know what I *actually* wanted to draw.

Sometime later, I had a slightly absurd shower thought: what if natural numbers
where actually natural? As in, what if they existed in the physical world, each
with it's own properties, like mass, weight, and color. In that case numbers,
like matter in the physical is made of atoms, would themselves be composed of
small particles: digits. But if the physical form of numbers and digits were
determined by their written symbols, then there'd be no distinction between the
digit `7` and the number `7`. A digit would itself consist of digits, and so on,
ad infinitum.

With that, I set out to turn the concept into a working implementation. I think it
took me a few attempts over the course of a couple of years to get it right.

It's far from perfect, but I'm fairly satisfied with the final result - you can
see it in action below.

<video src="preview.mp4" loop autoplay controls></video>

If you're interested in the details, the source code is available [here](numbers.py).
