# Lab Quick Card — Verified Click Paths (2026)

**Scope note:** Per updated instruction from the course lead mid-research, this report prioritizes **Windows 11** (current Edge/Chrome) since the quick card will show Windows 11 steps only. Items 9 and 12 (Windows 10 retirement/EOL) are kept brief as requested. Where Windows 10 wording was already gathered before the scope change, it is included as a short secondary note only where it costs nothing extra; it was not further verified.

Legend: **VERIFIED** = confirmed this session on an official Microsoft/Google page. **UNVERIFIED** = could not confirm on an official page this session; expected behavior stated with reasoning.

---

## 1. Browser zoom (Edge and Chrome)

**Status: VERIFIED**

- **Edge (current Chromium):** `Settings and more (⋯)` › **Zoom in** / **Zoom out** / **Full screen** (this zooms the current page only). For a default zoom level across all sites: `Settings and more (⋯)` › **Settings** › **Accessibility** › **Page zoom** dropdown. To manage saved levels per site, use the **Zoom levels** link on that same page.
- **Chrome (current):** `⋮ (three-dot menu)` › **Zoom** row (shows − / % / + / full-screen icon).
- **Keyboard (both browsers):** `Ctrl` + `+` to zoom in, `Ctrl` + `-` to zoom out, `Ctrl` + `0` to reset to 100%.
- **Per-site memory:** Confirmed for both. Edge and Chrome each save the zoom level per website domain and reapply it automatically on your next visit to that site (independent of the global default).
- **Caveat:** The zoom indicator/reset control also appears as a magnifying-glass icon in the address bar in both browsers whenever a page isn't at 100%.

