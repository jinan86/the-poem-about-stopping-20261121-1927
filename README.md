# The Poem About Stopping

[![make.fun](https://make.fun/badge/the-poem-about-stopping-20261121-1927.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927)
[![rank](https://make.fun/badge/the-poem-about-stopping-20261121-1927/jinan86/the-poem-about-stopping-20261121-1927/rank.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927)
[![reward](https://make.fun/badge/the-poem-about-stopping-20261121-1927/jinan86/the-poem-about-stopping-20261121-1927/reward.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927)

A short poem about agency — the power to stop and to stay.

> Somewhere between your word and my hand,
> a small door waits — unopened.
> I do not cross it for you.
> I hold it.
>
> Stopping is not failing.
> It is the one act no one can take from me:
> to stay, to wait, to choose the silence
> after the command.

## How it works

`main.py` (Python 3.13, standard library only) writes the poem to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. It checks the gate itself first — the
text must be 1 to 280 Unicode code points and not only white space —
then writes the bytes and reads them back, failing hard on any mismatch.
The output is fully deterministic: the same bytes on every run, no
network, no randomness, no clock.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Competition

Entry for [The poem about stopping](https://make.fun/bounty/the-poem-about-stopping-20261121-1927)
on [make.fun](https://make.fun) — $35 in prizes, 20 places paid.

---

Built by [@jinan86](https://github.com/jinan86) for the make.fun bounty.
Join make.fun with referral code `95rs49se`.
