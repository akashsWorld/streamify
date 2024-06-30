/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
  ],
  theme: {
    colors:{
      white:'#E2E8F0',
      black:'#000',
      transparent: 'transparent'
    },
    fontFamily:{
      'body':["Dosis", 'sans-serif'],
      'heading':["Jost", 'sans-serif']
    },
    extend: {
    },
  },
  plugins: [],
}