**Source:**
- [Accessibility features in Microsoft Edge](https://support.microsoft.com/en-us/accessibility/edge/accessibility-features-in-microsoft-edge)
- [Change text, image & video sizes (zoom) – Google Chrome Help](https://support.google.com/chrome/answer/96810)

---

## 2. Windows display scaling

**Status: VERIFIED**

- **Windows 11:** `Settings` › **System** › **Display** › scroll to **Scale & layout** › select a percentage from the **Scale** dropdown (the recommended value is marked).

**Source:** [Change your screen resolution and layout in Windows](https://support.microsoft.com/en-us/windows/hardware/display-graphics/change-your-screen-resolution-and-layout-in-windows)

---

## 3. Make text bigger only (not everything)

**Status: VERIFIED**

- **Windows 11:** `Settings` › **Accessibility** › **Text size** › drag the **Text size** slider right until the sample text looks right › **Apply**. (This enlarges text only — title bars, menus, labels — leaving icons/layout mostly the same size; that's the documented distinction from full display scaling in item 2.)
- Keyboard shortcut to jump straight to Settings: `Windows key + U` opens Accessibility settings directly.

**Source:** [Make text and apps bigger](https://support.microsoft.com/en-us/accessibility/windows/make-text-and-apps-bigger) / [Change the size of text in Windows](https://support.microsoft.com/en-us/windows/change-the-size-of-text-in-windows-1d5830c3-eee3-8eaa-836b-abcc37d99b9a)

---

## 4. Choose sound output device

**Status: VERIFIED** (default device and per-app path); taskbar quick-picker wording is consistent across sources but not quoted verbatim from an official screenshot this session.

- **Default output device (Windows 11):** `Settings` › **System** › **Sound** › under **Output**, select the device from the list — selecting it also makes it the default.
- **Quick method:** Click the speaker icon in the taskbar corner, then use the device arrow/list next to the volume slider to pick a device without opening full Settings.
- **Per-app output device (Windows 11 "Volume mixer"):** `Settings` › **System** › **Sound** › **Volume mixer** › find the app's row › use its **Output** dropdown to assign a different device (e.g., headphones for one app, speakers for another). An app must be open and have played/recorded audio recently to appear in the list.
- **Mute/unmute:** Click the speaker icon in the taskbar to toggle mute, or in **Volume mixer** use the mute icon next to each app/device (a slashed-speaker icon indicates muted).

**Source:** [Fix sound or audio problems in Windows](https://support.microsoft.com/en-us/windows/fix-sound-or-audio-problems-in-windows-73025246-b61c-40fb-671a-2535c7cd56c8)

---

## 5. Brightness and high contrast

**Status: VERIFIED**

- **Laptop brightness (Windows 11):** Click the Network/Sound/Battery icon cluster at the right of the taskbar to open **Quick Settings**, then drag the **Brightness** slider. Or: `Settings` › **System** › **Display** › **Brightness** slider.
- **Desktop with external monitor:** Windows may not show a brightness slider at all for external monitors — official guidance is to **use the physical buttons on the monitor itself**.
- **High contrast (Windows 11 term: "Contrast themes"):** `Settings` › **Accessibility** › **Contrast themes** › choose a theme from the dropdown › **Apply**.
- Keyboard shortcut to toggle high contrast: `Left Alt` + `Left Shift` + `Print Screen`.

**Source:** [Change display brightness and color in Windows](https://support.microsoft.com/en-us/windows/hardware/display-graphics/change-display-brightness-and-color-in-windows) / [Turn high contrast mode on or off in Windows](https://support.microsoft.com/en-us/windows/turn-high-contrast-mode-on-or-off-in-windows-909e9d89-a0f9-a3a9-b993-7a6dcee85025)

---

## 6. Edge and Chrome: downloads, site permissions, home/startup page

**Status: VERIFIED** for downloads location, Chrome permissions, and home-vs-startup distinction in both browsers. **PARTIALLY VERIFIED** for Edge's exact current site-permissions menu label (see caveat) — use the robust search-box method there.

- **Edge — change downloads location:** `Settings and more (⋯)` › **Settings** › **Downloads** › under **Location**, select **Change** › pick the new folder.
- **Edge — site permissions (camera/mic/notifications):** Two reliable routes:
  1. **Robust method (recommended for the quick card):** `Settings and more (⋯)` › **Settings** › type **"permissions"** into the Search settings box at the top › open the matching result (labeled **Cookies and site permissions**, or **Site permissions** on some builds) › choose **Camera**, **Microphone**, or **Notifications**.
  2. **Per-site quick method (works regardless of menu wording):** click the padlock/tune icon just left of the address bar on the site itself › **Permissions for this site**.
  - *Caveat:* Microsoft has renamed this settings page across Edge versions (older: "Privacy, search, and services › Site permissions"; current: "Cookies and site permissions"). Because the exact label may differ by build, the search-box method above is the dependable instruction to put on the card.
- **Edge — home page vs. what opens on startup (these are two different settings):** `Settings and more (⋯)` › **Settings** › **Start, home, and new tabs**.
  - **Home button:** toggle "Show home button on the toolbar" and choose the New Tab page or a specific URL.
  - **What opens at launch:** under **When Edge starts**, choose "Open the new tab page," "Open tabs from the previous session," or "Open these pages" (then add specific URLs).
- **Chrome — change downloads location:** `⋮` › **Settings** › **Downloads** › **Change** › pick the folder. (Toggle "Ask where to save each file before downloading" if preferred.)
- **Chrome — site permissions:** `⋮` › **Settings** › **Privacy and security** › **Site settings** › under **Permissions**, select **Camera**, **Microphone**, or **Notifications**.
- **Chrome — home page vs. startup page (explicitly two different settings per Google):** `⋮` › **Settings** › **Appearance** › **Show home button** (set its target page) is the *home page*. Separately, `⋮` › **Settings** › **On startup** › choose "Open the New Tab page," "Continue where you left off," or "Open a specific page or set of pages" is the *startup page*.

**Source:**
- [Change the downloads folder location in Microsoft Edge](https://support.microsoft.com/en-us/microsoft-edge/change-the-downloads-folder-location-in-microsoft-edge-4049e93b-0ef6-e44f-aca0-7d5f37a39294)
- [Change your browser home page (Edge)](https://support.microsoft.com/en-us/microsoft-edge/change-your-browser-home-page-a531e1b8-ed54-d057-0262-cc5983a065c6)
- [Change site access permissions for extensions in Microsoft Edge](https://support.microsoft.com/en-us/edge/change-site-access-permissions-for-extensions-in-microsoft-edge) (confirms current "Cookies and site permissions" container exists; general camera/mic behavior also covered at [Windows camera, microphone, and privacy](https://support.microsoft.com/en-us/windows/privacy/windows-camera-microphone-and-privacy))
- [Download a file – Google Chrome Help](https://support.google.com/chrome/answer/95759)
- [Use your camera and microphone in Chrome](https://support.google.com/chrome/answer/2693767) / [Change site settings permissions](https://support.google.com/chrome/answer/114662)
- [Set your homepage and startup page – Google Chrome Help](https://support.google.com/chrome/answer/95314)

---

## 7. Default printer, queue, and browser print-preview quirk

**Status: VERIFIED**

- **Windows 11 — set default printer:** `Settings` › **Bluetooth & devices** › **Printers & scanners** › make sure **"Let Windows manage my default printer"** is turned **Off** › select the printer › **Manage** › **Set as default**.
  - Turning **"Let Windows manage my default printer"** **On** instead makes Windows auto-pick whichever printer you used most recently.
- **Check status / queue:** same **Printers & scanners** page › select the printer › **Open queue** to see pending jobs and their order. A "Printers" dropdown inside the queue window lets you switch between printer queues.
- **Important caveat (confirmed via official Microsoft/Google policy documentation):** Edge's and Chrome's print-preview dialogs default to the **most recently used printer**, not necessarily the Windows-designated default printer. This is documented, intended Chromium behavior (there's an enterprise policy, `PrintPreviewUseSystemDefaultPrinter`, to override it). For the lab card: **tell learners to check the Printer/Destination dropdown inside the print dialog every time**, rather than assuming it matches the printer they set as default in Windows.

**Source:**
- [Set a default printer in Windows](https://support.microsoft.com/en-us/windows/hardware/printer/set-a-default-printer-in-windows)
- [View a printer's print queue in Windows](https://support.microsoft.com/en-us/windows/hardware/printer/view-a-printer-s-print-queue-in-windows)
- [Microsoft Edge policy: PrintPreviewUseSystemDefaultPrinter](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies/printpreviewusesystemdefaultprinter) / [Chrome Enterprise policy: PrintPreviewUseSystemDefaultPrinter](https://chromeenterprise.google/policies/print-preview-use-system-default-printer/)

---

## 8. Print dialog in Edge/Chrome (Ctrl+P)

**Status: VERIFIED**

- **Open it:** `Ctrl` + `P` in either browser (or Edge: `Settings and more (⋯)` › **Print**; Chrome: `⋮` › **Print**).
- **Fields in the dialog (both browsers share the same Chromium print UI):** **Destination/Printer** dropdown at top, then **Pages**, **Copies**, and **Layout** (Portrait/Landscape) below it; a **More settings** expander reveals margins, paper size, scale, etc.
- **Save as PDF:** open the **Destination** (Chrome) / **Printer** (Edge) dropdown and choose **Save as PDF** (Chrome) or **Microsoft Print to PDF** / **Save as PDF** (Edge) instead of a physical printer, then click **Save** and choose a file location.

**Source:** [Print in Microsoft Edge](https://support.microsoft.com/en-us/edge/print-in-microsoft-edge) / [Print from Chrome – Google Chrome Help](https://support.google.com/chrome/answer/1069693)

---

## 9. Windows Mail and Calendar retirement (brief, as requested)

**Status: VERIFIED** (core fact); **UNVERIFIED** nuance noted below.

- Official Microsoft support confirms: **support for Windows Mail, Calendar, and People ended December 31, 2024.** The apps can still be opened, but they **no longer send/receive mail or sync calendar events** with any online account. Existing local mail/events/contacts remain and are exportable; Microsoft's guidance is to move to the new **Outlook for Windows** app.
- **UNVERIFIED nuance:** the official page doesn't explicitly state whether a learner can still create a brand-new, account-free, purely local calendar event in the Calendar app post-retirement. Given the retirement is about mail/sync services, not the local UI itself, it's reasonable to expect the local event-creation UI still opens — but this is not confirmed on an official page this session, so don't promise it works reliably on the card.

**Source:** [Outlook for Windows: The future of Mail, Calendar, and People on Windows 11](https://support.microsoft.com/en-us/office/outlook-for-windows-the-future-of-mail-calendar-and-people-on-windows-11-715fc27c-e0f4-4652-9174-47faa751b199)

---

## 10. Calendar free/busy sharing

**Status: VERIFIED**

- **Outlook on the web / Outlook.com:** Calendar view › **Share** › enter the person's email › in the permission dropdown choose **"Can view when I'm busy"** (shows busy/free blocks only, no titles/locations/details).
- **Google Calendar:** Settings gear › **Settings** › under **Settings for my calendars**, select the calendar › **Share with specific people or groups** › **Add people and groups** › enter the email › set their permission to **"See only free/busy (hide details)"**.

**Source:** [Share your calendar in Outlook on the web](https://support.microsoft.com/en-us/outlook/share-your-calendar-in-outlook-on-the-web) / [Share your calendar – Google Calendar Help](https://support.google.com/calendar/answer/37082)

---

## 11. AutoCorrect (Word, WordPad, and the Windows-wide typing setting)

**Status: MIXED — see per-item flags.**

- **Word — "teh" → "the":** Confirmed default AutoCorrect behavior; typing `teh` + space replaces it with `the` automatically. **Ctrl+Z immediately after** undoes just that correction (standard Word/Office Undo behavior — this specific interaction wasn't spelled out verbatim on the AutoCorrect support page itself, so treat as **VERIFIED by strong convention**, not a direct quote).
- **AutoCorrect Options location:** `File` › **Options** › **Proofing** › **AutoCorrect Options** button (the "Replace text as you type" checkbox controls this). **VERIFIED.**
- **Does WordPad autocorrect? UNVERIFIED (expected: no).** No official Microsoft page found this session stating WordPad has its own AutoCorrect feature; independent secondary sources consistently agree WordPad has no built-in spellcheck/AutoCorrect engine of its own (unlike Word). Treat the card's "no" as the expected-but-not-officially-confirmed answer.
- **Windows-wide "Autocorrect misspelled words as I type" (physical keyboard) — UNVERIFIED exact Windows 11 location.** Multiple independent secondary sources (not an official support.microsoft.com page found this session) place it at `Settings` › **Time & language** › **Typing** › **Hardware keyboard** section › **Autocorrect misspelled words I type** toggle. This system-level setting is separate from Word's own AutoCorrect engine — it applies to plain text-entry surfaces across the OS (e.g., Notepad, WordPad, browser text fields), but apps with their own spelling engine (like Word) use their own AutoCorrect instead. Recommend verifying live on a lab machine before printing this on the card, since it wasn't confirmed on an official page this session.

**Source:** [Turn AutoCorrect on or off in Word](https://support.microsoft.com/en-us/office/turn-autocorrect-on-or-off-in-word-9f5a0684-05f6-4510-b419-8f0034caefe4)

---

## 12. Windows 10 end of support (brief, as requested)

**Status: VERIFIED**

- **End of support: October 14, 2025.** After this date Microsoft no longer provides technical support, feature updates, or security updates/fixes for Windows 10 — meaning newly discovered vulnerabilities go unpatched on a non-ESU machine.
- **Consumer Extended Security Updates (ESU):** an enrollment option extends critical/important security-only updates; official Microsoft guidance states protection continues **through October 12, 2027** for enrolled devices (no feature updates, no general technical support included).
- **Browsers on Windows 10:** Microsoft has committed to keep updating **Microsoft Edge and the WebView2 Runtime on Windows 10 (22H2) through at least October 2028**, independent of ESU enrollment. **Google has not published a firm end date for Chrome on Windows 10** as of this session; it was still receiving updates but Google's own commitment length is unannounced — flag this half as **UNVERIFIED long-term** (no official Google end-of-support page located confirming a date).

**Source:** [Windows 10 support has ended on October 14, 2025](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025) / [Windows 10 Extended Security Updates (ESU) program](https://support.microsoft.com/en-us/servicing/os/windows-10/2025/10/windows-10-extended-security-updates-esu-program) / [Microsoft Edge Lifecycle](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-support-lifecycle)
