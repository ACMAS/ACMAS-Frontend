/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './app/ACMAS_Web/templates/**/*.html'
  ],
  theme: {
    extend: {},
    colors: {
      "black": "#000000",
      "gray-500": "#595959",
      "gray-700": "#999999",
      "gray-900": "#d9d9d9",
      "white": "#ffffff",
      "acmas-blue": "#327796",
      "primary-100": "#003eb3",
      "primary-300": "#0074f0",
      "primary-500": "#14a9ff",
      "primary-700": "#85dcff",
      "success-300": "#199033",
      "success-500": "#32a94c",
      "success-700": "#4cc366",
      "danger-300": "#a22020",
      "danger-500": "#bf2626",
      "danger-700": "#e14747",
    },
  },
  plugins: [],
}
