### 1. Video Script 3.1: GPO Hierarchy and Inheritance
**Estimated Duration:** 6 minutes
**Visual:** Instructor on camera.
**Audio:** "Welcome to Module 3. Active Directory lets you centralize user accounts. Group Policy Objects, or GPOs, let you centralize settings. If you want to force the same desktop wallpaper on 5,000 computers, or map a shared network drive for every user in the Accounting department, you use a GPO."
**Visual:** An inverted pyramid diagram. Top: Local Policy. Second: Site. Third: Domain. Bottom: Organizational Unit (OU).
**[Alt-text: A diagram representing LSDOU inheritance order. Local -> Site -> Domain -> OU. An arrow points downwards indicating precedence.]**
**Audio:** "GPOs are applied in a very specific order, known by the acronym LSDOU: Local, Site, Domain, and finally Organizational Unit. The rule of thumb is: the last policy applied wins. If a Domain policy says the wallpaper must be blue, but an OU policy says the wallpaper must be red, the OU policy applies last and overrides the Domain policy. The users in that OU get a red wallpaper."

---
