# StudyHub Landing Page (Mobile-First Design)

## Overview
- A mobile-first website landing page for **StudyHub** focused on helping students manage time, stay focused, and track progress.
- The experience prioritizes:
  - Single-column mobile design
  - Accessibility (WCAG)
  - Semantic HTML structure
  - Warm, grounded visual tone

---

## Plan Details

### Screen: Landing Page (Mobile-first; base 390px)

#### 1. Navbar (Header)
- **Mobile:**
  - StudyHub logo (left)
  - Hamburger menu (right)
  - "Skip to content" link (visible on focus)

- **Tablet (≥768px):**
  - Links: Home | Features | Contact
  - Optional CTA button

- **Desktop (≥1024px):**
  - Full horizontal layout
  - CTA on the right

- **Accessibility:**
  - Semantic `<header>` and `<nav>`
  - Focus states
  - ARIA labels

---

#### 2. Hero Section
- **Mobile Layout:**
  - Heading
  - Subtext
  - CTA button
  - Image below

- **Tablet/Desktop:**
  - Two-column layout (text + image)

- **Content:**
  - **Heading:** Focus Better. Study Smarter.
  - **Subtext:** A simple tool to help students stay productive.
  - **CTA:** Get Started

- **Typography:**
  - Responsive using `clamp()`

---

#### 3. Features Section
- **Mobile:** Single column cards
- **Tablet:** Two-column layout
- **Desktop:** Three columns

**Features:**
1. **Time Tracking**  
   Log study sessions and see where your time goes.

2. **Goal Setting**  
   Create study goals and break them into manageable tasks.

3. **Progress Reports**  
   Visualize progress with weekly reports and streaks.

- **Accessibility:**
  - Icons + text labels
  - Proper heading hierarchy

---

#### 4. About Section
- **Mobile:** Single paragraph
- **Tablet/Desktop:** Two-column layout

**Text:**
> StudyHub helps students build productive habits by combining straightforward time tracking, easy goal-setting, and clear progress reports. Built for focus and simplicity.

---

#### 5. Footer
- **Mobile:**
  - Center-aligned
  - Email + social links

- **Tablet/Desktop:**
  - Two-column layout

- **Email:** contact@studyhub.app

---

## Mobile-First Strategy
- Base design: ~390px
- Breakpoints:
  - Tablet: 768px
  - Desktop: 1024px
- Use fluid typography and spacing

---

## Typography

- **Fonts:**
  - Headings: Montserrat
  - Body: Roboto

- **Weights:**
  - 400 (Regular)
  - 600 (SemiBold)
  - 700 (Bold)

- **Responsive Sizes:**
    - Heading: ``clamp(1.5rem, 5vw, 2.25rem)``
    - Subheading: clamp(1.125rem, 3.5vw, 1.5rem)
    - Body: clamp(0.95rem, 1.8vw, 1.125rem)

## Accessibility (WCAG)

- Semantic HTML: `header`, `nav`, `main`, `section`, `footer`
- Proper heading structure (H1 → H2)
- Alt text for all images
- Keyboard navigation support
- Visible focus states
- Contrast ratio:
  - 4.5:1 (normal text)
  - 3:1 (large text)
- "Skip to content" link
- Descriptive labels (avoid "click here")

---

## Visual Direction

- Warm and grounded design
- Soft rounded corners (6–12px)
- Calm blue/teal accents for CTAs
- Light neutral background
- Subtle shadows and elevation
- Minimal and non-distracting motion

---

## Content Copy

- **Brand:** StudyHub
- **Hero Heading:** Focus Better. Study Smarter.
- **Subtext:** A simple tool to help students stay productive.
- **CTA:** Get Started

### Features

- **Time Tracking** — Log study sessions and see where your time goes.
- **Goal Setting** — Create study goals and break them into manageable tasks.
- **Progress Reports** — Visualize progress with weekly reports and streaks.

### About

StudyHub helps students build productive habits by combining straightforward time tracking, easy goal-setting, and clear progress reports. Built for focus and simplicity.

### Footer Email

contact@studyhub.app

---

## Handoff Notes

- Provide SVG icons for each feature
- Include hero illustration or dashboard mockup
- Use optimized images for mobile and desktop
- Include font files or CDN links (Montserrat, Roboto)
- Provide accessibility checklist:
  - Headings structure
  - Alt text
  - Focus states
  - Skip link
- Ensure proper color contrast validation