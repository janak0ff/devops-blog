---
title: How to Connect a Netlify sites to a Custom Domain or subdomain Using Cloudflare with SSL Certificate
pubDatetime: 2025-05-21
featured: true
tags:
  - Step-by-Step Guide
  - Netlify
  - Domain Configure
description: Connect Custom Domain\subdomain via Cloudflare,  Point DNS from Cloudflare to Netlify, Verify Domain Ownership with Netlify via Cloudflare, Ensure SSL (HTTPS) Works
---

To connect your Netlify any site to your custom domain or subdomain `https://blogs.janakkumarshrestha0.com.np` using **Cloudflare**, follow this step-by-step guide:

---

## ✅ Step-by-Step: Connect Custom Domain via Cloudflare

### 📌 Prerequisites:

- Your site is already deployed and live on **Netlify**
- You own/manage the `.com.np` domain via **Cloudflare**

---

## 🔧 STEP 1: Add Domain to Netlify

1. Go to your site on [Netlify](https://app.netlify.com/)
2. Navigate to:
   `Site settings → Domain Management → Add a domain`
3. Click **Add a domain you already own”**
4. Enter your sub domain:
   `blogs.janakkumarshrestha0.com.np`
5. Click **Verify**, then **Add domain**

---

## 🌐 STEP 2: Point DNS from Cloudflare to Netlify

1. Go to your domain in [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. Go to the **DNS** tab
3. Add a new **CNAME** record:

   | Type  | Name | Target                  | TTL  | Proxy |
   | ----- | ---- | ----------------------- | ---- | ----- |
   | CNAME | blog | `your-site.netlify.app` | Auto | ✅ ON |

   - Replace `your-site.netlify.app` with your actual Netlify subdomain (found on your Netlify dashboard).
   - `Name` is `blog`, not the full domain.

---

### 🔑 STEP 3: Verify Domain Ownership with Netlify via Cloudflare

**Netlify needs to verify** that you **own the domain** `example.com.np` before it allows you to add a subdomain like `sub.example.com.np`.

sub.example.com.np is an alias of examples.netlify.app and has its traffic proxied through Cloudflare.

To verify ownership using **Cloudflare DNS**, follow these steps:

---

### Copy TXT Record from Netlify

From Netlify:

- **Host**: `netlify-challenge`
- **Value**: `your-value`

---

### Add TXT Record in Cloudflare

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. Select your domain: `yourdomain.com.np`
3. Go to the **DNS** tab
4. Click **“Add record”**
5. Choose:

   - **Type**: `TXT`
   - **Name (Host)**: `netlify-challenge`
   - **Content (Value)**: `your-value`
   - TTL: Auto

6. Click **Save**

---

## 🔒 STEP 4: Ensure SSL (HTTPS) Works

- **On Netlify**:

  - Go to **Site settings → Domain Management → HTTPS**
  - Enable **Automatic HTTPS (Let’s Encrypt)** if not already

- **On Cloudflare**:

  - Go to **SSL/TLS → Overview**
  - Set SSL mode to **Full** or **Full (Strict)**

---

## 🚀 STEP 5: Test Your Domain

- Open a browser and go to:

  ```
  https://blog.janakkumarshrestha0.com.np/
  ```

- It should load your Netlify blog.

---

### ✅ Done!

Your blog is now live at your custom domain using Netlify + Cloudflare DNS.
