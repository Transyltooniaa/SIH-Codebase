const path = require('path');

function resolveSrc(_path) {
  return path.join(__dirname, _path);
}

module.exports = {
  lintOnSave: true, // Enable linting on save
  publicPath: process.env.NODE_ENV === 'production' ? '/deployment/' : '/', // Set public path for GitHub Pages
  configureWebpack: {
    resolve: {
      alias: {
        assets: resolveSrc('src/assets') // Set up aliases for assets
      }
    }
  },
  css: {
    sourceMap: process.env.NODE_ENV !== 'production' // Enable CSS source maps in development
  }
};
