---


name: cm-auto-publisher
description: "CORE — Đưa nội dung Markdown lên trang web Astro tự động qua Router API."
version: 2.0.0
---

# cm-auto-publisher — Automated Content Publisher (LITE)

> **Goal:** Automate the publishing workflow for articles (Markdown + Media) to an Astro website system via a Router API, ensuring Git history consistency and intelligent image handling.

## When to Activate

- Publishing a blog post or article to a hosted site
- Pushing a lesson plan or educational content to a web system
- Automating content delivery from a pipeline (downstream of `cm-content-factory`)
- Fetching content from a URL and republishing it automatically

## Instructions

### API Payload Structure

| Field | Type | Description |
|-------|------|-------------|
| `site_id` | String | Target website ID (e.g., `cody-master`). |
| `title` | String | Compelling, SEO-friendly title. |
| `description` | String | Meta description (1-2 sentences). |
| `content` | String | Raw Markdown content. |
| `media` | Array | Array of `[{url: "...", filename: "kebab-case.jpg"}]`. |

### 5-Phase Publish Workflow

1. **Analyze:** Extract content from URL / Video / Raw text.
2. **Media Prep:** Build the `media` array with kebab-case filenames.
3. **Payload:** Construct the complete JSON payload.
4. **Push:** Send POST request to Router API (Cloudflare Workers) with API Key.
5. **Verify:** Confirm `{"success": true}` response and report the commit SHA.

### Execution Rules

- **Router API:** `https://content-factory-router.<ACCOUNT>.workers.dev/publish`
- **Method:** POST with `Authorization: Bearer <API_KEY>`.
- **Media:** Do NOT download images locally. The Router API handles them from their source URL automatically.

## Quality Gate (Red Flags)

- ❌ Manually creating `.mdx` files and running `git push` directly (causes data conflicts).
- ❌ Using `echo` or `cat` to construct complex JSON (must write to a `.json` file).
- ❌ Non-SEO-compliant media filenames (must use kebab-case).
- ❌ Missing API Key or incorrect `site_id`.

## Example Triggers

- "Publish this article to the CodyMaster blog."
- "Fetch the news from [URL] and push it to the news site automatically."
- "Publish the Robotics lesson draft to the platform."
- "Automate publishing the output of the content factory to the web."
