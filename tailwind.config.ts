import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
        charcoal: {
          900: "#0f1115",
          800: "#161b22",
          700: "#21262d",
        },
        neon: {
          blue: "#00f0ff",
        },
      },
      fontFamily: {
        sans: ['var(--font-inter)', 'sans-serif'],
      }
    },
  },
  plugins: [],
};
export default config;
