/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*/templates/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        'ubuntu-mono': ["'Ubuntu Mono'",'mono','sans-serif'],
        'raleway': ["'Raleway'",'sans-serif'],
      }
    },
  },
  plugins: [],
}
