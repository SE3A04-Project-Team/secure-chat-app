/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./App.{js,jsx,ts,tsx}",
    "./components/**/*.{js,jsx,ts,tsx}",
    "./screens/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#FFFFFF',
        secondary: '#000000',
        accent: '#86EFAC',
        admin_accent: '#93C5FD',
        input_field: '#F4F4F5',
      },
      backgroundColor: theme => theme('colors'),
      textColor: theme => theme('colors'),
    },
  },
  plugins: [],
}

