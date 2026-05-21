# Reading Guide: Module 13 - Modules and Packages
## Course: CIS-1310_Intro_to_Python (PCAP (Certified Associate in Python Programming))

---

### Introduction
Welcome to **Module 13 - Modules and Packages**! This week's study material focuses on the core foundations and configuration mechanics of **Modules and Packages** as aligned with the **PCAP (Certified Associate in Python Programming)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Importing modules**: The `import` statement loads a module and makes its contents available under the module's namespace (e.g., `import math` then `math.sqrt(9)`). The `from module import name` form imports a specific name directly into the current namespace without the module prefix; `from module import *` imports all public names but risks overwriting existing names with the same identifier. The PCAP exam tests whether you know that `import math` and `from math import sqrt` produce different namespaces and that module code executes only once — on the first import.
*   **namespaces (import math vs from math import *)**: When you use `import math`, all of `math`'s names live under the `math.` prefix, so there is no risk of collision with your own names. When you use `from math import *`, all exported names are injected directly into the current namespace, which can silently overwrite your own variables if they share a name with something in the module. The PCAP exam strongly discourages wildcard imports in production code and may present questions where a wildcard import causes unexpected name shadowing.
*   **sys.path**: `sys.path` is a list of directory strings that Python searches in order when looking for a module to import; it is populated from the script's directory, the `PYTHONPATH` environment variable, and installation-dependent defaults. You can inspect it at runtime with `import sys; print(sys.path)` and append custom directories to make your own modules discoverable. The PCAP exam may ask why an `import` raises `ModuleNotFoundError` — the answer is usually that the module's directory is not on `sys.path`.
*   **creating custom modules**: Any `.py` file is a module — save functions and variables in `mymath.py` and another script can `import mymath` to use them, provided `mymath.py` is on `sys.path` or in the same directory. The special variable `__name__` equals `"__main__"` when a file is run directly and equals the module name when it is imported; guarding code with `if __name__ == "__main__":` prevents test code from running when the file is used as a library.

---

### 2. Certification Exam Tips
*   **Focus Area:** The PCAP exam tests the difference between `import module` (qualified access via `module.name`) and `from module import name` (unqualified direct access). Know that `import math as m` creates an alias so you can write `m.sqrt()` instead of `math.sqrt()`. Also know the `__name__ == "__main__"` guard — expect a code trace question asking what prints when a module is imported versus run directly.
*   **Scenario Trap:** Watch for questions where `from math import sqrt` is used and then the script defines its own `sqrt` variable — the later assignment overwrites the imported name, and subsequent calls will fail with a `TypeError` or produce unexpected results. Also watch for `ModuleNotFoundError` questions: the module exists but its directory is not in `sys.path`, which is fixed by adjusting the path or installing the package.
*   **Study Resource:** To reinforce these concepts visually, review this targeted playlist: [Python for Everybody Course Playlist - Modules and Packages](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — supplement with the official Python docs on [the import system](https://docs.python.org/3/reference/import.html) for the authoritative description of `sys.path` and namespace resolution tested on the PCAP exam.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Chapter 11 covering **Modules and Packages** in the OER Textbook: [Python for Everybody by Dr. Charles Severance](https://www.py4e.com/book) — a free OER textbook; focus on the sections covering how Python locates modules, the difference between qualified and unqualified imports, and the `__name__` variable that controls whether module-level code runs on import.
*   **Required Video:** Watch the video lecture on **Modules and Packages** in the official course playlist: [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — create a two-file project in the REPL: write `mymath.py` with a custom function and import it from a second script, observing the `__name__` value in each context.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Import `math` and use `math.sqrt()`**: Write `import math` then call `math.sqrt(144)` and print the result; confirm you get `12.0` and that `math` functions are accessed with the `math.` prefix.
*   **Create a custom helper module `mymath.py`**: In a new file `mymath.py`, define `def square(n): return n ** 2` and add a `if __name__ == "__main__": print(square(5))` guard; run the file directly and confirm the guard executes, then import it from another script and confirm it does not.
*   **Import and test functions from `mymath.py` in a separate script**: In `main.py`, write `from mymath import square` and call `print(square(7))`; verify the output is `49` and that no output from the guard block appears.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section/chapter covering **Modules and Packages** in [Python for Everybody](https://www.py4e.com/book).
- [ ] Watch the video lecture on **Modules and Packages** in [Python for Everybody Course Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
