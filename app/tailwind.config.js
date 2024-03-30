/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./App.{js,jsx,ts,tsx}",
    "./components/**/*.{js,jsx,ts,tsx}",
    "./screens/**/*.{js,jsx,ts,tsx}"
  ],
  theme: {
    colors: {
      primary: "#FFFFFF",
      secondary: "#000000",
      accent: "#6366f1",
    }
  },
  plugins: [],
}

