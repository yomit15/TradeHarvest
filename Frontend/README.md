This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.

```
trade-harvest
├─ next.config.mjs
├─ package-lock.json
├─ package.json
├─ postcss.config.mjs
├─ public
│  ├─ icons
│  ├─ images
│  │  ├─ apple.jpeg
│  │  ├─ carrot.jpg
│  │  ├─ corn.jpg
│  │  ├─ drought.jpeg
│  │  ├─ ginger.jpg
│  │  ├─ lady.jpeg
│  │  ├─ logo.png
│  │  ├─ market.jpg
│  │  ├─ minister.jpg
│  │  ├─ photo.jpg
│  │  ├─ potato.jpg
│  │  ├─ scheme1.png
│  │  ├─ scheme2.jpg
│  │  ├─ scheme3.webp
│  │  ├─ scheme4.jpg
│  │  ├─ ship.jpg
│  │  ├─ tomato.jpg
│  │  ├─ weather.png
│  │  └─ wheat.jpg
│  ├─ next.svg
│  └─ vercel.svg
├─ README.md
├─ src
│  ├─ app
│  │  ├─ (auth)
│  │  │  ├─ sign-in
│  │  │  │  └─ [[...sign-in]]
│  │  │  │     └─ page.tsx
│  │  │  └─ sign-up
│  │  │     └─ [[...sign-up]]
│  │  │        └─ page.tsx
│  │  ├─ (root)
│  │  │  ├─ (home)
│  │  │  │  ├─ cart
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ explore
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ layout.tsx
│  │  │  │  ├─ list
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ messaging
│  │  │  │  │  └─ page.tsx
│  │  │  │  ├─ page.tsx
│  │  │  │  ├─ profile
│  │  │  │  │  └─ page.tsx
│  │  │  │  └─ shopping
│  │  │  │     └─ page.tsx
│  │  │  └─ layout.tsx
│  │  ├─ data
│  │  │  ├─ carousel.ts
│  │  │  ├─ items.ts
│  │  │  └─ news.ts
│  │  ├─ favicon.ico
│  │  ├─ globals.css
│  │  ├─ layout.tsx
│  │  └─ [id]
│  │     └─ page.tsx
│  ├─ components
│  │  ├─ graph.tsx
│  │  ├─ logo.tsx
│  │  ├─ navbar.tsx
│  │  ├─ news.tsx
│  │  ├─ trending.tsx
│  │  └─ ui
│  │     ├─ avatar.tsx
│  │     ├─ badge.tsx
│  │     ├─ button.tsx
│  │     ├─ calendar.tsx
│  │     ├─ card.tsx
│  │     ├─ carousel.tsx
│  │     ├─ chart.tsx
│  │     ├─ input.tsx
│  │     ├─ label.tsx
│  │     ├─ popover.tsx
│  │     ├─ separator.tsx
│  │     ├─ sheet.tsx
│  │     └─ textarea.tsx
│  ├─ context
│  │  └─ ProductsContext.tsx
│  ├─ lib
│  │  └─ utils.ts
│  └─ middleware.ts
├─ tailwind.config.ts
└─ tsconfig.json

```