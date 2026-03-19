---
title: Writing an ouroboros quine
date: 2019-11-20
tags: code, unix
---

Smart people write C. Pragmatic people write Go. Only a fool would
write C code that outputs Go code that outputs the original C code.

So I made one. Below is the code:

{{< code "ouroboros.c" >}}

If you run it, you should get the result below:

```
$ cc ouroboros.c -o ouroboros
$ ./ouroboros > ouroboros.go
$ go run ouroboros.go > ouroboros2.c
$ diff ouroboros.c ouroboros2.c && cowsay "wtf?"
 ______ 
< wtf? >
 ------ 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

How
---

One of the simplest quines in C looks like this:

```
#include <stdio.h>
int main(){
char*c="#include <stdio.h>%cint main(){%cchar*c=%c%s%c;%cprintf(c,10,10,34,c,34,10,10,10,10);%creturn 0;%c}%c";
printf(c,10,10,34,c,34,10,10,10,10);
return 0;
}
```

I'm not going to dive into the details - there's a detailed explanation
on the tricks and examples for writing quines available in [Rosetta Code's wiki page][rosettacode-quine].

Since I wasn't going to waste my time
hand-crafting the string that should contain the original source code,
I wrote Python code which generates the C code above:

{{< code "codegen.py" >}}

To go further than just a simple quine, I had to make
the quine self-aware, storing the output string in a variable.
To do so I updated the template C code to the one below:

```c
#include <stdio.h>
int main(){
char*c="?",o[1000];
sprintf(o,c,!);
fputs(o, stdout);
return 0;
}
```

The variable `o` now holds the value of the source code.
Next, I came up with Go code snippet that should output it:

    package main;import"fmt";func main(){fmt.Print(`<your_quine_here>`)})

I used back-quoted string since they can contain any characters,
even newlines, which will be present in the `o`.

And the final tricky part - I needed to add the Go code as a C string:

```c
#include <stdio.h>
int main(){
char*c="?",o[1000],g[1000];
sprintf(g,"package main;import%cfmt%c;func main(){fmt.Print(%c%cs%c)}",34,34,96,37,96);
sprintf(o,c,!);
fprintf(stdout,g,o);
return 0;
}
```

The variable `g` now contains the template Go code. 
The trick here is making sure that the variable for Go code
contains `%s` and <code>&#96;</code>, but implicitly.
The former needs to be used in the next `sprintf` call to do the substitution,
and the latter can't be explicit because back-quoted strings in Go cannot contain
back-quote characters.

The final Python code
which outputs the C code
which outputs the Go code
which outputs the C... you got it, is available
<a href="./codegen.py">here</a>.

## Why

Why not?

[rosettacode-quine]: https://rosettacode.org/wiki/Quine
