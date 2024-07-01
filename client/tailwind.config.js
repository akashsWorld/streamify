/** @type {import('tailwindcss').Config} */
const {transparent,black,red,white, gray}= require('tailwindcss/colors')

module.exports = {
  content: [
    "./src/**/*.{html,ts}",
  ],
  theme: {
    colors:{
      white:'#E2E8F0',
      black: black,
      red,
      transparent: transparent,
      primaryWhite: white,
      gray
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
